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
    created_at: datetime | None = None

    # Compatibilidad con tu schema mostrado en Swagger
    data_hora: datetime | None = None
