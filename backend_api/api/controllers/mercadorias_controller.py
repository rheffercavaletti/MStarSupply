from .. import models

def get_mercadoria(id):
    mercadoria = models.Mercadoria.query.get(id)
    return mercadoria.to_dict()

def get_mercadorias():
    mercadorias = models.Mercadoria.query.filter(models.Mercadoria.deletado == False)
    return [mercadoria.to_dict() for mercadoria in mercadorias]

def post_mercadoria(data):
    mercadoria = models.Mercadoria(
        nome = data['nome'],
		numero_registro = data['numero_registro'],
		fabricante_id = data['fabricante_id'],
		mercadoria_tipo_id = data['mercadoria_tipo_id'],
		descricao = data['descricao']
    )
    models.db.session.add(mercadoria)
    models.db.session.commit()

def put_mercadoria(id, data):
    mercadoria = models.Mercadoria.query.get(id)
    if not mercadoria:
        raise Exception(f'Mercadoria <id={id}> não encontrada')

    mercadoria.nome = data['nome']
    mercadoria.numero_registro = data['numero_registro']
    mercadoria.fabricante_id = data['fabricante_id']
    mercadoria.mercadoria_tipo_id = data['mercadoria_tipo_id']
    mercadoria.descricao = data['descricao']

    models.db.session.add(mercadoria)
    models.db.session.commit()

def delete_mercadoria(id):
    mercadoria = models.Mercadoria.query.get(id)
    if not mercadoria:
        raise Exception(f'Mercadoria <id={id}> não encontrada')
    mercadoria.deletado = True
    models.db.session.add(mercadoria)
    models.db.session.commit()