# app/schemas.py
from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class WorldStateBase(BaseModel):
    world_id: str
    version: int
    data: Dict[str, Any]


class WorldStateCreate(BaseModel):
   
    pass


class WorldStateResponse(WorldStateBase):
    id: int

    class Config:
        orm_mode = True


class EventProposal(BaseModel):
    world_id: str
    max_events: int = 5


class EventResult(BaseModel):
    approved_events: List[Dict[str, Any]]
    rejected_events: List[Dict[str, Any]]
    world_version: int
