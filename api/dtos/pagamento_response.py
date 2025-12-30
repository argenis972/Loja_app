from pydantic import BaseModel
from typing import Optional

class PagamentoResponse(BaseModel):
    total: float
    metodo: str
    descricao: str
    parcelas: int          
    valor_parcela: float   