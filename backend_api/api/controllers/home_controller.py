from .. import models
from datetime import datetime

def get_api_home():
    try:
        data_ok = models.Fabricante.query.count() > 0
    except:
        data_ok = False
    if not data_ok:
        get_init_test_db()
    return f'MStarSupply - backend api - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

def get_init_test_db():
    import init_test_db as initDb
    initDb.drop_create_data()
    return 'banco de dados recriado, dados de teste inseridos'
