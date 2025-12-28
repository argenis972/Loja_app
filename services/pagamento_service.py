from domain.calculadora import CalculadoraPagamentos
from services.recibo_repository import ReciboRepository
from domain.recibo import Recibo


class PagamentoService:
    def __init__(self, repositorio):
        self.repositorio = repositorio


class PagamentoService:

    def __init__(self, repository: ReciboRepository):
        self.repository = repository

    def pagar_a_vista_dinheiro(self, valor: float, persistir: bool = True) -> Recibo:
        recibo = CalculadoraPagamentos.a_vista_dinheiro(valor)
        if persistir:
            self.repository.salvar(recibo)
        return recibo

    def pagar_a_vista_cartao(self, valor: float, persistir: bool = True) -> Recibo:
        recibo = CalculadoraPagamentos.a_vista_cartao(valor)
        if persistir:
            self.repository.salvar(recibo)
        return recibo

    def pagar_parcelado(self, valor: float, parcelas: int, persistir: bool = True) -> Recibo:
        recibo = CalculadoraPagamentos.parcelado(valor, parcelas)
        if persistir:
            self.repository.salvar(recibo)
        return recibo
