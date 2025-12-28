from pydantic import BaseModel, Field


class PagamentoDinheiroRequest(BaseModel):
    valor: float = Field(..., gt=0, description="Valor do pagamento em dinheiro")


class PagamentoParceladoRequest(BaseModel):
    valor: float = Field(..., gt=0, description="Valor total do pagamento")
    parcelas: int = Field(..., ge=1, le=12, description="Número de parcelas")
