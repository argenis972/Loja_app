import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class TaxasConfig:
    desconto_vista: float
    juros_parcelamento: float


def _validate_taxas(data: Any) -> TaxasConfig:
    if not isinstance(data, dict):
        raise TypeError("Formato inválido de taxas: esperado um objeto JSON.")
    if "desconto_vista" not in data or "juros_parcelamento" not in data:
        raise ValueError(
            "Arquivo de taxas deve conter 'desconto_vista' e 'juros_parcelamento'."
        )
    desconto = data["desconto_vista"]
    juros = data["juros_parcelamento"]
    if not isinstance(desconto, (int, float)) or not isinstance(juros, (int, float)):
        raise TypeError("As taxas devem ser numéricas (int ou float).")
    desconto = float(desconto)
    juros = float(juros)
    if desconto < 0 or juros < 0:
        raise ValueError("As taxas não podem ser negativas.")
    return TaxasConfig(desconto_vista=desconto, juros_parcelamento=juros)


def get_settings(path: str | None = None) -> TaxasConfig:
    """
    Lê o arquivo config/taxas.json e retorna um TaxasConfig validado.
    A leitura do arquivo ocorre somente quando esta função for chamada.
    """
    if path is None:
        # arquivo taxas.json localizado no mesmo diretório que este módulo
        path = Path(__file__).parent / "taxas.json"
    else:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return _validate_taxas(data)
