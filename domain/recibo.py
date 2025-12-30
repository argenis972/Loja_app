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

        from datetime import datetime
        self.data_hora = datetime.now()

    # Alias
    @property
    def valor_da_parcela(self) -> float:
        return self.valor_parcela
