import pytest
from domain import Recibo

@pytest.mark.parametrize("total, parcela", [
    (-10.0, 1),
    (100.0, 0),
])
def test_recibo_validacoes_obrigatorias(total, parcela):
    with pytest.raises(ValueError):
        Recibo(total=total, metodo="Teste", parcela=parcela)


def test_recibo_calcula_valor_da_parcela_corretamente():
    recibo = Recibo(total=100.0, metodo="Pix", parcela=2)

    assert recibo.valor_da_parcela == 50.0
