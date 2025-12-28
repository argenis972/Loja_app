from fastapi import FastAPI, HTTPException
from infrastructure.storage import ArquivoReciboRepository
from services.pagamento_service import PagamentoService

app = FastAPI()

repo = ArquivoReciboRepository("data/recibos.txt")
service = PagamentoService(repo)


@app.post("/pagamentos/a-vista/dinheiro")
def pagar_a_vista_dinheiro(valor: float):
    try:
        recibo = service.pagar_a_vista_dinheiro(valor)
        return {
            "total": recibo.total,
            "parcelas": recibo.parcelas,
            "metodo": "parcelado",
            "descricao": recibo.metodo
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
