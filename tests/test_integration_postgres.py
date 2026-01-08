"""Integration test demonstrating PostgreSQL repository with API deps."""

import os
import tempfile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.recibo import Recibo
from infrastructure.database import Base
from infrastructure.models import ReciboModel
from infrastructure.storage import PostgresReciboRepository


def test_integration_postgres_repository_with_env_var():
    """
    Test that demonstrates PostgreSQL repository integration.
    Uses SQLite in-memory for testing without requiring actual PostgreSQL.
    """
    # Create in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:
        # Create repository
        repo = PostgresReciboRepository(db)

        # Create and save multiple recibos
        recibo1 = Recibo(total=90.0, metodo="dinheiro", parcelas=1)
        recibo2 = Recibo(total=95.0, metodo="cartao", parcelas=1)
        recibo3 = Recibo(total=100.0, metodo="parcelado", parcelas=6)

        repo.salvar(recibo1)
        repo.salvar(recibo2)
        repo.salvar(recibo3)

        # Query and verify all recibos
        all_recibos = db.query(ReciboModel).all()
        assert len(all_recibos) == 3

        # Verify individual recibos
        assert all_recibos[0].total == 90.0
        assert all_recibos[0].metodo == "dinheiro"

        assert all_recibos[1].total == 95.0
        assert all_recibos[1].metodo == "cartao"

        assert all_recibos[2].total == 100.0
        assert all_recibos[2].metodo == "parcelado"
        assert all_recibos[2].parcelas == 6

    finally:
        db.close()


def test_database_created_with_sqlite_url():
    """Test that database file is created with SQLite URL."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Set up database with file path
        engine = create_engine(f"sqlite:///{tmp_path}")
        Base.metadata.create_all(bind=engine)

        # Verify file was created
        assert os.path.exists(tmp_path)

        # Verify table exists
        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()

        try:
            # Save a recibo
            repo = PostgresReciboRepository(db)
            recibo = Recibo(total=100.0, metodo="test", parcelas=1)
            repo.salvar(recibo)

            # Verify it was saved
            saved = db.query(ReciboModel).first()
            assert saved is not None
            assert saved.total == 100.0
        finally:
            db.close()

    finally:
        # Clean up
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
