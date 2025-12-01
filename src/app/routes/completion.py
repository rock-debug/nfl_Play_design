from fastapi import APIRouter
from src.engine.play_sim import simulate_demo

router = APIRouter(prefix="/completion", tags=["Completion"])

@router.get("/play")
def simulate_play(T: int = 40):
    off, deff, oroute, droute, timeline = simulate_demo(
        T=T, visualize=False, analytics=True
    )
    return {"timeline": timeline}

@router.get("/best_target")
def best_target(T: int = 40):
    _, _, _, _, timeline = simulate_demo(T=T, visualize=False, analytics=True)
    arr = [
        {
            "frame": f["frame"],
            "best_id": f["best_target"]["id"],
            "prob": f["best_target"]["prob"]
        }
        for f in timeline
    ]
    return {"best": arr}
