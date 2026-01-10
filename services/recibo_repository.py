from abc import ABC, abstractmethod
from typing import Any

from domain.recibo import Recibo


class ReciboRepository(ABC):
    @abstractmethod
    def salvar(self, recibo: Recibo) -> None:
        """Persiste um recibo no storage."""

    def save(self, recibo: Recibo) -> None:
        """Alias compatível com implementações que usam inglês."""
        self.salvar(recibo)

    @abstractmethod
    def listar_todos(self) -> list[Any]:
        """Retorna todos os recibos persistidos em ordem adequada."""
