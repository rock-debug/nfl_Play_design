import numpy as np
from src.app.services.utils import compute_basic_features

def predict_play_coverage(play):
    """Dummy model until ML integration is ready"""
    off = np.array([[p.x, p.y] for r in play.offense for p in r.route])
    defn = np.array([[p.x, p.y] for r in play.defense for p in r.route])

    # Later: replace with your trained ML model
    features = compute_basic_features(off, defn)
    fake_pred = "Cover2" if features["num_deep"] >= 2 else "Cover1"

    return {
        "predicted_coverage": fake_pred,
        "features": features,
        "confidence": 0.85,
    }
