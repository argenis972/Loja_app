import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _serialize_recibo(recibo: Dict[str, Any]) -> Dict[str, Any]:
    serial: Dict[str, Any] = {}
    for k, v in recibo.items():
        if isinstance(v, datetime):
            serial[k] = v.isoformat()
        elif isinstance(v, dict):
            serial[k] = _serialize_recibo(v)
        else:
            serial[k] = v
    return serial


def _gerar_pdf(path_pdf: Path, recibo: Dict[str, Any]) -> None:
    if not REPORTLAB_AVAILABLE:
        return

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

    taxas = recibo.get("taxas", "")
    if taxas:
        linha("Taxas", str(taxas))

    y -= 8
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(margem_esquerda, y, "Recibo gerado pelo sistema Loja_app")

    c.showPage()
    c.save()


def salvar_recibo(recibo: Dict[str, Any], dirpath: str = "receipts") -> Dict[str, str]:
    """
    Persistencia del CLI:
    - guarda un JSON serializado en /receipts
    - opcionalmente genera un PDF si reportlab está disponible
    """
    base_dir = Path(dirpath)
    _ensure_dir(base_dir)

    serial = _serialize_recibo(recibo)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    uid = uuid.uuid4().hex[:8]
    json_name = f"recibo_{ts}_{uid}.json"
    json_path = base_dir / json_name

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(serial, f, ensure_ascii=False, indent=2)

    result = {"json": str(json_path)}

    if REPORTLAB_AVAILABLE:
        pdf_name = f"recibo_{ts}_{uid}.pdf"
        pdf_path = base_dir / pdf_name
        _gerar_pdf(pdf_path, recibo)
        result["pdf"] = str(pdf_path)

    return result