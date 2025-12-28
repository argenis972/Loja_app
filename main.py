from services.pagamento_service import PagamentoService
from infrastructure.storage import ArquivoReciboRepository
from ui import exibir_menu_principal, exibir_recibo, pedir_input_numerico

def main():
    repo = ArquivoReciboRepository("data/recibos.txt")
    service = PagamentoService(repo)

    valor_compra, opcao = exibir_menu_principal()

    try:
        if opcao == 1:
            recibo = service.pagar_a_vista_dinheiro(valor_compra, persistir=False)

        elif opcao == 2:
            recibo = service.pagar_a_vista_cartao(valor_compra, persistir=False)

        elif opcao == 3:
            recibo = service.pagar_parcelado(valor_compra, 2, persistir=False)

        elif opcao == 4:
            parcelas = pedir_input_numerico("Em quantas parcelas (3/24)? : ", int, 3, 24)
            recibo = service.pagar_parcelado(valor_compra, parcelas, persistir=False)

        else:
            raise ValueError("Opção inválida")

        exibir_recibo(recibo)

        confirmar = input("Confirmar processamento? (S/N): ").strip().upper()
        if confirmar == "S":
            repo.salvar(recibo)
            print("[SISTEMA] Venda finalizada e registrada!")
        else:
            print("[SISTEMA] Operação cancelada.")

    except Exception as e:
        print(f"[ERRO]: {e}")


if __name__ == "__main__":
    main()
