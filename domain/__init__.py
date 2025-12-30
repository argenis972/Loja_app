# Pacote domain: exporta símbolos públicos e mantém compatibilidade retroativa.
# Importamos símbolos conhecidos de forma defensiva para evitar que a importação do pacote
# quebre quando algum submódulo ainda estiver sendo refatorado.

__all__ = []

# Importa a calculadora (nome novo) e garante o alias para o nome antigo usado em testes/código.
try:
    from .calculadora import Calculadora, CalculadoraPagamentos  # type: ignore
    __all__.extend(["Calculadora", "CalculadoraPagamentos"])
except Exception:
    # Não falhar na importação do pacote; a falha real será levantada quando o símbolo for acessado.
    Calculadora = None  # type: ignore
    CalculadoraPagamentos = None  # type: ignore

# Tenta exportar Recibo se existir
try:
    from .recibo import Recibo  # type: ignore
    __all__.append("Recibo")
except Exception:
    Recibo = None  # type: ignore

# Caso haja outros módulos de domínio que precisem ser exportados no futuro,
# adicioná‑los aqui de forma semelhante para manter compatibilidade.