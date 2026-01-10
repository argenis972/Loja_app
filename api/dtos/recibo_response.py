from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReciboResponse(BaseModel):
    id: int | None = None
    total: float
    metodo: str
    parcelas: int
    informacoes_adicionais: str = ""
    created_at: datetime | None = None
    data_hora: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
