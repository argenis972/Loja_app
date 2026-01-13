from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ReciboResponse(BaseModel):
    id: int
    total: float
    metodo: str
    parcelas: int
    informacoes_adicionais: str = ""
    valor_parcela: float

    data_hora = Column(DateTime, server_default=sa.func.now(), nullable=False)

    # Compatibilidad con tu schema mostrado en Swagger
    data_hora: datetime | None = None
