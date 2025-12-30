import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

try:
    # Import opcional — se não existir, geraremos apenas JSON e TXT
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _serialize_recibo(recibo: Dict[str, Any]) -> Dict[str, Any]:
    """
    Garante que todos os campos do recibo sejam serializáveis em JSON.
    Converte datetimes para ISO strings, etc.
    """
    serial = {}
    for k, v in recibo.items():
        if isinstance(v, datetime):
            serial[k] = v.isoformat()
        elif isinstance(v, dict):
            serial[k] = _serialize_recibo(v)
        else:
            # números, strings, listas etc.
            serial[k] = v
    return serial


def _gerar_pdf(path_pdf: Path, recibo: Dict[str, Any]) -> None:
    """
    Gera um PDF simples com os dados do recibo usando reportlab.
    """
    c = canvas.Canvas(str(path_pdf), pagesize=A4)
    width, height = A4

    margem_esquerda = 40
    y = height - 60

    c.setFont("Helvetica-Bold", 14)
    c.drawString(margem_esquerda, y, "RESUMO DO PAGAMENTO")
    y -= 30

    c.setFont("Helvetica", 10)

    def linha(chave: str, valor: str):
        nonlocal y
        c.drawString(margem_esquerda, y, f"{chave}: {valor}")
        y -= 16

    # Cabeçalho com data/hora
    data_hora = recibo.get("data_hora")
    if hasattr(data_hora, "strftime"):
        data_hora_str = data_hora.strftime("%Y-%m-%d %H:%M:%S")
    else:
        data_hora_str = str(data_hora)
    linha("Data/Hora", data_hora_str)

    linha("Método de pagamento", str(recibo.get("metodo", "")))
    linha("Valor original", f"R$ {recibo.get('valor_original', 0.0):,.2f}")
    parcelas = recibo.get("parcelas", 1)
    if parcelas and int(parcelas) > 1:
        linha("Número de parcelas", str(parcelas))
        linha("Valor de cada parcela", f"R$ {recibo.get('valor_da_parcela', 0.0):,.2f}")
    else:
        linha("Pagamento", "À vista")
    linha("Total a pagar", f"R$ {recibo.get('total', 0.0):,.2f}")

    taxas = recibo.get("taxas", {})
    if taxas:
        linha(
            "Taxas",
            f"desconto_vista={taxas.get('desconto_vista')}% "
            f"juros_parcelamento={taxas.get('juros_parcelamento')}%",
        )
    # Observação final
    y -= 8
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(margem_esquerda, y, "Recibo gerado pelo sistema Loja_app")

    c.showPage()
    c.save()


def salvar_recibo(recibo: Dict[str, Any], dirpath: str = "receipts") -> Dict[str, str]:
    base_dir = Path(dirpath)
    _ensure_dir(base_dir)

    # normalizar/serializar o recibo para JSON
    serial = _serialize_recibo(recibo)

    # gerar nomes únicos com timestamp e uuid
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    uid = uuid.uuid4().hex[:8]
    json_name = f"recibo_{ts}_{uid}.json"
    json_path = base_dir / json_name

    try:
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(serial, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise RuntimeError(f"Falha ao salvar recibo JSON: {e}")

    saved = {"json": str(json_path)}

    # tentar gerar PDF
    if REPORTLAB_AVAILABLE:
        pdf_name = f"recibo_{ts}_{uid}.pdf"
        pdf_path = base_dir / pdf_name
        try:
            _gerar_pdf(pdf_path, recibo)
            saved["pdf"] = str(pdf_path)
        except Exception as e:
            """Se falhar a geração de PDF,
            não interromper o fluxo; apenas reportar no retorno"""
            saved["pdf_error"] = str(e)
    else:
        # fallback: gerar um .txt simples para visualizar se não houver reportlab
        txt_name = f"recibo_{ts}_{uid}.txt"
        txt_path = base_dir / txt_name
        try:
            with txt_path.open("w", encoding="utf-8") as f:
                f.write("RESUMO DO PAGAMENTO\n")
                f.write("===================\n")
                for k, v in serial.items():
                    f.write(f"{k}: {v}\n")
            saved["txt"] = str(txt_path)
        except Exception as e:
            saved["txt_error"] = str(e)
    return saved
