from fastapi.testclient import TestClient
from main_api import app

client = TestClient(app)


# ===============================
# PAGAMENTO À VISTA - DINHEIRO
# ===============================

def test_pagamento_a_vista_dinheiro_sucesso():
    response = client.post(
        "/pagamentos/a-vista/dinheiro",
        json={"valor": 100}
    )

    assert response.status_code == 200

    body = response.json()

    # domínio manda: 10% de desconto
    assert body["total"] == 90.0
    assert body["metodo"] == "a_vista_dinheiro"
    assert body["descricao"] == "Desconto de 10%"
    assert body["parcelas"] == 1


def test_pagamento_a_vista_dinheiro_valor_invalido():
    response = client.post(
        "/pagamentos/a-vista/dinheiro",
        json={
        "total": 90.0,
        "metodo": "a_vista_dinheiro",
        "descricao": "À vista em dinheiro",
        "parcelas": 1
        }
    )

    # erro de validação (Pydantic)
    assert response.status_code == 422


def test_pagamento_parcelado_sucesso():
    response = client.post(
        "/pagamentos/parcelado",
        json={
            "valor": 100,
            "parcelas": 5
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["total"] > 100
    assert body["parcelas"] == 5
    assert body["metodo"] == "parcelado"
    assert body["descricao"] == "Cartão de crédito em 5x"



def test_pagamento_parcelado_parcelas_invalidas():
    response = client.post(
        "/pagamentos/parcelado",
        json={
            "valor": 100,
            "parcelas": 0
        }
    )

    # validação de entrada
    assert response.status_code == 422
