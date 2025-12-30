from typing import Any, Dict


class Calculadora:

    DESCONTO_VISTA_FIXO = 10.0
    DESCONTO_CARTAO_FIXO = 5.0
    ACRESCIMO_10_PERCENT = 10.0

    def __init__(self, desconto_vista: float = 0.0, juros_parcelamento: float = 0.0):
        if not isinstance(desconto_vista, (int, float)):
            raise TypeError("desconto_vista deve ser numérico (int ou float).")
        if not isinstance(juros_parcelamento, (int, float)):
            raise TypeError("juros_parcelamento deve ser numérico (int ou float).")
        self.desconto_vista = float(desconto_vista)
        self.juros_parcelamento = float(juros_parcelamento)

    def calcular(self, valor: float, num_parcelas: int) -> Dict[str, Any]:
        """
        Comportamento genérico (usa as taxas injetadas).
        total é calculado a partir do raw_total e arredondado para 2 casas.
        valor_parcela é total / num_parcelas arredondado para 2 casas.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("valor deve ser numérico.")
        if not isinstance(num_parcelas, int):
            raise TypeError("num_parcelas deve ser inteiro.")
        if valor < 0:
            raise ValueError("valor não pode ser negativo.")
        if num_parcelas < 1:
            raise ValueError("num_parcelas deve ser >= 1.")

        if num_parcelas == 1:
            raw_total = float(valor) * (1 - (self.desconto_vista / 100.0))
        else:
            raw_total = float(valor) * (
                1 + (self.juros_parcelamento / 100.0) * num_parcelas
            )
        total = round(raw_total, 2)
        valor_parcela = round(total / num_parcelas, 2)

        return {
            "total": total,
            "valor_parcela": valor_parcela,
            "num_parcelas": num_parcelas,
        }

    def calcular_por_opcao(
        self, opcao: int, valor: float, num_parcelas: int
    ) -> Dict[str, Any]:
        """
        Regras fixas por opção do menu.
        Retorna dicionário com: total, valor_parcela, num_parcelas, taxas, opcao
        """
        # Validações básicas
        if not isinstance(opcao, int):
            raise TypeError("opcao deve ser um inteiro.")
        if not isinstance(valor, (int, float)):
            raise TypeError("valor deve ser numérico.")
        if not isinstance(num_parcelas, int):
            raise TypeError("num_parcelas deve ser inteiro.")
        if valor < 0:
            raise ValueError("valor não pode ser negativo.")
        if num_parcelas < 1:
            raise ValueError("num_parcelas deve ser >= 1.")

        if opcao == 1:
            # À vista em dinheiro: desconto fixo de 10%
            if num_parcelas != 1:
                raise ValueError(
                    "Opção 1 (à vista em dinheiro) aceita apenas 1 parcela."
                )
            raw_total = float(valor) * (1 - (self.DESCONTO_VISTA_FIXO / 100.0))
            taxas = f"{self.DESCONTO_VISTA_FIXO}% (Desconto à vista)"
        elif opcao == 2:
            # À vista em cartão: desconto fixo de 5%
            if num_parcelas != 1:
                raise ValueError("Opção 2 (à vista em cartão) aceita apenas 1 parcela.")
            raw_total = float(valor) * (1 - (self.DESCONTO_CARTAO_FIXO / 100.0))
            taxas = f"{self.DESCONTO_CARTAO_FIXO}% (Desconto cartão à vista)"
        elif opcao == 3:
            # Parcelado 2..6 sem juros
            if not (2 <= num_parcelas <= 6):
                sugerido = 2 if num_parcelas < 2 else 6
                raise ValueError(
                    "Opção 3 suporta de 2 a 6 parcelas. "
                    f"Sugestão: use {sugerido} parcela(s)."
                )
            raw_total = float(valor)
            taxas = "0% (Sem juros)"
        elif opcao == 4:
            # Parcelado 12..24 com acréscimo fixo total de 10%
            if not (12 <= num_parcelas <= 24):
                sugerido = 12 if num_parcelas < 12 else 24

                raise ValueError(
                    "Opção 4 suporta de 12 a 24 parcelas."
                    f"Sugestão: use {sugerido} parcela(s)."
                )

            raw_total = float(valor) * (1 + (self.ACRESCIMO_10_PERCENT / 100.0))
            taxas = f"{self.ACRESCIMO_10_PERCENT}% (Acréscimo fixo)"
        else:
            raise ValueError("Opção inválida. Escolha um valor entre 1 e 4.")

        total = round(raw_total, 2)
        valor_parcela = round(total / num_parcelas, 2)

        return {
            "total": total,
            "valor_parcela": valor_parcela,
            "num_parcelas": num_parcelas,
            "taxas": taxas,
            "opcao": opcao,
        }


# Alias retrocompatível
class CalculadoraPagamentos(Calculadora):
    pass


__all__ = ["Calculadora", "CalculadoraPagamentos"]
