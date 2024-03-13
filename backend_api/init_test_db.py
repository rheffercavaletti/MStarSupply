from app import db
import api.models as M
from sqlalchemy import asc
from datetime import datetime


def drop_create_data():
    db.drop_all()
    db.create_all()
    print('banco de dados recriado')


    #FABRICANTES
    fabricantes = [
        {'nome': 'Fabricante A'},
        {'nome': 'Fabricante B'},
        {'nome': 'Fabricante C'},
    ]
    for r in fabricantes:
        fabricante = M.Fabricante(**r)
        db.session.add(fabricante)
    db.session.commit()
    print('fabricantes adicionados ao banco')


    #Tipos de Mercadoria
    mercadoria_tipos = [
        {'nome': 'Tipo A'},
        {'nome': 'Tipo B'},
        {'nome': 'Tipo C'},
        {'nome': 'Tipo D'},
        {'nome': 'Tipo E'},
    ]
    for r in mercadoria_tipos:
        mercadoria_tipo = M.Mercadoria_Tipo(**r)
        db.session.add(mercadoria_tipo)
    db.session.commit()
    print('tipos de mercadoria adicionados ao banco')
    

    #Mercadorias
    mercadorias = [
        {'nome': 'Mercadoria 01', 'numero_registro': 'NR9999_01', 'fabricante_id': 1, 'mercadoria_tipo_id': 1, 'descricao': 'Descrição Mercadoria 01'},
        {'nome': 'Mercadoria 02', 'numero_registro': 'NR9999_02', 'fabricante_id': 2, 'mercadoria_tipo_id': 2, 'descricao': 'Descrição Mercadoria 02'},
        {'nome': 'Mercadoria 03', 'numero_registro': 'NR9999_03', 'fabricante_id': 3, 'mercadoria_tipo_id': 3, 'descricao': 'Descrição Mercadoria 03'},
        {'nome': 'Mercadoria 04', 'numero_registro': 'NR9999_04', 'fabricante_id': 1, 'mercadoria_tipo_id': 4, 'descricao': 'Descrição Mercadoria 04'},
        {'nome': 'Mercadoria 05', 'numero_registro': 'NR9999_05', 'fabricante_id': 2, 'mercadoria_tipo_id': 5, 'descricao': 'Descrição Mercadoria 05'},
        {'nome': 'Mercadoria 06', 'numero_registro': 'NR9999_06', 'fabricante_id': 3, 'mercadoria_tipo_id': 1, 'descricao': 'Descrição Mercadoria 06'},
        {'nome': 'Mercadoria 07', 'numero_registro': 'NR9999_07', 'fabricante_id': 1, 'mercadoria_tipo_id': 2, 'descricao': 'Descrição Mercadoria 07'},
        {'nome': 'Mercadoria 08', 'numero_registro': 'NR9999_08', 'fabricante_id': 2, 'mercadoria_tipo_id': 3, 'descricao': 'Descrição Mercadoria 08'},
        {'nome': 'Mercadoria 09', 'numero_registro': 'NR9999_09', 'fabricante_id': 3, 'mercadoria_tipo_id': 4, 'descricao': 'Descrição Mercadoria 09'},
        {'nome': 'Mercadoria 10', 'numero_registro': 'NR9999_10', 'fabricante_id': 1, 'mercadoria_tipo_id': 5, 'descricao': 'Descrição Mercadoria 10'},
        {'nome': 'Mercadoria 11', 'numero_registro': 'NR9999_11', 'fabricante_id': 2, 'mercadoria_tipo_id': 1, 'descricao': 'Descrição Mercadoria 11'},
        {'nome': 'Mercadoria 12', 'numero_registro': 'NR9999_12', 'fabricante_id': 3, 'mercadoria_tipo_id': 2, 'descricao': 'Descrição Mercadoria 12'},
        {'nome': 'Mercadoria 13', 'numero_registro': 'NR9999_13', 'fabricante_id': 2, 'mercadoria_tipo_id': 3, 'descricao': 'Descrição Mercadoria 13'},
        {'nome': 'Mercadoria 14', 'numero_registro': 'NR9999_14', 'fabricante_id': 2, 'mercadoria_tipo_id': 4, 'descricao': 'Descrição Mercadoria 14'},
        {'nome': 'Mercadoria 15', 'numero_registro': 'NR9999_15', 'fabricante_id': 2, 'mercadoria_tipo_id': 5, 'descricao': 'Descrição Mercadoria 15'},
    ]
    for r in mercadorias:
        mercadoria = M.Mercadoria(**r)
        db.session.add(mercadoria)
    db.session.commit()
    print('mercadorias adicionadas ao banco')


    #Locais de Mercadoria
    locais = [
        {'nome': 'Deposito A'},
        {'nome': 'Deposito B'},
        {'nome': 'Deposito C'},
    ]
    for r in locais:
        local = M.Mercadoria_Local(**r)
        db.session.add(local)
    db.session.commit()
    print('locais adicionados ao banco')


    #Movimentações de Mercadoria
    for merc in M.Mercadoria.query.order_by(asc(M.Mercadoria.id)).all():
        for mes in range(1, 13):
            nreg = [1,3,4,9]
            nreg = nreg[(mes + merc.id) % len(nreg)]
            nqtd = [1,2,3,5,10,20,7,9,5,8]
            locais = [1,2,3]
            for n in range(nreg):
                qtd = nqtd[(mes + merc.id + n) % len(nqtd)] + n
                qtd = qtd if n % 2 == 0 else qtd * -1
                qtd = -1 * abs(qtd) if mes in [6,7,10] and not n % 2 else qtd
                dia = (mes * merc.id * n) % 28 + 1
                h = ((dia + abs(qtd)) * nreg ) % 13 + 8
                m = (dia * nreg) % 60
                d = datetime(2023, mes, dia, h, m, 0)

                mm = M.Mercadoria_Movimentacao()
                mm.data_hora = d.strftime('%Y-%m-%d %H:%M:%S')
                mm.mercadoria_id = merc.id
                mm.quantidade = qtd
                mm.mercadoria_local_id = locais[(mes + n + qtd) % len(locais)]
                
                db.session.add(mm)
    db.session.commit()

    print('movimentacoes adicionadas ao banco')