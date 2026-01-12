#from flask import Blueprint, jsonify, request

from flask_restx import Namespace, Resource, fields
import model.aluno_model as aluno_model

#aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/alunos')
aluno_ns = Namespace(
    'alunos',
    description= 'Operacoes relacionadas a alunos'
)

aluno_model_swagger = aluno_ns.model('Aluno',{
    'nome': fields.String(required=True, description= 'Nome do aluno'),
    'idade': fields.Integer(required=True, description= 'Idade do aluno')
})

aluno_response_model = aluno_ns.model('AlunoResponse', {
    'id': fields.Integer(description='Id do aluno'),
    'nome': fields.String(description='Nome do aluno'),
    'idade': fields.String(description='Idade do aluno')
})


@aluno_ns.route('/')
class AlunoList(Resource):
    def get(self):
        return {"mensagem": "Lista de alunos"}
    
           
    @aluno_ns.expect(aluno_model_swagger, validate=True)
    @aluno_ns.marshal_with(aluno_response_model, code=201)
    def post(self):
        dados = aluno_ns.payload
        aluno_criado = aluno_model.criar_aluno(dados)
        return aluno_criado, 201

@aluno_ns.route('/<int:id>')
class AlunoResource(Resource):
    @aluno_ns.marshal_with(aluno_response_model)
    @aluno_ns.response(200, 'Aluno encontrado')
    @aluno_ns.response(404, 'Aluno não encontrado')
    def get(self, id):
        aluno= aluno_model.retornar_aluno_por_id(id)
        if not aluno:
            aluno_ns.abort(404, 'Aluno não encontrado')
        return aluno
#@aluno_bp.route('', methods=['GET'])       NAMESPACE FEITO
def get_alunos():
    try:
        alunos = aluno_model.retornar_aluno()
        return jsonify(alunos), 200
        
    except Exception as e:
        return jsonify({'Erro': f'não foi possível retornar lista de alunos: {e}'}), 500


#@aluno_bp.route('/<int:user_id>', methods=['GET'])     NAMESPACE FEITO
def get_aluno_id(user_id):
    try:
        aluno = aluno_model.retornar_aluno_por_id(user_id)
        if aluno:
            return jsonify(aluno),200
        else:
            return jsonify({'erro':'Aluno não encontrado.'}), 404
    except Exception as e:
        return jsonify({'Erro': f'Erro ao retornar aluno: {e}'}),500


#@aluno_bp.route('/', methods=['POST'])     NAMESPACE FEITO
def create_aluno():
    try:
        novo_aluno = request.get_json()
        aluno_criado = aluno_model.criar_aluno(novo_aluno)
        return jsonify({'mensagem':'Aluno criado com sucesso!',
                        'aluno': aluno_criado}), 201
    except Exception as e:
        return jsonify({'erro': f'Erro ao criar aluno: {e}'}), 500


#@aluno_bp.route('/limpar', methods =['POST'])  
def limpar_campos_aluno():
    try:
        campos_limpos = aluno_model.limpar_campos_aluno()
        return jsonify({'mensagem':'Campos limpos com sucesso!', 
                        'campos': campos_limpos}),200
    except Exception as e:
        return jsonify({'erro':f'Erro ao tentar limpar os campos: {e}'}), 500


#@aluno_bp.route('/<int:user_id>', methods =['PATCH'])
def atualizar_aluno(user_id):
    try:
        novos_dados = request.get_json()
        if not novos_dados:
            return jsonify({'erro':'Dados de atualização não fornecidos'}), 400
        
        aluno_atualizado = aluno_model.atualizar_aluno_por_id(user_id, novos_dados)

        if isinstance(aluno_atualizado, dict) and 'erro' in aluno_atualizado:
            return jsonify(aluno_atualizado), 400
        
        return jsonify({'mensagem':'aluno atualizado com sucesso!',
                        'Aluno': aluno_atualizado}), 200
    except Exception as e:
        return jsonify({'erro': f'Erro ao atualizar aluno. Erro: {e}'}), 500
    

#@aluno_bp.route('/<int:user_id>', methods = ['DELETE'])
def delete_aluno(user_id):
    try:
        aluno_deletado = aluno_model.deletar_aluno_por_id(user_id)
        if aluno_deletado is True:
            return jsonify({'mensagem':'aluno deletado com sucesso!'}), 200
        return jsonify({'erro': 'aluno não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro':f'Erro ao deletar aluno: {e}'}), 500
    
