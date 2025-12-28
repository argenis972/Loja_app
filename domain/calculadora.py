from .recibo import Recibo

class CalculadoraPagamentos:

    @staticmethod
    def a_vista_dinheiro(valor: float) -> Recibo:
        total = valor * 0.9
        return Recibo(
            total=total,
            metodo="a_vista_dinheiro",
            parcelas=1,
            informacoes_adicionais="À vista em dinheiro"
        )
        
    @staticmethod
    def parcelado(valor: float, parcelas: int) -> Recibo:
        if parcelas == 2:
            return Recibo(
                total=valor,
                metodo="parcelado",
                parcelas=2,
                informacoes_adicionais="Sem juros"
            )

        if 3 <= parcelas <= 24:
            total = valor * 1.20
            return Recibo(
                total=total,
                metodo="parcelado",
                parcelas=parcelas,
                informacoes_adicionais="20% de juros"
            )

        raise ValueError("Número de parcelas inválido")

