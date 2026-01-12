from __future__ import annotations

from typing import Any, Optional

from domain.calculadora import Calculadora
from domain.recibo import Recibo


class PagamentoService:
    def __init__(
        self,
        desconto_vista: float,
        juros_parcelamento: float,
        repo: Optional[object] = None,
    ) -> None:
        self.calculadora = Calculadora(desconto_vista, juros_parcelamento)
        self.repo = repo

    def listar_recibos(self) -> list[Any]:
        if not self.repo:
            return []

        if hasattr(self.repo, "listar_todos"):
            return self.repo.listar_todos()
        if hasattr(self.repo, "list_all"):
            return self.repo.list_all()
        return []

    def _persistir(self, recibo: Recibo) -> None:
        if not self.repo:
            return

        if hasattr(self.repo, "salvar"):
            self.repo.salvar(recibo)
            return

        # Compatibilidade caso exista "save"
        if hasattr(self.repo, "save"):
            self.repo.save(recibo)  # type: ignore[attr-defined]
            return

        raise RuntimeError("Repositório não possui método salvar/save.")

    def criar_pagamento(self, valor: float, num_parcelas: int) -> dict:
        """
        Mantido por compatibilidade com testes/código legado.
        Trata como pagamento parcelado simples (opção 3 por padrão).
        """
        # Usa a lógica existente do domínio para manter consistência
        resultado = self.calculadora.calcular(valor, num_parcelas)

        recibo = Recibo(
            total=float(resultado["total"]),
            metodo="Pagamento",
            parcelas=int(resultado.get("num_parcelas", num_parcelas)),
            informacoes_adicionais=str(resultado.get("taxas", "")),
        )
        self._persistir(recibo)
        return resultado

    def criar_pagamento_por_opcao(
        self, opcao: int, valor: float, num_parcelas: int
    ) -> dict:
        resultado = self.calculadora.calcular_por_opcao(opcao, valor, num_parcelas)

        metodo_por_opcao = {
            1: "À vista (Dinheiro)",
            2: "À vista (Cartão)",
            3: "Parcelado s/ juros",
            4: "Parcelado c/ juros",
        }
        metodo = metodo_por_opcao.get(opcao, "Pagamento")

        recibo = Recibo(
            total=float(resultado["total"]),
            metodo=metodo,
            parcelas=int(resultado.get("num_parcelas", num_parcelas)),
            informacoes_adicionais=str(resultado.get("taxas", "")),
        )
        self._persistir(recibo)
        return resultado
