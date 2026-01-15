from fastapi import Depends

from infrastructure.database import SessionLocal
from infrastructure.storage import PostgresReciboRepository
from services.pagamento_service import PagamentoService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_recibo_repository(db=Depends(get_db)):
    return PostgresReciboRepository(db)


def get_pagamento_service(
    repo=Depends(get_recibo_repository),
):
    return PagamentoService(repo)
