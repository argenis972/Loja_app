from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.pagamentos_api import router as pagamentos_router

app = FastAPI(title="Loja App - Pagamentos")


@app.get("/", response_class=JSONResponse)
def health():
    return {"status": "ok"}


app.include_router(pagamentos_router)
