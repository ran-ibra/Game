# app/services/world_service.py
from typing import Dict, Any

from sqlalchemy.orm import Session

from ..models import WorldState, WorldSnapshot
from ..agents.world_designer import generate_base_world
from ..agents.content_builder import build_initial_content
from ..agents.events_agent import propose_events
from ..agents.narrative_controller import validate_events


def create_world(db: Session) -> WorldState:
    world = generate_base_world()
    world = build_initial_content(world)

    world_id = world["world_id"]
    version = 1

    world_state = WorldState(
        world_id=world_id,
        version=version,
        data=world,
        is_active=1,
    )
    db.add(world_state)
    db.commit()
    db.refresh(world_state)

    snapshot = WorldSnapshot(
        world_id=world_id,
        version=version,
        data=world,
    )
    db.add(snapshot)
    db.commit()

    return world_state


def get_active_world(db: Session, world_id: str) -> WorldState | None:
    return (
        db.query(WorldState)
        .filter(WorldState.world_id == world_id, WorldState.is_active == 1)
        .order_by(WorldState.version.desc())
        .first()
    )


def propose_events_for_world(
    db: Session, world_id: str, max_events: int = 5
) -> Dict[str, Any]:
    world_state = get_active_world(db, world_id)
    if not world_state:
        raise ValueError("World not found or inactive.")

    world_data = world_state.data

    raw_events = propose_events(world_data, max_events=max_events)
    approved, rejected = validate_events(world_data, raw_events)

    result = {
        "approved_events": approved,
        "rejected_events": rejected,
        "world_version": world_state.version,
    }
    return result
def save_world_state(
    db: Session, world_id: str, new_data: Dict[str, Any]
) -> WorldState:
    current_state = get_active_world(db, world_id)
    if not current_state:
        raise ValueError("World not found or inactive.")

    current_state.is_active = 0
    db.commit()

    new_version = current_state.version + 1
    new_world_state = WorldState(
        world_id=world_id,
        version=new_version,
        data=new_data,
        is_active=1,
    )
    db.add(new_world_state)
    db.commit()
    db.refresh(new_world_state)

    snapshot = WorldSnapshot(
        world_id=world_id,
        version=new_version,
        data=new_data,
    )
    db.add(snapshot)
    db.commit()

    return new_world_state                                      