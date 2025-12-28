from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Recibo:
    def __init__(
        self,
        total: float,
        metodo: str,
        parcelas: int = 1,
        informacoes_adicionais: str = ""
    ):
        if total <= 0:
            raise ValueError("Total inválido")

        if parcelas < 1:
            raise ValueError("Parcelas inválidas")

        self.total = total
        self.metodo = metodo
        self.parcelas = parcelas
        self.informacoes_adicionais = informacoes_adicionais
        self.valor_parcela = round(self.total / self.parcelas, 2)


