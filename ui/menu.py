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
    print("\n" + "=="*24, "RECIBO DE PAGAMENTO", "=="*24)
    print(f"Total a pagar: R$ {recibo.total:.2f}")
    print(f"Método de pagamento: {recibo.metodo}")
    
    if recibo.parcela > 1:
        print(f"Número de parcelas: {recibo.parcela}")
        print(f"Valor de cada parcela: {recibo.valor_da_parcela:.2f} R$")
    
    if recibo.informacoes_adicionais:
        print(f"Informações adicionais: {recibo.informacoes_adicionais}\n")