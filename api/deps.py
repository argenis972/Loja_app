import os

from fastapi import Depends
from sqlalchemy.orm import Session

from config.settings import TaxasConfig, get_settings
from infrastructure.database import get_db
from infrastructure.storage import ArquivoReciboRepository, PostgresReciboRepository
from services.pagamento_service import PagamentoService
from services.recibo_repository import ReciboRepository


def get_recibo_repository(db: Session = Depends(get_db)) -> ReciboRepository:

    database_url = os.getenv("DATABASE_URL", "")

    if database_url and database_url.startswith("postgres"):
        return PostgresReciboRepository(db)
    return ArquivoReciboRepository("receipts/recibos.txt")


def get_pagamento_service(
    repo: ReciboRepository = Depends(get_recibo_repository),
) -> PagamentoService:
    try:
        taxas = get_settings()
    except Exception:
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    return PagamentoService(taxas.desconto_vista, taxas.juros_parcelamento, repo)
