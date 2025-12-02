from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your route modules correctly
from src.app.routes import plays, coverage, classify, completion
from src.engine.player_classifier import load_classifier, predict_player_position

app = FastAPI(
    title="NFL Play Designer Backend",
    version="0.1.0"
)

# CORS (development mode)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers (ONLY once)
app.include_router(plays.router, prefix="/plays")
app.include_router(classify.router, prefix="/classify")
app.include_router(coverage.router, prefix="/coverage")
app.include_router(completion.router, prefix="/completion")

@app.get("/")
def root():
    return {"message": "NFL Play Designer API is running"}
