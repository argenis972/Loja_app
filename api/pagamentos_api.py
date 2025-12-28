from fastapi import FastAPI, HTTPException
from api.dtos.pagamento_request import (
    PagamentoDinheiroRequest,
    PagamentoParceladoRequest,
)
from api.dtos.pagamento_response import PagamentoResponse
from services.pagamento_service import PagamentoService
from infrastructure.storage import ArquivoReciboRepository

app = FastAPI()

repo = ArquivoReciboRepository("data/recibos.txt")
service = PagamentoService(repo)


@app.post("/pagamentos/a-vista/dinheiro", response_model=PagamentoResponse)
def pagamento_a_vista_dinheiro(request: PagamentoDinheiroRequest):
    try:
        recibo = service.pagar_a_vista_dinheiro(request.valor)

        return PagamentoResponse(
            total=recibo.total,
            metodo="a_vista_dinheiro",
            descricao=recibo.informacoes_adicionais,
            parcelas=recibo.parcelas,
            valor_parcela=recibo.valor_parcela
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/pagamentos/parcelado", response_model=PagamentoResponse)
def pagamento_parcelado(request: PagamentoParceladoRequest):
    try:
        recibo = service.pagar_parcelado(
            request.valor,
            request.parcelas
        )

        return PagamentoResponse(
            total=recibo.total,
            metodo="parcelado",
            descricao=f"Cartão de crédito em {recibo.parcelas}x",
            parcelas=recibo.parcelas,
            valor_parcela=recibo.valor_parcela
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
