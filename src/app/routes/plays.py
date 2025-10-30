from fastapi import APIRouter, UploadFile, File
from typing import List
import json

router = APIRouter(prefix="/plays", tags=["Plays"])

@router.post("/upload")
async def upload_play(file: UploadFile = File(...)):
    """Upload a play file (JSON or CSV)"""
    content = await file.read()
    data = json.loads(content.decode("utf-8"))
    # TODO: validate & store
    return {"filename": file.filename, "status": "uploaded", "num_players": len(data.get("players", []))}
