from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np

from engine.player_classifier import load_classifier, predict_player_position

router = APIRouter(prefix="/classify", tags=["Player Classifier"])

class RouteInput(BaseModel):
    route: list  # list of {x, y} dicts

@router.post("/player")
def classify_player(data: RouteInput):
    if not data.route or len(data.route) < 2:
        raise HTTPException(400, "Route must have at least 2 points")

    route_np = np.array([[p["x"], p["y"]] for p in data.route])
    clf = load_classifier()
    pred = predict_player_position(route_np)
    return {"predicted_role": pred}
