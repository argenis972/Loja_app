import pytest
from domain.calculadora import Calculadora


def test_aplica_desconto_a_vista():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=1, valor=100.0, num_parcelas=1)
    assert resultado["total"] == 90.0
    assert resultado["valor_parcela"] == 90.0
    assert resultado["num_parcelas"] == 1


def test_aplica_desconto_cartao_vista_5pct():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=2, valor=100.0, num_parcelas=1)
    # Aplicar 5% de desconto no cartão à vista -> 95.0
    assert resultado["total"] == 95.0
    assert resultado["valor_parcela"] == 95.0


def test_parcelado_sem_juros_2x():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=3, valor=200.0, num_parcelas=2)
    assert resultado["total"] == 200.0
    assert resultado["valor_parcela"] == 100.0


def test_parcelado_sem_juros_6x():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=3, valor=300.0, num_parcelas=6)
    # Para 6x sem juros, total deve ser igual ao valor original
    assert resultado["total"] == 300.0
    assert resultado["valor_parcela"] == round(300.0 / 6, 2)


def test_parcelado_com_acrescimo_12x():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=4, valor=1000.0, num_parcelas=12)
    # Acréscimo fixo de 10% sobre total: 1000 + 100 = 1100
    assert resultado["total"] == 1100.0
    assert resultado["valor_parcela"] == round(1100.0 / 12, 2)


def test_parcelado_com_acrescimo_24x():
    calc = Calculadora()
    resultado = calc.calcular_por_opcao(opcao=4, valor=240.0, num_parcelas=24)
    # Acréscimo fixo de 10% -> total = 264.0
    assert resultado["total"] == 264.0
    assert resultado["valor_parcela"] == round(264.0 / 24, 2)


def test_opcao_3_parcelas_invalidas_sugestao():
    calc = Calculadora()
    with pytest.raises(ValueError) as exc:
        calc.calcular_por_opcao(opcao=3, valor=100.0, num_parcelas=8)
    assert "Sugestão" in str(exc.value)


def test_opcao_4_parcelas_invalidas_sugestao():
    calc = Calculadora()
    with pytest.raises(ValueError) as exc:
        calc.calcular_por_opcao(opcao=4, valor=100.0, num_parcelas=8)
    assert "Sugestão" in str(exc.value)