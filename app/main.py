# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import Base, engine, get_db
from . import models
from .schemas import (
    WorldStateResponse,
    WorldStateCreate,
    EventProposal,
    EventResult,
)
from .services.world_service import create_world, propose_events_for_world


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="game Backend",
    version="0.1.0",
    description="Prototype multi-agent backend.",
)


@app.post("/generate_world", response_model=WorldStateResponse)
def generate_world(
    payload: WorldStateCreate | None = None, db: Session = Depends(get_db)
):
    world_state = create_world(db)
    return WorldStateResponse(
        id=world_state.id,
        world_id=world_state.world_id,
        version=world_state.version,
        data=world_state.data,
    )


@app.post("/propose_events", response_model=EventResult)
def propose_events_endpoint(
    payload: EventProposal, db: Session = Depends(get_db)
):
    try:
        result = propose_events_for_world(
            db, world_id=payload.world_id, max_events=payload.max_events
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return EventResult(**result)
