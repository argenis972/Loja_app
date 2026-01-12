import os
import subprocess

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from api.main import app
from infrastructure.database import SessionLocal


@pytest.fixture(scope="session", autouse=True)
def aplicar_migracoes() -> None:
    """
    Garante que o banco de testes esteja migrado antes de rodar a suíte.

    Requer:
    - DATABASE_URL apontando para o banco de testes (ex.: loja_test_db)

    Em CI (GitHub Actions), a variável é injetada pelo workflow.
    Em ambiente local, o desenvolvedor deve defini-la manualmente.
    """
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL não configurada para testes. "
            "Defina a variável de ambiente antes de rodar o pytest."
        )

    # Executa migrações apenas uma vez por sessão
    subprocess.check_call(["alembic", "upgrade", "head"])


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
