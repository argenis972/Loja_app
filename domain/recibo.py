from dataclasses import dataclass
from typing import List

@dataclass
class Recibo:
    total: float
    metodo: str
    parcela: int = 1
    informacoes_adicionais: str = ""

    def __post_init__(self):
        if self.total <= 0:
            raise ValueError("Total do recibo deve ser maior que zero")

        if self.parcela < 1:
            raise ValueError("Parcela deve ser no mínimo 1")

    @property
    def valor_da_parcela(self) -> float:
        return round(self.total / self.parcela, 2)

