from typing import Optional
from domain.calculadora import Calculadora


class PagamentoService:
    """
    Serviço de aplicação responsável por orquestrar a criação de pagamentos.
    Recebe as taxas no construtor (injeção de dependência) e instancia a Calculadora do domínio.
    Mantém suporte a um repositório opcional (repo) para compatibilidade com código anterior.
    """

    def __init__(
        self,
        desconto_vista: float,
        juros_parcelamento: float,
        repo: Optional[object] = None,
    ):
        # cria a calculadora do domínio com as taxas recebidas
        self.calculadora = Calculadora(desconto_vista, juros_parcelamento)
        # armazena repo opcional (p.ex. para persistência de pagamentos)
        self.repo = repo

    def criar_pagamento(self, valor: float, num_parcelas: int):
        """
        Retorna o resultado da Calculadora.
        Se houver necessidade, aqui poderíamos persistir usando self.repo.
        """
        resultado = self.calculadora.calcular(valor, num_parcelas)
        # Exemplo: persistir se repo fornecido (interface genérica)
        if self.repo:
            try:
                # supondo um método save no repo; isto é apenas ilustrativo e opcional
                self.repo.save(resultado)
            except Exception:
                # não falhar em caso de ausência de método ou erro de persistência
                pass
        return resultado