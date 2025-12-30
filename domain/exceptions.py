# domain/exceptions.py


class LojaAppError(Exception):
    """Base para todos os erros da aplicação."""

    pass


class PagamentoInvalidoError(LojaAppError):
    """Lançada quando a opção de pagamento não existe."""

    pass


class PersistenciaError(LojaAppError):
    """Lançada quando o storage falha (ex: disco cheio, permissão)."""

    pass
