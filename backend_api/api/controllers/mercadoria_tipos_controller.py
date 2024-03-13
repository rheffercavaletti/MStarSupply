from .. import models

def get_mercadoria_tipo(id):
    mercadoria_tipo = models.Mercadoria_Tipo.query.get(id)
    return mercadoria_tipo.to_dict()

def get_mercadoria_tipos():
    mercadoria_tipos = models.Mercadoria_Tipo.query.all()
    return [mercadoria_tipo.to_dict() for mercadoria_tipo in mercadoria_tipos]