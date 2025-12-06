# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime

from .db import Base


class WorldState(Base):
    __tablename__ = "world_states"

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(String, index=True)
    version = Column(Integer, default=1)
    data = Column(JSON)  # world JSON
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Integer, default=1)  # 1 = active, 0 = archived


class WorldSnapshot(Base):
    __tablename__ = "world_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(String, index=True)
    version = Column(Integer)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
