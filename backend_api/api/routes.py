from flask import jsonify, request
from . import api_blueprint
from .controllers import *


@api_blueprint.route('/', methods=['GET'])
def home():
    return home_controller.get_api_home()

@api_blueprint.route('/init_test_db', methods=['GET'])
def init_test_db():
    return home_controller.get_init_test_db(), 200


#MERCADORIAS
@api_blueprint.route('/mercadorias/<int:id>', methods=['GET'])
def get_mercadoria(id):
    return jsonify(mercadorias_controller.get_mercadoria(id)), 200

@api_blueprint.route('/mercadorias', methods=['GET'])
def get_mercadorias():
    return jsonify(mercadorias_controller.get_mercadorias()), 200

@api_blueprint.route('/mercadorias', methods=['POST'])
def post_mercadoria():
    data = request.get_json()
    mercadorias_controller.post_mercadoria(data)
    return jsonify({'message': 'Mercadoria adicionada com sucesso'}), 201

@api_blueprint.route('/mercadorias/<int:id>', methods=['PUT'])
def put_mercadoria(id):
    data = request.get_json()
    mercadorias_controller.put_mercadoria(id, data)
    return jsonify({'message': 'Mercadoria atualizada com sucesso'}), 200

@api_blueprint.route('/mercadorias/<int:id>', methods=['DELETE'])
def delete_mercadoria(id):
    mercadorias_controller.delete_mercadoria(id)
    return jsonify({'message': 'Mercadoria apagada com sucesso'}), 200


#FABRICANTES
@api_blueprint.route('/fabricantes/<int:id>', methods=['GET'])
def get_fabricante(id):
    return jsonify(fabricantes_controller.get_fabricante(id)), 200

@api_blueprint.route('/fabricantes', methods=['GET'])
def get_fabricantes():
    return jsonify(fabricantes_controller.get_fabricantes()), 200


#MERCADORIA_TIPOS
@api_blueprint.route('/mercadorias/tipos/<int:id>', methods=['GET'])
def get_mercadoria_tipo(id):
    return jsonify(mercadoria_tipos_controller.get_mercadoria_tipo(id)), 200

@api_blueprint.route('/mercadorias/tipos', methods=['GET'])
def get_mercadoria_tipos():
    return jsonify(mercadoria_tipos_controller.get_mercadoria_tipos()), 200


#MERCADORIA_LOCAIS
@api_blueprint.route('/mercadorias/locais/<int:id>', methods=['GET'])
def get_mercadoria_local(id):
    return jsonify(mercadoria_locais_controller.get_mercadoria_local(id)), 200

@api_blueprint.route('/mercadorias/locais', methods=['GET'])
def get_mercadoria_locais():
    return jsonify(mercadoria_locais_controller.get_mercadoria_locais()), 200


#MERCADORIA_MOVIMENTACOES
@api_blueprint.route('/mercadorias/<int:id>/movimentacoes', methods=['POST'])
def post_mercadoria_movimentacao(id):
    data = request.get_json()
    mercadoria_movimentacoes_controller.post_mercadoria_movimentacao(id, data)
    return jsonify({'message': 'Movimentação adicionada com sucesso'}), 201

@api_blueprint.route('/mercadorias/movimentacoes/totais', methods=['GET'])
def get_mercadorias_movimentacoes_por_mes():
    return jsonify(mercadoria_movimentacoes_controller.get_mercadorias_movimentacoes_totais()), 200

@api_blueprint.route('/mercadorias/<int:id>/movimentacoes/mensal', methods=['GET'])
def get_mercadoria_movimentacoes_por_mes(id):
    return jsonify(mercadoria_movimentacoes_controller.get_mercadoria_movimentacoes_por_mes(id)), 200
