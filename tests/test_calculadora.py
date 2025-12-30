import pytest

from domain.calculadora import Calculadora


def test_aplica_desconto_a_vista():
    calc = Calculadora(desconto_vista=10.0, juros_parcelamento=2.0)
    resultado = calc.calcular(valor=100.0, num_parcelas=1)
    assert resultado["total"] == 90.0
    assert resultado["valor_parcela"] == 90.0
    assert resultado["num_parcelas"] == 1


def test_aplica_juros_parcelado():
    calc = Calculadora(desconto_vista=5.0, juros_parcelamento=2.0)
    resultado = calc.calcular(valor=100.0, num_parcelas=2)
    # juros simples: 2% por parcela -> total raw = 100 * (1 + 0.02*2) = 104.0
    assert resultado["total"] == 104.0
    assert resultado["valor_parcela"] == 52.0
    assert resultado["num_parcelas"] == 2


def test_erros_de_tipo_nas_taxas():
    with pytest.raises(TypeError):
        Calculadora(desconto_vista="10", juros_parcelamento=2.0)
    with pytest.raises(TypeError):
        Calculadora(desconto_vista=10.0, juros_parcelamento="2")


def test_valores_invalidos_levantam_excecao():
    calc = Calculadora(desconto_vista=10.0, juros_parcelamento=2.0)
    with pytest.raises(TypeError):
        calc.calcular(valor="100", num_parcelas=1)
    with pytest.raises(ValueError):
        calc.calcular(valor=100.0, num_parcelas=0)