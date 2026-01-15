import pytest
from fastapi.testclient import TestClient

from api.deps import get_pagamento_service
from api.main import app
from services.pagamento_service import PagamentoService


@pytest.fixture
def client():
    def override_get_pagamento_service():
        # 🔒 SEM repositório → não toca no banco
        return PagamentoService(repo=None)

    app.dependency_overrides[get_pagamento_service] = override_get_pagamento_service

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
