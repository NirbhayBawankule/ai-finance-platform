from fastapi import FastAPI, Header, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from db import supabase
from predict import predict_next
from upload import process_csv
from advisor import generate_advice
from report import generate_pdf

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- EXPENSES ----------------
@app.get("/expenses")
def get_expenses(user_id: str = Header(...)):
    return supabase.table("expenses").select("*").eq("user_id", user_id).execute().data


# ---------------- CSV UPLOAD ----------------
@app.post("/upload-csv")
def upload_csv(
    user_id: str = Header(...),
    file: UploadFile = File(...)
):
    process_csv(file.file, user_id)
    return {"status": "uploaded"}


# ---------------- PREDICTIONS ----------------
@app.post("/predict")
def run_predictions(user_id: str = Header(...)):
    expenses = supabase.table("expenses").select("*").eq("user_id", user_id).execute().data

    if not expenses:
        raise HTTPException(status_code=400, detail="No expenses found")

    prediction_month = datetime.now().strftime("%Y-%m")
    predictions = {}

    for category in set(e["category"] for e in expenses):
        values = [e["amount"] for e in expenses if e["category"] == category]

        try:
            pred = predict_next(values, category)
        except KeyError:
            continue

        supabase.table("predictions").delete() \
            .eq("user_id", user_id) \
            .eq("category", category) \
            .eq("prediction_month", prediction_month) \
            .execute()

        supabase.table("predictions").insert({
            "user_id": user_id,
            "category": category,
            "predicted_amount": pred,
            "prediction_month": prediction_month
        }).execute()

        predictions[category] = pred

    return predictions


# ---------------- ADVISOR ----------------
@app.post("/advisor")
def advisor(user_id: str = Header(...)):
    preds = supabase.table("predictions").select("*").eq("user_id", user_id).execute().data
    return {"advice": generate_advice(preds, [])}


# ---------------- PDF REPORT ----------------
@app.get("/report")
def report(user_id: str = Header(...)):
    preds = supabase.table("predictions").select("*").eq("user_id", user_id).execute().data
    data = {p["category"]: p["predicted_amount"] for p in preds}

    path = generate_pdf(data)
    return {"file": path}
