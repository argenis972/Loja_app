import os
import subprocess

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import text

from api.main import app
from infrastructure.database import SessionLocal, init_db

# Carga EXCLUSIVAMENTE el env de test
load_dotenv(".env.test", override=True)


@pytest.fixture(scope="session", autouse=True)
def db_migrated():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL não configurada para testes")

    subprocess.run(
        ["alembic", "upgrade", "head"],
        check=True,
        env={**os.environ, "DATABASE_URL": database_url},
    )

    init_db()
    yield


@pytest.fixture(scope="function")
def db_session():
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
