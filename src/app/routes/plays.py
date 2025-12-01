from fastapi import APIRouter, UploadFile, File, HTTPException
import json

router = APIRouter(prefix="/plays", tags=["Plays"])

@router.post("/upload")
async def upload_play(file: UploadFile = File(...)):
    if file.content_type not in ("application/json", "text/json"):
        raise HTTPException(400, "Only JSON uploads supported for now.")
    content = await file.read()
    data = json.loads(content.decode("utf-8"))
    # TODO: validate, store to DB
    return {"filename": file.filename, "players": len(data.get("players", [])), "status": "uploaded"}
