from pydantic import BaseModel, Field
from typing import List, Dict

class PlayerPosition(BaseModel):
    x: float = Field(..., description="Field x (yards)")
    y: float = Field(..., description="Field y (yards)")

class PlayerRoute(BaseModel):
    id: str
    team: str  # "off" | "def"
    role: str  # WR/CB/QB/etc
    route: List[PlayerPosition]  # array of frames for this player

class PlayData(BaseModel):
    offense: List[PlayerRoute]
    defense: List[PlayerRoute]
    metadata: Dict[str, str] = {}
