from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from api.routes import api_blueprint
from api.models import db

API_VERSION = 'v0.1.0'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_CONNECTION_URI
CORS(app)
db.init_app(app)
app.register_blueprint(api_blueprint, url_prefix=f'/api/{API_VERSION}')
swagger = Swagger(app)