import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.base import Base  # noqa: F401
from infrastructure.db.models.recibo_model import ReciboModel  # noqa: F401


def _get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL não configurada. Exemplo: "
            "postgresql+psycopg://usuario:senha@localhost:5432/loja_db"
        )
    return database_url


DATABASE_URL = _get_database_url()

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator:
    """Dependência do FastAPI que fornece uma sessão."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    """Cria todas as tabelas (use migrações/alembic preferencialmente)."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Generator:
    """Context manager para consumidores fora do FastAPI (ex.: CLI)."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
