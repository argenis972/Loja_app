import os
import subprocess

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from api.main import app
from infrastructure.database import SessionLocal


@pytest.fixture(scope="session", autouse=True)
def aplicar_migracoes() -> None:
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        return

    subprocess.run(
        ["alembic", "upgrade", "head"],
        check=True,
        env={**os.environ, "DATABASE_URL": database_url},
    )


@pytest.fixture(scope="function")
def client():
    """
    Cliente de teste para a API usando Postgres.

    Limpa a tabela a cada teste para manter isolamento e evitar efeitos colaterais.
    """
    db = SessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE recibos RESTART IDENTITY;"))
        db.commit()
    finally:
        db.close()

    with TestClient(app) as c:
        yield c
