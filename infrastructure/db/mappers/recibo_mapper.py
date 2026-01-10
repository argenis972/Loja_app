from domain.models.recibo import Recibo
from infrastructure.db.models.recibo_model import ReciboModel


def to_model(entity: Recibo) -> ReciboModel:
    return ReciboModel(
        total=entity.total,
        metodo=entity.metodo,
        parcelas=entity.parcelas,
        informacoes_adicionais=entity.informacoes_adicionais,
        data_hora=entity.data_hora,
    )


def to_entity(model: ReciboModel) -> Recibo:
    recibo = Recibo(
        total=model.total,
        metodo=model.metodo,
        parcelas=model.parcelas,
        informacoes_adicionais=model.informacoes_adicionais,
    )
    recibo.data_hora = model.data_hora
    return recibo
