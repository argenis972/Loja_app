from pydantic import BaseModel


class PagamentoResponse(BaseModel):
    total: float
    metodo: str
    descricao: str
    parcelas: int | None = None
    valor_parcela: float | None = None
