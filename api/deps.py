"""Dependency injection for FastAPI endpoints."""

import os

from config.settings import TaxasConfig, get_settings
from infrastructure.database import get_db
from infrastructure.storage import (ArquivoReciboRepository,
                                    PostgresReciboRepository)
from services.pagamento_service import PagamentoService
from services.recibo_repository import ReciboRepository


def get_recibo_repository() -> ReciboRepository:
    """
    Get the appropriate recibo repository based on DATABASE_URL environment variable.

    If DATABASE_URL is set and points to postgres, use PostgresReciboRepository.
    Otherwise, fallback to file-based repository for local development/testing.
    """
    database_url = os.getenv("DATABASE_URL", "")

    if database_url and database_url.startswith("postgres"):
        # Use PostgreSQL repository
        db = next(get_db())
        return PostgresReciboRepository(db)
    else:
        # Fallback to file-based repository
        return ArquivoReciboRepository("receipts/recibos.txt")


def get_pagamento_service() -> PagamentoService:
    """Get configured PagamentoService with taxas and repository."""
    try:
        taxas = get_settings()
    except Exception:
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    repo = get_recibo_repository()
    return PagamentoService(taxas.desconto_vista, taxas.juros_parcelamento, repo)
