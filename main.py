import os

from config.settings import TaxasConfig, get_settings
from infrastructure.database import SessionLocal
from infrastructure.storage import PostgresReciboRepository
from services.pagamento_service import PagamentoService
from ui.menu import exibir_recibo, obter_dados_pagamento


def main() -> None:
    """
    CLI persistindo no Postgres.

    Requer:
    - DATABASE_URL configurada (ex: postgresql+psycopg://...)
    - Postgres acessível
    - Migrações já aplicadas (alembic upgrade head)
    """
    # Carregar configuraç��o
    try:
        taxas_conf: TaxasConfig = get_settings()
    except Exception:
        taxas_conf = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    if not os.getenv("DATABASE_URL"):
        raise RuntimeError(
            "DATABASE_URL não configurada. Exemplo: "
            "postgresql+psycopg://loja_user:SENHA@localhost:5432/loja_db"
        )

    db = SessionLocal()
    try:
        repo = PostgresReciboRepository(db)
        service = PagamentoService(
            taxas_conf.desconto_vista,
            taxas_conf.juros_parcelamento,
            repo,
        )

        valor, opcao, num_parcelas, metodo = obter_dados_pagamento()

        # Este método agora persiste no Postgres (via repo.salvar)
        resultado = service.criar_pagamento_por_opcao(opcao, valor, num_parcelas)

        # Exibir no console (UI usa dict)
        recibo_view = {
            "metodo": metodo,
            "parcelas": resultado.get("num_parcelas"),
            "valor_da_parcela": resultado.get("valor_parcela"),
            "total": resultado.get("total"),
            "taxas": resultado.get("taxas"),
        }
        exibir_recibo(recibo_view)

        print("Recibo persistido no Postgres com sucesso.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
