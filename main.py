from services.pagamento_service import PagamentoService # IMPORTANTE: Verifique o caminho
from infrastructure.storage import Storage
from ui import exibir_menu_principal, exibir_recibo, pedir_input_numerico

def main():
    # 1. Configuração
    repo_real = Storage("data/recibos.txt")
    service = PagamentoService(repositorio=repo_real)

    # 2. Entrada de Dados
    valor_compra, opcao = exibir_menu_principal()
    
    qtd_parcelas = 1
    if opcao == 4:
        qtd_parcelas = pedir_input_numerico("Em quantas parcelas (3/24)? : ", int, 3, 24)
    elif opcao == 3:
        qtd_parcelas = 2

    try:
        # 3. Cálculo da Prévia (Regras de Negócio aplicadas)
        recibo_previa = service.calcular_previa(valor_compra, opcao, qtd_parcelas)

        # 4. Resumo para Confirmação 
        print(f"\n" + "="*40)
        print(f"{'CONFIRMAÇÕA DO PAGAMENTO':^40}")
        print(f"="*40)
        print(f"Valor Original:       R${valor_compra:>10.2f}")
        print(f"Método:               {recibo_previa.metodo}")
        
        if recibo_previa.parcela > 1:
            print(f"Parcelamento:        {recibo_previa.parcela}x de R$ {recibo_previa.valor_da_parcela:.2f}")
        
        print(f"-"*40)
        print(f"TOTAL A PAGAR:        R$ {recibo_previa.total:>10.2f}")
        print(f"="*40)
        
        confirmar = input("Confirmar processamento? (S/N): ").strip().upper()

        if confirmar == 'S':
            service.finalizar_venda(recibo_previa)
            print("\n" + "*"*40)
            exibir_recibo(recibo_previa)
            print("[SISTEMA] Venda finalizada e registrada!")
        else:
            print("\n[SISTEMA] Operação cancelada pelo usuário.")

    except Exception as e:
        print(f"\n[ERRO CRÍTICO]: {e}")

if __name__ == "__main__":
    main()