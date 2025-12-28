from services.pagamento_service import PagamentoService
from domain.recibo import Recibo


class FakeReciboRepository:
    def __init__(self):
        self.salvos = []

    def salvar(self, recibo):
        self.salvos.append(recibo)


def test_pagamento_a_vista_dinheiro():
    repo = FakeReciboRepository()
    service = PagamentoService(repo)

    recibo = service.pagar_a_vista_dinheiro(100)

    assert isinstance(recibo, Recibo)
    assert recibo.total == 90
    assert recibo.metodo == "À vista em dinheiro"
    assert len(repo.salvos) == 1


def test_pagamento_parcelado_com_juros():
    repo = FakeReciboRepository()
    service = PagamentoService(repo)

    recibo = service.pagar_parcelado(100, 5)

    assert recibo.total == 120
    assert recibo.parcelas == 5
    assert "juros" in recibo.informacoes_adicionais.lower()
