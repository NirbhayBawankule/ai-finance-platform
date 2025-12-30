import joblib

MODELS = {
    "bills": joblib.load("models/bills__linear.pkl"),
    "entertainment": joblib.load("models/entertainment__linear.pkl"),
    "food": joblib.load("models/food__rf.pkl"),
    "health": joblib.load("models/health__rf.pkl"),
    "shopping": joblib.load("models/shopping__rf.pkl"),
    "utilities": joblib.load("models/utilities__linear.pkl"),
}
