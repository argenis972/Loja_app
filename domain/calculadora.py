from .recibo import Recibo

class CalculadoraPagamentos:

    @staticmethod
    def a_vista_dinheiro(valor: float) -> Recibo:
        total = valor * 0.90
        return Recibo(
            total=total,
            metodo="À vista em dinheiro",
            informacoes_adicionais="Desconto de 10%"
        )

    @staticmethod
    def a_vista_cartao(valor: float) -> Recibo:
        total = valor * 0.95
        return Recibo(
            total=total,
            metodo="À vista em cartão",
            informacoes_adicionais="Desconto de 5%"
        )

    @staticmethod
    def parcelado(valor: float, parcela: int) -> Recibo:
        if parcela == 2:
            return Recibo(
                total=valor,
                metodo="Cartão de crédito em 2x",
                parcela=2,
                informacoes_adicionais="Sem juros"
            )

        if 3 <= parcela <= 24:
            total = valor * 1.20
            return Recibo(
                total=total,
                metodo=f"Cartão de crédito em {parcela}x",
                parcela=parcela,
                informacoes_adicionais="20% de juros"
            )

        raise ValueError("Número de parcelas inválido.")


