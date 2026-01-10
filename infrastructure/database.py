import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.base import Base  # noqa: F401
from infrastructure.db.models.recibo_model import ReciboModel  # noqa: F401

# Default to a local SQLite database when DATABASE_URL is not provided.
# This keeps tests and local development self-contained while allowing
# PostgreSQL or any other SQLAlchemy-supported backend via env var.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./receipts/recibos.db",
)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator:
    """FastAPI dependency that yields a scoped session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    """Create all tables defined on the metadata."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Generator:
    """Context manager for non-FastAPI callers that need a session."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
