from infrastructure.postgres_repository import PostgresPagamentoRepository
from services.pagamento_service import PagamentoService


def main() -> None:
    repo = PostgresPagamentoRepository()

    # Taxas explícitas (obrigatório)
    desconto_vista = 0.0
    juros_parcelamento = 0.0

    service = PagamentoService(
        desconto_vista=desconto_vista,
        juros_parcelamento=juros_parcelamento,
        repo=repo,
    )

    valor = float(input("Digite o valor da compra: "))
    parcelas = int(input("Digite o número de parcelas: "))

    resultado = service.criar_pagamento(valor, parcelas)

    print("\nResultado:")
    for k, v in resultado.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
