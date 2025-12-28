from domain.calculadora import CalculadoraPagamentos

class PagamentoService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def calcular_previa(self, valor, opcao, parcelas=0):
        # Dispatch table segura
        metodos = {
            1: lambda v: CalculadoraPagamentos.a_vista_dinheiro(v),
            2: lambda v: CalculadoraPagamentos.a_vista_cartao(v),
            3: lambda v: CalculadoraPagamentos.parcelado(v, 2),
            4: lambda v: CalculadoraPagamentos.parcelado(v, parcelas)
        }
        
        acao = metodos.get(opcao)
        if not acao:
            raise ValueError(f"Opção de pagamento {opcao} é inválida.")
            
        return acao(valor) # Retorna o objeto Recibo (com o campo .total atualizado)

    def finalizar_venda(self, recibo):
        self.repositorio.salvar(recibo)