from typing import List

from sqlalchemy.orm import Session

from domain.recibo import Recibo
from infrastructure.db.models.recibo_model import ReciboModel
from services.recibo_repository import ReciboRepository


class PostgresReciboRepository(ReciboRepository):
    """Repositório PostgreSQL para persistência de Recibo via SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def salvar(self, recibo: Recibo) -> None:
        db_recibo = ReciboModel(
            total=recibo.total,
            metodo=recibo.metodo,
            parcelas=recibo.parcelas,
            informacoes_adicionais=recibo.informacoes_adicionais,
            valor_parcela=recibo.valor_parcela,
            created_at=recibo.data_hora,
        )
        self.db.add(db_recibo)
        self.db.commit()
        self.db.refresh(db_recibo)

    def listar_todos(self) -> List[ReciboModel]:
        return (
            self.db.query(ReciboModel)
            .order_by(ReciboModel.created_at.desc())
            .all()
        )