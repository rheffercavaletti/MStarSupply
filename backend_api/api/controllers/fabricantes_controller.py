from .. import models

def get_fabricante(id):
    fabricante = models.Fabricante.query.get(id)
    return fabricante.to_dict()

def get_fabricantes():
    fabricantes = models.Fabricante.query.all()
    return [fabricante.to_dict() for fabricante in fabricantes]