from fastapi import APIRouter
from src.app.models.play_schema import PlayData
from src.app.services.coverage_inference import predict_play_coverage

router = APIRouter(prefix="/coverage", tags=["Coverage"])

@router.post("/predict")
def predict_coverage(play: PlayData):
    return predict_play_coverage(play)
