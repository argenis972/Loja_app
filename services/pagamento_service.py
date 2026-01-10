from __future__ import annotations

from typing import Any, Optional

from domain.calculadora import Calculadora


class PagamentoService:
    def __init__(
        self,
        desconto_vista: float,
        juros_parcelamento: float,
        repo: Optional[object] = None,
    ) -> None:
        # cria a calculadora do domínio com as taxas recebidas
        self.calculadora = Calculadora(desconto_vista, juros_parcelamento)
        # armazena repo opcional (p.ex. para persistência de pagamentos)
        self.repo = repo

    def listar_recibos(self) -> list[Any]:
        """
        Lista todos os recibos/pagamentos persistidos.

        Retorna uma lista. Se não houver repositório configurado, retorna lista vazia
        (mantém compatibilidade com cenários sem persistência).
        """
        if not self.repo:
            return []

        if hasattr(self.repo, "listar_todos"):
            return self.repo.listar_todos()
        if hasattr(self.repo, "list_all"):
            return self.repo.list_all()
        return []

    def criar_pagamento(self, valor: float, num_parcelas: int):
        resultado = self.calculadora.calcular(valor, num_parcelas)
        if self.repo:
            try:
                self.repo.save(resultado)
            except Exception:
                pass
        return resultado

    def criar_pagamento_por_opcao(self, opcao: int, valor: float, num_parcelas: int):
        resultado = self.calculadora.calcular_por_opcao(opcao, valor, num_parcelas)
        if self.repo:
            try:
                self.repo.save(resultado)
            except Exception:
                pass
        return resultado
