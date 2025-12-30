import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.mark.parametrize(
    "payload, expected_total, expected_num_parcelas, expected_taxa_substr",
    [
        ({"opcao": 1, "valor": 100.0, "num_parcelas": 1}, 90.0, 1, "10.0"),
        ({"opcao": 2, "valor": 100.0, "num_parcelas": 1}, 95.0, 1, "5.0"),
        ({"opcao": 3, "valor": 100.0, "num_parcelas": 6}, 100.0, 6, "sem juros"),
        ({"opcao": 4, "valor": 144.0, "num_parcelas": 12}, 158.4, 12, "acréscimo"),
    ],
)
def test_api_pagamentos_por_opcao(
    payload, expected_total, expected_num_parcelas, expected_taxa_substr
):
    with TestClient(app) as client:
        resp = client.post("/pagamentos/", json=payload)
        assert resp.status_code == 200, resp.text

        data = resp.json()
        # chaves essenciais
        assert "total" in data
        assert "valor_parcela" in data
        assert "num_parcelas" in data
        assert "taxas" in data

        assert data["num_parcelas"] == expected_num_parcelas
        assert data["total"] == pytest.approx(expected_total, rel=1e-3)
        assert data["valor_parcela"] == pytest.approx(
            round(expected_total / expected_num_parcelas, 2), rel=1e-3
        )

        assert expected_taxa_substr.lower() in str(data["taxas"]).lower()

        # se o endpoint incluir "opcao" no retorno, validar coerência (não obrigatório)
        if "opcao" in data:
            assert data["opcao"] == payload["opcao"]
