from domain import CalculadoraPagamentos
from ui import exibir_menu_principal, exibir_recibo, validacao_de_dados
from infrastructure import salvar_recibo_em_arquivo_texto


# Fluxo principal de processamento de pagamento
def processar_pagamento():
    # Orquestrador do fluxo principal
    valor , opcao = exibir_menu_principal()

        # Dispatch table
    dispatch = {
        1: lambda v: CalculadoraPagamentos.a_vista_dinheiro(v),
        2: lambda v: CalculadoraPagamentos.a_vista_cartao(v),
        3: lambda v: CalculadoraPagamentos.parcelado(v, 2),
        4: lambda v: CalculadoraPagamentos.parcelado(v, validacao_de_dados("Em quantas parcelas (3/24)? : ", int, 3))
        }
    try:
        acao = dispatch.get(opcao)
        if not acao:
            raise ValueError("Opção de pagamento inválida.")
        resultado_recibo = acao(valor)

        # Exibir e salvar o recibo
        exibir_recibo(resultado_recibo)
        salvar_recibo_em_arquivo_texto(resultado_recibo)

    except Exception as e:
        print(f"Erro ao processar pagamento: {e}")
