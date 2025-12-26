import pytest
from domain import CalculadoraPagamentos, Recibo

def test_desconto_dinheiro_precisao_float():
    # Testa se o desconto de 10% para pagamento à vista em dinheiro é aplicado corretamente
    valor_compra = 150.50
    esperado = 150.50 * 0.90
    recibo = CalculadoraPagamentos.a_vista_dinheiro(valor_compra)
    assert recibo.total == pytest.approx(esperado) 
    # pytest.approx lida com precisão de float

@pytest.mark.parametrize("parcelas, juros", [
    (2, 1.0),   # 2x sem juros
    (3, 1.20),  # 3x com 20% juros
    (24, 1.20), # Limite máximo (24x)
])

def test_logica_parcelamento_e_limites(parcelas, juros):
    valor = 1000.0
    recibo = CalculadoraPagamentos.parcelado(valor, parcelas)
    assert recibo.total == valor * juros
    assert recibo.parcela == parcelas

def test_calculadora_bloqueia_parcelas_fora_do_intervalo():
    # Testa se a calculadora bloqueia parcelas inválidas
    with pytest.raises(ValueError, match="Número de parcelas inválido"):
        CalculadoraPagamentos.parcelado(100, 1)
    with pytest.raises(ValueError, match="Número de parcelas inválido"):
        CalculadoraPagamentos.parcelado(100, 25)