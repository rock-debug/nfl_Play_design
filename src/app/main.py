from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.routes import plays, coverage

app = FastAPI(title="NFL Play Designer Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev mode
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plays.router)
app.include_router(coverage.router)

@app.get("/")
def root():
    return {"message": "NFL Play Designer API is running"}
app.include_router(plays.router)
app.include_router(classify.router)
app.include_router(coverage.router)
app.include_router(completion.router)
