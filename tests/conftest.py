import os
import subprocess

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from api.main import app
from infrastructure.database import SessionLocal, init_db


@pytest.fixture(scope="session")
def db_migrated():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        pytest.skip("DATABASE_URL não configurada")

    subprocess.run(
        ["alembic", "upgrade", "head"],
        check=True,
        env={**os.environ, "DATABASE_URL": database_url},
    )

    init_db()
    yield


@pytest.fixture(scope="function")
def db_session(db_migrated):
    db = SessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE recibos RESTART IDENTITY;"))
        db.commit()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c
