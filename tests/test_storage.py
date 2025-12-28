from infrastructure.storage import ArquivoReciboRepository
from domain.recibo import Recibo

import tempfile
from infrastructure.storage import ArquivoReciboRepository
from domain.recibo import Recibo

def test_salvar_recibo_em_arquivo():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        repo = ArquivoReciboRepository(tmp.name)

        recibo = Recibo(
            total=100,
            metodo="teste"
        )

        repo.salvar(recibo)

        with open(tmp.name) as f:
            conteudo = f.read()

        assert "Recibo" in conteudo
