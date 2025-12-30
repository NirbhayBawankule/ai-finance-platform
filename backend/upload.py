import pandas as pd
from db import supabase

def process_csv(file, user_id):
    df = pd.read_csv(file)

    records = []
    for _, row in df.iterrows():
        records.append({
            "user_id": user_id,
            "month_year": row["month_year"],
            "category": row["category"],
            "amount": row["amount"]
        })

    supabase.table("expenses").insert(records).execute()
