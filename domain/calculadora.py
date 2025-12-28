from .recibo import Recibo

class CalculadoraPagamentos:

    @staticmethod
    def a_vista_dinheiro(valor: float) -> Recibo:
        total = round(valor * 0.9, 2)


        return Recibo(

            total=total,
            metodo="À vista em dinheiro",
            parcelas=1,
            informacoes_adicionais="Desconto de 10%"
        )

  
    @staticmethod
    def parcelado(valor: float, parcelas: int) -> Recibo:
        if parcelas < 2 or parcelas > 24:
            raise ValueError("Número de parcelas inválido")

        # 2x sem juros
        if parcelas == 2:
            total = valor
        else:
            total = round(valor * 1.20, 2)

        return Recibo(
            total=total,
            metodo="parcelado",
            parcelas=parcelas,
            informacoes_adicionais="20% de juros" if parcelas > 2 else "Sem juros"
        )


