import numpy as np
from models_loader import MODELS

def predict_next(values, category):
    if category not in MODELS:
        raise KeyError("Model not found for category")

    model = MODELS[category]
    X = np.arange(len(values)).reshape(-1, 1)
    next_step = np.array([[len(values)]])

    return float(model.predict(next_step)[0])
