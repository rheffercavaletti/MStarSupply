from .. import models
from sqlalchemy import func, case, extract
from datetime import datetime

def post_mercadoria_movimentacao(mercadoria_id, data):
    movimentacao = models.Mercadoria_Movimentacao(
        data_hora = data['data_hora'],
		mercadoria_id = mercadoria_id,
		quantidade = data['quantidade'],
		mercadoria_local_id = data['mercadoria_local_id']
    )
    
    models.db.session.add(movimentacao)
    models.db.session.commit()

def get_mercadorias_movimentacoes_totais():
    resumo = models.db.session.query(
        models.Mercadoria.nome.label('mercadoria'),
        func.sum(
            case(
                (models.Mercadoria_Movimentacao.quantidade > 0, models.Mercadoria_Movimentacao.quantidade),
                else_=0
            )
        ).label('entradas'),
        func.sum(
            case(
                (models.Mercadoria_Movimentacao.quantidade < 0, - models.Mercadoria_Movimentacao.quantidade),
                else_=0
            )
        ).label('saidas')
    ).join(models.Mercadoria, models.Mercadoria.id == models.Mercadoria_Movimentacao.mercadoria_id
    ).group_by(models.Mercadoria.nome).filter(models.Mercadoria.deletado == False)
    return [{
        'mercadoria': r.mercadoria,
        'entradas': r.entradas,
        'saidas': r.saidas
        } for r in resumo ]

def get_mercadoria_movimentacoes_por_mes(mercadoria_id):
    resumo = models.db.session.query(
        extract('year', models.Mercadoria_Movimentacao.data_hora).label('ano'),
        extract('month', models.Mercadoria_Movimentacao.data_hora).label('mes'),
        models.Mercadoria.nome.label('nome_produto'),
        func.sum(
            case(
                (models.Mercadoria_Movimentacao.quantidade > 0, models.Mercadoria_Movimentacao.quantidade),
                else_=0
            )
        ).label('entradas'),
        func.sum(
            case(
                (models.Mercadoria_Movimentacao.quantidade < 0, -models.Mercadoria_Movimentacao.quantidade),
                else_=0
            )
        ).label('saidas')
    ).join(models.Mercadoria, models.Mercadoria.id == models.Mercadoria_Movimentacao.mercadoria_id
    ).group_by('ano', 'mes', models.Mercadoria.nome).filter(models.Mercadoria.deletado == False, models.Mercadoria.id == mercadoria_id)
    return[{
        'mes_ano': f'{str(r.mes).zfill(2)}/{r.ano}',
        'entradas': r.entradas,
        'saidas': r.saidas
    } for r in resumo ]