"""SQLAlchemy models for database persistence."""

from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database import Base


class ReciboModel(Base):
    """SQLAlchemy model for Recibo entity."""

    __tablename__ = "recibos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    total: Mapped[float] = mapped_column(Float, nullable=False)
    metodo: Mapped[str] = mapped_column(String(50), nullable=False)
    parcelas: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    informacoes_adicionais: Mapped[str] = mapped_column(
        String(500), default="", nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    def __repr__(self) -> str:
        return f"<ReciboModel(id={self.id}, total={self.total}, metodo={self.metodo})>"
