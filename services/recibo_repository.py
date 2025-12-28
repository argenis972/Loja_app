from abc import ABC, abstractmethod
from domain.recibo import Recibo


class ReciboRepository(ABC):

    @abstractmethod
    def salvar(self, recibo: Recibo) -> None:
        pass
