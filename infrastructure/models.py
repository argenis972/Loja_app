from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ReciboModel(Base):
    __tablename__ = "recibos"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    metodo = Column(String(50), nullable=False)
    parcelas = Column(Integer, nullable=False)
    informacoes_adicionais = Column(Text, nullable=True)

    # IMPORTANTE: esta coluna precisa existir também no SQLite de testes
    valor_parcela = Column(Float, nullable=False)

    created_at = Column(DateTime, nullable=True)