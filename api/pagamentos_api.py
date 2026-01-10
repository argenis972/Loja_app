from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from api.deps import get_pagamento_service
from api.dtos.recibo_response import ReciboResponse
from services.pagamento_service import PagamentoService

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])


@router.get("/", response_model=list[ReciboResponse])
def listar_pagamentos(service: PagamentoService = Depends(get_pagamento_service)):
    return service.listar_recibos()


class PagamentoRequest(BaseModel):
    opcao: int = Field(..., ge=1, le=4)
    valor: float = Field(..., gt=0)
    num_parcelas: int = Field(..., ge=1)


@router.post("/", response_model=dict)
def criar_pagamento(
    req: PagamentoRequest,
    service: PagamentoService = Depends(get_pagamento_service),
):
    return service.criar_pagamento_por_opcao(req.opcao, req.valor, req.num_parcelas)
