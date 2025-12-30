from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, Field

from config.settings import TaxasConfig
from services.pagamento_service import PagamentoService

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])


class PagamentoRequest(BaseModel):
    opcao: int = Field(..., ge=1, le=4, description="Opção do menu (1..4)")
    valor: float = Field(..., gt=0, description="Valor total do pagamento")
    num_parcelas: int = Field(..., ge=1, description="Número de parcelas")


def get_taxas(request: Request) -> TaxasConfig:
    taxas = getattr(request.app.state, "taxas_config", None)
    if taxas is None:
        raise HTTPException(
            status_code=500, detail="Configuração de taxas não carregada."
        )
    return taxas


@router.post("/", response_model=dict)
def criar_pagamento(
    req: PagamentoRequest, request: Request, taxas: TaxasConfig = Depends(get_taxas)
):
    """
    Usa o serviço singleton criado em app.state (se disponível) para garantir coerência com o startup.
    Chama criar_pagamento_por_opcao para aplicar exatamente as mesmas regras do domínio/CLI.
    """
    service: PagamentoService = getattr(request.app.state, "pagamento_service", None)
    if service is None:
        service = PagamentoService(taxas.desconto_vista, taxas.juros_parcelamento)

    resultado = service.criar_pagamento_por_opcao(
        req.opcao, req.valor, req.num_parcelas
    )
    return resultado
