from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.routes import plays, coverage

app = FastAPI(title="NFL Play Designer Backend", version="0.1.0")

# Allow frontend (React/Streamlit) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(plays.router)
app.include_router(coverage.router)

@app.get("/")
def root():
    return {"message": "NFL Play Designer API is running"}
