from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np

# Import the classifier and prediction functions
from src.engine.player_classifier import load_classifier, predict_player_position

router = APIRouter(prefix="/classify", tags=["Player Classifier"])

# Load the model ONCE at import time (fast, correct way)
model = load_classifier()

class RoutePoint(BaseModel):
    x: float
    y: float

class RouteInput(BaseModel):
    route: list[RoutePoint]

@router.post("/player")
def classify_player(data: RouteInput):
    # Validate route input
    if len(data.route) < 2:
        raise HTTPException(status_code=400, detail="Route must have at least 2 points")

    # Convert list of RoutePoint -> numpy array (N, 2)
    route_np = np.array([[p.x, p.y] for p in data.route])

    # Predict using the pre-loaded model
    pred = predict_player_position(model, route_np)

    return {"predicted_role": str(pred)}
