from pydantic import BaseModel
from typing import Optional

class PagamentoResponse(BaseModel):
    total: float
    metodo: str
    descricao: str
    parcelas: int          # ⬅️ NO Optional
    valor_parcela: float   # ⬅️ NO Optional
