from typing import Tuple
from .validacoes import validacao_de_dados, pedir_input_numerico
from datetime import datetime

def exibir_menu_principal() -> Tuple[float, str, int]:
    """
    Exibe menu principal e retorna (valor_total, metodo_str, num_parcelas).
    - Opções:
      1 => À vista em dinheiro (1 parcela)
      2 => À vista em cartão (1 parcela)
      3 => 2x no cartão de crédito (2 parcelas)
      4 => 3x até 24x no cartão de crédito (pede número de parcelas entre 3 e 24)
    """
    print("\n" + "==" * 25 + " LOJA ARGENIS LOPEZ " + "==" * 25)
    valor = validacao_de_dados("\nDigite o valor total da compra: R$ ", float, 0.01)

    print("\nFORMAS DE PAGAMENTO:")
    print("[1] À vista em dinheiro")
    print("[2] À vista em cartão")
    print("[3] 2x no cartão de crédito")
    print("[4] 3x até 24x no cartão de crédito")

    while True:
        opcao = validacao_de_dados("Qual é a opção? : ", int, 1)
        if opcao not in (1, 2, 3, 4):
            print("Opção inválida. Use 1, 2, 3 ou 4.")
            continue

        if opcao == 1:
            metodo = "Dinheiro (à vista)"
            parcelas = 1
        elif opcao == 2:
            metodo = "Cartão (à vista)"
            parcelas = 1
        elif opcao == 3:
            metodo = "Cartão (2x)"
            parcelas = 2
        else:  # opcao == 4
            metodo = "Cartão (parcelado)"
            parcelas = pedir_input_numerico("Quantas parcelas? (3-24): ", tipo=int, minimo=3, maximo=24)

        return valor, metodo, parcelas


def exibir_recibo(recibo: dict) -> None:
    """
    Exibe o recibo formatado no terminal. Recebe um dicionário com as chaves:
    data_hora (datetime), metodo (str), parcelas (int), valor_da_parcela (float), total (float)
    """
    data_hora = recibo.get("data_hora")
    metodo = recibo.get("metodo", "não informado")
    parcelas = recibo.get("parcelas", 1)
    valor_parcela = recibo.get("valor_da_parcela", 0.0)
    total = recibo.get("total", 0.0)
    valor_original = recibo.get("valor_original", 0.0)
    taxas = recibo.get("taxas", {})

    print("\n" + "=" * 55)
    print(f"{'RESUMO DO PAGAMENTO':^55}")
    print("=" * 55)
    if hasattr(data_hora, "strftime"):
        print(f"Data/Hora:                  {data_hora.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"Data/Hora:                  {str(data_hora)}")
    print(f"Método de pagamento:         {metodo}")
    print(f"Valor original:              R$ {valor_original:,.2f}")
    if parcelas and parcelas > 1:
        print(f"Número de parcelas:          {parcelas}")
        print(f"Valor de cada parcela:       R$ {valor_parcela:,.2f}")
    else:
        # à vista
        print(f"Número de parcelas:          1 (à vista)")
        print(f"Valor pago:                  R$ {total:,.2f}")

    if taxas:
        dv = taxas.get("desconto_vista")
        jp = taxas.get("juros_parcelamento")
        print(f"Taxas: desconto_vista={dv}%, juros_parcelamento={jp}%")

    print("-" * 55)
    print(f"Total a pagar:               R$ {total:,.2f}")
    print("=" * 55 + "\n")