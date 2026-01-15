from fastapi import FastAPI

from api.pagamentos_api import router as pagamentos_router

app = FastAPI(title="Loja App - Pagamentos")

app.include_router(pagamentos_router)
