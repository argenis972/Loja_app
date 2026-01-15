import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from infrastructure.db.base import Base
from infrastructure.db.models.recibo_models import ReciboModel  # noqa: F401

engine = create_engine(settings.database_url, future=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL não configurada. "
            "Exemplo: postgresql+psycopg://usuario:senha@localhost:5432/loja_db"
        )
    return database_url


def get_engine():
    return create_engine(get_database_url(), echo=False)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def session_scope() -> Generator:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
