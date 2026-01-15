from datetime import datetime

from pydantic import BaseModel


class ReciboResponse(BaseModel):
    id: int
    pedido_id: int
    valor_total: float
    created_at: datetime

    class Config:
        from_attributes = True
