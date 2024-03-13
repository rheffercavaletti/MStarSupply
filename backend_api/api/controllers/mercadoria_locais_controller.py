from .. import models

def get_mercadoria_local(id):
    mercadoria_local = models.Mercadoria_Local.query.get(id)
    return mercadoria_local.to_dict()

def get_mercadoria_locais():
    mercadoria_locais = models.Mercadoria_Local.query.all()
    return [mercadoria_local.to_dict() for mercadoria_local in mercadoria_locais]