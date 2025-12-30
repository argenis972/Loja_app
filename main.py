
from datetime import datetime
from typing import Any, Callable, Optional

from config.settings import get_settings, TaxasConfig
from services.pagamento_service import PagamentoService
from ui import exibir_menu_principal, exibir_recibo


def localizar_funcao_persistencia() -> Optional[Callable[[dict], Any]]:
    try:
        from infra.storage import salvar_recibo  # type: ignore
        return salvar_recibo  # type: ignore
    except Exception:
        pass

    # 2) módulo storage com nomes comuns
    try:
        import storage  # type: ignore
        for nome in ("salvar_recibo", "save_receipt", "save", "salvar"):
            if hasattr(storage, nome):
                return getattr(storage, nome)
    except Exception:
        pass

    # 3) domain.recibo com classe Recibo
    try:
        from domain.recibo import Recibo  # type: ignore

        def salvar_via_recibo(rec: dict) -> Any:
            try:
                inst = Recibo(rec)  # tentar instanciar
                if hasattr(inst, "salvar"):
                    return inst.salvar()
                if hasattr(inst, "save"):
                    return inst.save()
            except TypeError:
                if hasattr(Recibo, "salvar"):
                    return Recibo.salvar(rec)  # type: ignore
                if hasattr(Recibo, "save"):
                    return Recibo.save(rec)  # type: ignore
            raise RuntimeError("Não foi possível usar domain.Recibo para persistência.")
        return salvar_via_recibo
    except Exception:
        pass

    return None


def main() -> None:
    # Carregar taxas (I/O apenas aqui)
    try:
        taxas: TaxasConfig = get_settings()
    except FileNotFoundError:
        print("Arquivo de configuração de taxas não encontrado. Usando taxas 0.0%.")
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)
    except Exception as exc:
        print(f"Aviso ao carregar taxas ({exc}). Usando taxas 0.0%.")
        taxas = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    # Localiza função de persistência (se houver)
    salvar_recibo = localizar_funcao_persistencia()

    # UI: obter dados do usuário (valor, método, parcelas)
    valor_total, metodo, num_parcelas = exibir_menu_principal()

    # Instanciar serviço com as taxas injetadas
    service = PagamentoService(taxas.desconto_vista, taxas.juros_parcelamento)

    # Chamar serviço e tratar erros amigáveis
    try:
        resultado = service.criar_pagamento(valor=valor_total, num_parcelas=num_parcelas)
    except (ValueError, TypeError) as exc:
        print(f"Erro ao processar pagamento: {exc}")
        return
    except Exception:
        print("Erro inesperado ao processar o pagamento. Tente novamente mais tarde.")
        return

    # Montar recibo (dicionário)
    now = datetime.now()
    recibo = {
        "data_hora": now,
        "metodo": metodo,
        "parcelas": resultado.get("num_parcelas"),
        "valor_da_parcela": resultado.get("valor_parcela"),
        "total": resultado.get("total"),
        "valor_original": round(float(valor_total), 2),
        "taxas": {
            "desconto_vista": taxas.desconto_vista,
            "juros_parcelamento": taxas.juros_parcelamento,
        },
    }

    # Exibir recibo via UI
    exibir_recibo(recibo)

    # Persistência (se disponível)
    if salvar_recibo:
        try:
            salvar_recibo(recibo)
            print("Recibo salvo com sucesso.")
        except Exception as exc:
            print(f"Aviso: falha ao salvar o recibo: {exc}")
    else:
        print("Aviso: função de persistência não encontrada. Recibo não foi salvo.")


if __name__ == "__main__":
    main()