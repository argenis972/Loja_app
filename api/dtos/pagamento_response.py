from pydantic import BaseModel


class PagamentoResponse(BaseModel):
    total: float
    metodo: str
    descricao: str
    parcelas: int
    valor_parcela: float
