from typing import Dict


class Calculadora:
    """
    Classe de domínio que realiza os cálculos de pagamento.

    Recebe as taxas no construtor e NÃO realiza I/O nem importa config.
    """

    def __init__(self, desconto_vista: float, juros_parcelamento: float):
        # validação de tipos (protege contra erros de configuração vindos de infra)
        if not isinstance(desconto_vista, (int, float)):
            raise TypeError("desconto_vista deve ser numérico (int ou float).")
        if not isinstance(juros_parcelamento, (int, float)):
            raise TypeError("juros_parcelamento deve ser numérico (int ou float).")
        desconto_vista = float(desconto_vista)
        juros_parcelamento = float(juros_parcelamento)
        if desconto_vista < 0 or juros_parcelamento < 0:
            raise ValueError("As taxas não podem ser negativas.")

        self.desconto_vista = desconto_vista
        self.juros_parcelamento = juros_parcelamento

    def calcular(self, valor: float, num_parcelas: int) -> Dict[str, float]:
        """
        Calcula e retorna um dicionário com:
          - total: total a pagar (float)
          - valor_parcela: valor de cada parcela (float)
          - num_parcelas: int
        Regras:
          - se num_parcelas == 1: aplica desconto_vista (%) sobre o valor.
          - se num_parcelas > 1: aplica juros simples (juros_parcelamento (%) por parcela) sobre o valor.
        Para garantir total = valor_parcela * num_parcelas, arredondamos o valor_parcela para 2 decimais
        e recalculamos o total como valor_parcela * num_parcelas.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("valor deve ser numérico.")
        if not isinstance(num_parcelas, int):
            raise TypeError("num_parcelas deve ser um inteiro.")
        if valor < 0:
            raise ValueError("valor não pode ser negativo.")
        if num_parcelas < 1:
            raise ValueError("num_parcelas deve ser >= 1.")

        if num_parcelas == 1:
            raw_total = valor * (1 - (self.desconto_vista / 100.0))
        else:
            # juros simples por parcela: juros_parcelamento (%) multiplicado pelo número de parcelas
            raw_total = valor * (1 + (self.juros_parcelamento / 100.0) * num_parcelas)

        valor_parcela = round(raw_total / num_parcelas, 2)
        total = round(valor_parcela * num_parcelas, 2)

        return {
            "total": total,
            "valor_parcela": valor_parcela,
            "num_parcelas": num_parcelas,
        }


# Alias para compatibilidade retroativa com código/tests que importam CalculadoraPagamentos
class CalculadoraPagamentos(Calculadora):
    """Classe compatível com o nome antigo; herda toda a funcionalidade de Calculadora."""
    pass


__all__ = ["Calculadora", "CalculadoraPagamentos"]