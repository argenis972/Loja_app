from domain.recibo import Recibo
from services.recibo_repository import ReciboRepository


class ArquivoReciboRepository(ReciboRepository):

    def __init__(self, caminho: str):
        self.caminho = caminho

    def salvar(self, recibo: Recibo) -> None:
        with open(self.caminho, "a") as f:
            f.write(f"{recibo}\n")
