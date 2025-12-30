from datetime import datetime
from typing import Optional
from config.settings import get_settings, TaxasConfig
from services.pagamento_service import PagamentoService
from ui.menu import obter_dados_pagamento, exibir_recibo
from api.main import app



def localizar_salvamento() -> Optional[callable]:
    try:
        from infra.storage import salvar_recibo  # type: ignore
        return salvar_recibo
    except Exception:
        return None


def main() -> None:
    # Carregar configuração
    try:
        taxas_conf: TaxasConfig = get_settings()
    except Exception:
        taxas_conf = TaxasConfig(desconto_vista=0.0, juros_parcelamento=0.0)

    # Instanciar serviço 
    service = PagamentoService(taxas_conf.desconto_vista, taxas_conf.juros_parcelamento)

    valor, opcao, num_parcelas, metodo = obter_dados_pagamento()
    try:
        resultado = service.calculadora.calcular_por_opcao(opcao, valor, num_parcelas)
    except (ValueError, TypeError) as exc:
    #ui
        print(f"Erro: {exc}")
        return
    except Exception:
        print("Erro inesperado ao processar o pagamento. Tente novamente mais tarde.")
        return

    # Montar recibo
    now = datetime.now()
    recibo = {
        "data_hora": now,
        "metodo": metodo,
        "parcelas": resultado.get("num_parcelas"),
        "valor_da_parcela": resultado.get("valor_parcela"),
        "total": resultado.get("total"),
        "valor_original": round(float(valor), 2),
        "taxas": resultado.get("taxas"),
    }

    # Delegar exibição ao UI
    exibir_recibo(recibo)

    # Persistência (best-effort)
    salvar = localizar_salvamento()
    if salvar:
        try:
            saved = salvar(recibo)
            # Mensagem curta e não intrusiva
            print("Recibo salvo em:", saved)
        except Exception as exc:
            print(f"Aviso: falha ao salvar recibo: {exc}")
    else:
        print("Aviso: persistência de recibos não disponível (infra.storage).")


if __name__ == "__main__":
    main()