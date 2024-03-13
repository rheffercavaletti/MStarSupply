from flask import jsonify, request
from flasgger import swag_from
from . import api_blueprint
from .controllers import *


@api_blueprint.route('/', methods=['GET'])
@swag_from({
    'summary': 'Status da API',
    'responses': {
        200: {
            'description': 'Mensagem de status da API com a data e hora atuais'
        }
    }
})
def home():
    return home_controller.get_api_home()

@api_blueprint.route('/init_test_db', methods=['GET'])
def init_test_db():
    return home_controller.get_init_test_db(), 200


#MERCADORIAS
@api_blueprint.route('/mercadorias/<int:id>', methods=['GET'])
@swag_from({
    'summary': 'Obter detalhes de uma mercadoria pelo ID',
    'parameters': [
        {
            'in': 'path',
            'name': 'id',
            'required': True,
            'description': 'ID da mercadoria a ser obtida',
            'schema': {'type': 'integer'}
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes da mercadoria obtidos com sucesso',
        },
        404: {
            'description': 'Mercadoria não encontrada'
        }
    }
})
def get_mercadoria(id):
    return jsonify(mercadorias_controller.get_mercadoria(id)), 200

@api_blueprint.route('/mercadorias', methods=['GET'])
@swag_from({
    'summary': 'Listar todas as mercadorias',
    'responses': {
        200: {
            'description': 'Lista de mercadorias obtida com sucesso',
        }
    }
})
def get_mercadorias():
    return jsonify(mercadorias_controller.get_mercadorias()), 200

@api_blueprint.route('/mercadorias', methods=['POST'])
def post_mercadoria():
    """Adicionar uma nova mercadoria
    Cria uma nova mercadoria no sistema.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Mercadoria
          required:
            - nome
            - numero_registro
            - fabricante_id
            - mercadoria_tipo_id
            - descricao
          properties:
            nome:
              type: string
              description: nome da mercadoria
            numero_registro:
              type: string
              description: número de registro da mercadoria
            fabricante_id:
              type: integer
              description: id do fabricante da mercadoria
            mercadoria_tipo_id:
              type: integer
              description: id do tipo da mercadoria
            descricao:
              type: string
              description: descrição da mercadoria
    responses:
      201:
        description: Mercadoria adicionada com sucesso
    """
    data = request.get_json()
    mercadorias_controller.post_mercadoria(data)
    return jsonify({'message': 'Mercadoria adicionada com sucesso'}), 201

@api_blueprint.route('/mercadorias/<int:id>', methods=['PUT'])
@swag_from({
    'summary': 'Atualizar uma mercadoria pelo ID',
    'parameters': [
        {
            'in': 'path',
            'name': 'id',
            'required': True,
            'description': 'ID da mercadoria a ser atualizada',
            'schema': {'type': 'integer'}
        }
    ],
    'responses': {
        200: {
            'description': 'Mercadoria atualizada com sucesso',
        }
    }
})
def put_mercadoria(id):
    data = request.get_json()
    mercadorias_controller.put_mercadoria(id, data)
    return jsonify({'message': 'Mercadoria atualizada com sucesso'}), 200

@api_blueprint.route('/mercadorias/<int:id>', methods=['DELETE'])
@swag_from({
    'summary': 'Apagar uma mercadoria pelo ID',
    'parameters': [
        {
            'in': 'path',
            'name': 'id',
            'required': True,
            'description': 'ID da mercadoria a ser apagada',
            'schema': {'type': 'integer'}
        }
    ],
    'responses': {
        200: {
            'description': 'Mercadoria apagada com sucesso',
        }
    }
})
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