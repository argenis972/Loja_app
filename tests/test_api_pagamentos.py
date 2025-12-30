# tests/test_api_pagamentos.py
# Teste de integração leve para o endpoint de pagamentos usando TestClient.
from fastapi.testclient import TestClient
from api.main import app
from config.settings import TaxasConfig

def test_api_criar_pagamento_injeta_taxas_no_app_state():
    # Injeta a configuração de taxas diretamente no app.state (sem I/O)
    app.state.taxas_config = TaxasConfig(desconto_vista=10.0, juros_parcelamento=2.0)
    client = TestClient(app)

    payload = {"valor": 100.0, "num_parcelas": 1}
    resp = client.post("/pagamentos/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    # Com desconto 10% -> total 90.0
    assert data["total"] == 90.0
    assert data["valor_parcela"] == 90.0
    assert data["num_parcelas"] == 1