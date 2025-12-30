from typing import Tuple

from .validacoes import pedir_input_numerico, validacao_de_dados


def obter_dados_pagamento() -> Tuple[float, int, int, str]:
    # Encabezado estilizado
    print("\n╔" + "═" * 50 + "╗")
    print(f"║{'SISTEMA DE VENDAS - LOJA ARGENIS':^50}║")
    print("╠" + "═" * 50 + "╣")
    print(f"║ {'[1] À vista em dinheiro (DTO 10%)':<48} ║")
    print(f"║ {'[2] À vista em cartão   (DTO 5%)':<48} ║")
    print(f"║ {'[3] Parcelado até 6x    (SEM JUROS)':<48} ║")
    print(f"║ {'[4] 12x até 24x         (10% ACRÉSCIMO)':<48} ║")
    print("╚" + "═" * 50 + "╝")

    # Input con estilo
    valor = validacao_de_dados("  > Digite o valor total da compra: R$ ", float, 0.01)

    while True:
        opcao = validacao_de_dados("  > Escolha a opção (1-4): ", int, 1)

        if opcao not in (1, 2, 3, 4):
            print("  [!] Opção inválida. Use 1, 2, 3 ou 4.")
            continue

        if opcao == 1:
            metodo = "À vista (Dinheiro)"
            parcelas = 1
            return valor, opcao, parcelas, metodo

        if opcao == 2:
            metodo = "À vista (Cartão)"
            parcelas = 1
            return valor, opcao, parcelas, metodo

        if opcao == 3:
            print("  ┌" + "─" * 20 + "┐")
            parcelas = pedir_input_numerico(
                "  │ Parcelas (2-6): ", tipo=int, minimo=2, maximo=6
            )
            print("  └" + "─" * 20 + "┘")
            metodo = f"Parcelado s/ juros ({parcelas}x)"
            return valor, opcao, parcelas, metodo

        if opcao == 4:
            print("  ┌" + "─" * 20 + "┐")
            parcelas = pedir_input_numerico(
                "  │ Parcelas (12-24):", tipo=int, minimo=12, maximo=24
            )
            print("  └" + "─" * 20 + "┘")
            metodo = f"Parcelado c/ juros ({parcelas}x)"
            return valor, opcao, parcelas, metodo


def exibir_recibo(recibo: dict) -> None:
    # Extraer datos con valores por defecto
    data_hora = recibo.get("data_hora")
    metodo = recibo.get("metodo", "não informado")
    parcelas = recibo.get("parcelas", 1)
    valor_parcela = recibo.get("valor_da_parcela", 0.0)
    total = recibo.get("total", 0.0)
    valor_original = recibo.get("valor_original", 0.0)
    taxas = recibo.get("taxas", "Nenhuma")

    if "5.0%" in taxas:
        taxas_formatadas = "5.0% (com desconto)"
    elif "10.0%" in taxas and "desconto" in taxas.lower():
        taxas_formatadas = "10.0% (com desconto)"
    elif "10.0%" in taxas and "acréscimo" in taxas.lower():
        taxas_formatadas = "10.0% (com acréscimo)"
    else:
        taxas_formatadas = taxas[:27]

    # Formatear fecha
    data_str = (
        data_hora.strftime("%d/%m/%Y %H:%M:%S")
        if hasattr(data_hora, "strftime")
        else str(data_hora)
    )

    print("\n" + "╔" + "═" * 50 + "╗")
    print(f"║{'RESUMO DO PAGAMENTO':^50}║")
    print("╠" + "═" * 50 + "╣")

    # Información General
    print(f"║ Data/Hora:           {data_str:>27} ║")
    print(f"║ Método:              {metodo[:27]:>27} ║")
    print(f"║ Valor Original:      {f'R$ {valor_original:,.2f}':>27} ║")

    print("╟" + "─" * 50 + "╢")

    # Lógica de cuotas (Parcelas)
    if parcelas > 1:
        print(
            f"║ Parcelamento:        {f'{parcelas}x de R$ {valor_parcela:,.2f}':>27} ║"
        )
    else:
        print(f"║ Pagamento:           {'À VISTA':>27} ║")

    # Resumen de Tasas y Total
    print(f"║ Taxas Aplicadas:     {taxas_formatadas:>27} ║")
    print("╠" + "═" * 50 + "╣")
    print(f"║ TOTAL A PAGAR:       {f'R$ {total:,.2f}':>27} ║")
    print("╚" + "═" * 50 + "╝\n")
