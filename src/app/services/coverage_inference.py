import numpy as np
from src.app.services.utils import arr_from_routes, num_deep_defenders

def predict_play_coverage(play):
    off_routes = arr_from_routes(play.offense)
    def_routes = arr_from_routes(play.defense)
    deep = num_deep_defenders(def_routes, eval_idx=min(10, def_routes.shape[1]-1), depth_thresh=18.0)
    # very simple heuristic placeholder
    pred = "Cover2" if deep >= 2 else ("Cover1" if deep == 1 else "Cover3/Zone")
    return {
        "predicted_coverage": pred,
        "num_deep_defenders": deep,
        "frames": int(def_routes.shape[1]) if def_routes.size else 0,
        "note": "Replace with trained classifier later."
    }
