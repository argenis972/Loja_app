from .validacoes import validacao_de_dados
from domain import Recibo

# Prints e inputs do menu

def exibir_menu_principal():
    # Exibir o menu e obter a escolha do usuário
    print("\n" + "=="*25, "LOJA ARGENIS LOPEZ", "=="*25)

    valor = validacao_de_dados("\nDigite o valor total da compra: R$ ", float, 0.01)
    print("\nFORMAS DE PAGAMENTO:")
    print("[1] À vista em dinheiro ")
    print("[2] À vista em cartão ")
    print("[3] 2x no cartão de crédito ")
    print("[4] 3x até 24x no cartão de crédito ")
    while True:
        opcao = validacao_de_dados("Qual é a opção? : ", int, 1)
        if 1 <= opcao <= 4:
            return valor, opcao
        else:
            print("Opção inválida. Tente com números de 1 a 4.")

def exibir_recibo(recibo: Recibo):
    # Exibir o recibo na tela
    print(f"\n" + "="*55)
    print(f"{'RESUMO DO PAGAMENTO':^55}")
    print(f"="*55)
    print(f"Data/Hora:                  " f"{recibo.data_hora.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Método de pagamento:          {recibo.metodo:>8}")
    if recibo.parcelas > 1:
        print(f"Número de parcelas:           {recibo.parcelas:>8}")
        print(f"Valor de cada parcela:          {recibo.valor_da_parcela:>8.2f} R$")
    
    if recibo.informacoes_adicionais:
        print(f"Informações adicionales:        {recibo.informacoes_adicionais:8}")
    print("-"*55)
    print(f"Total a pagar:                    R${recibo.total:8.2f}\n")
    print(f"="*55)