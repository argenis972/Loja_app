from sqlalchemy.orm import Session

from domain.recibo import Recibo
from services.recibo_repository import ReciboRepository


class ArquivoReciboRepository(ReciboRepository):
    """File-based repository for Recibo persistence."""

    def __init__(self, caminho: str):
        self.caminho = caminho

    def salvar(self, recibo: Recibo) -> None:
        with open(self.caminho, "a") as f:
            f.write(f"{recibo}\n")


class PostgresReciboRepository(ReciboRepository):
    """PostgreSQL-based repository for Recibo persistence using SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def salvar(self, recibo: Recibo) -> None:
        from infrastructure.models import ReciboModel

        db_recibo = ReciboModel(
            total=recibo.total,
            metodo=recibo.metodo,
            parcelas=recibo.parcelas,
            informacoes_adicionais=recibo.informacoes_adicionais,
            created_at=recibo.data_hora,
        )
        self.db.add(db_recibo)
        self.db.commit()
        self.db.refresh(db_recibo)
