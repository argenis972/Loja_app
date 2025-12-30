import pytest
from domain.calculadora import Calculadora

@pytest.mark.parametrize(
    "opcao, valor, num_parcelas, expected_total, expected_taxa_substr",
    [
        # opção 1: à vista (dinheiro) — desconto fixo 10%
        (1, 100.0, 1, 90.0, "10.0"),
        # opção 2: à vista (cartão) — desconto fixo 5%
        (2, 100.0, 1, 95.0, "5.0"),
        # opção 3: parcelado 2..6 — sem juros
        (3, 100.0, 6, 100.0, "Sem juros"),
        # opção 4: parcelado 12..24 — acréscimo fixo 10%
        (4, 144.0, 12, 158.4, "Acréscimo"),
    ],
)
def test_calcular_por_opcao(opcao, valor, num_parcelas, expected_total, expected_taxa_substr):
    # instanciamos a calculadora com as taxas do arquivo (ou aqui com valores quaisquer,
    # não usadas para regras fixas das opções 1..4)
    calc = Calculadora(desconto_vista=10.0, juros_parcelamento=2.5)

    resultado = calc.calcular_por_opcao(opcao, valor, num_parcelas)

    assert "total" in resultado
    assert "valor_parcela" in resultado
    assert "num_parcelas" in resultado
    assert "taxas" in resultado

    assert resultado["num_parcelas"] == num_parcelas
    assert resultado["total"] == pytest.approx(expected_total, rel=1e-3)
    # valor da parcela arredondado a 2 casas (como a entidade/funcionalidade faz)
    assert resultado["valor_parcela"] == pytest.approx(round(expected_total / num_parcelas, 2), rel=1e-3)
    # verificar que a string de taxas contém a expectativa (não case-sensitive)
    assert expected_taxa_substr.lower() in str(resultado["taxas"]).lower()