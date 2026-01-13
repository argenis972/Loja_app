import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.base import Base  # noqa: F401
from infrastructure.db.models.recibo_model import ReciboModel  # noqa: F401


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL não configurada. "
            "Exemplo: postgresql+psycopg://usuario:senha@localhost:5432/loja_db"
        )
    return database_url


def get_engine():
    return create_engine(
        get_database_url(),
        echo=False,
    )


engine = None
SessionLocal = None


def init_db():
    global engine, SessionLocal

    if engine is None:
        engine = get_engine()
        SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine,
        )


def get_db() -> Generator:
    init_db()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    init_db()
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Generator:
    init_db()
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
