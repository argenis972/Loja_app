from dotenv import load_dotenv

load_dotenv()

import os

import infrastructure.database as db
from config.settings import TaxasConfig, get_settings
from infrastructure.storage import PostgresReciboRepository
from services.pagamento_service import PagamentoService
from ui.menu import exibir_recibo, obter_dados_pagamento


def main() -> None:
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError(
            "DATABASE_URL não configurada. Exemplo: "
            "postgresql+psycopg://loja_user:SENHA@localhost:5432/loja_db"
        )

    db.init_db()
    session = db.SessionLocal()

    try:
        taxas_conf = get_settings()
    except Exception:
        taxas_conf = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    try:
        repo = PostgresReciboRepository(session)
        service = PagamentoService(
            taxas_conf.desconto_vista,
            taxas_conf.juros_parcelamento,
            repo,
        )

        valor, opcao, num_parcelas, metodo = obter_dados_pagamento()
        resultado = service.criar_pagamento_por_opcao(opcao, valor, num_parcelas)

        from datetime import datetime

        recibo_view = {
            "data_hora": datetime.now(),
            "metodo": metodo,
            "valor_original": valor,
            "parcelas": resultado.get("num_parcelas"),
            "valor_da_parcela": resultado.get("valor_parcela"),
            "total": resultado.get("total"),
            "taxas": resultado.get("taxas"),
        }
        exibir_recibo(recibo_view)

        print("Recibo persistido no Postgres com sucesso.")

    finally:
        session.close()


if __name__ == "__main__":
    main()
