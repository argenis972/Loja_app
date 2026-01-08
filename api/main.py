from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.pagamentos_api import router as pagamentos_router
from config.settings import TaxasConfig, get_settings
from infrastructure.database import create_tables
from services.pagamento_service import PagamentoService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    try:
        create_tables()
    except Exception as exc:
        print(f"Aviso: problema ao criar tabelas no banco: {exc}")

    try:
        taxas = get_settings()
    except FileNotFoundError:
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)
    except Exception as exc:
        # fallback seguro e aviso
        print(f"Aviso: problema ao carregar taxas: {exc}. Usando taxas padrão 0.0.")
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    app.state.taxas_config = taxas
    # Criar um serviço singleton para reuso pelos endpoints (opcional)
    app.state.pagamento_service = PagamentoService(
        taxas.desconto_vista, taxas.juros_parcelamento
    )

    yield


app = FastAPI(title="Loja App - Pagamentos", lifespan=lifespan)


@app.get("/", response_class=JSONResponse)
def health():
    return {"status": "ok"}


app.include_router(pagamentos_router)
