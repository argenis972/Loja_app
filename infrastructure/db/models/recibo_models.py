from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from infrastructure.db.base import Base


class ReciboModel(Base):
    __tablename__ = "recibos"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    metodo = Column(String(50), nullable=False)
    parcelas = Column(Integer, nullable=False)
    informacoes_adicionais = Column(Text, nullable=True)
    valor_parcela = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    @property
    def data_hora(self):
        return self.created_at
