"""
Database initialization and session management.
"""
from __future__ import annotations

import logging
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.config import DATABASE_URL
from backend.database.models import Base

logger = logging.getLogger(__name__)

# Ensure the parent directory exists
db_path = Path(DATABASE_URL.replace("sqlite:///", ""))
db_path.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Create all tables if they don't exist."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized at %s", DATABASE_URL)


def get_session() -> Session:
    """Return a new database session (caller must close)."""
    return SessionLocal()
