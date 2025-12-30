from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel

from config.settings import TaxasConfig
from services.pagamento_service import PagamentoService

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])


class PagamentoRequest(BaseModel):
    valor: float
    num_parcelas: int


def get_taxas(request: Request) -> TaxasConfig:
    """
    Dependency que obtém as taxas carregadas no startup através de request.app.state.
    Evita importar diretamente o módulo de settings aqui (a leitura já foi feita no startup).
    """
    taxas = getattr(request.app.state, "taxas_config", None)
    if taxas is None:
        raise HTTPException(status_code=500, detail="Configuração de taxas não carregada.")
    return taxas


@router.post("/", response_model=dict)
def criar_pagamento(req: PagamentoRequest, taxas: TaxasConfig = Depends(get_taxas)):
    # Injetamos as taxas no serviço; o serviço instancia a Calculadora de domínio.
    service = PagamentoService(taxas.desconto_vista, taxas.juros_parcelamento)
    resultado = service.criar_pagamento(req.valor, req.num_parcelas)
    return resultado
