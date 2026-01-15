from datetime import datetime

from pydantic import BaseModel


class ReciboResponse(BaseModel):
    id: int
    total: float
    created_at: datetime

    class Config:
        from_attributes = True
