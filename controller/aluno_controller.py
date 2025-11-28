from flask import Blueprint, jsonify, request
import model.aluno_model as aluno_model

aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/alunos')



@aluno_bp.route('', methods=['GET'])
def get_alunos():
    try:
        alunos = aluno_model.retornar_aluno()
        return jsonify(alunos), 200
        
    except Exception as e:
        return jsonify({'Erro': f'não foi possível retornar lista de alunos: {e}'}), 500


@aluno_bp.route('/<int:user_id>', methods=['GET'])
def get_aluno_id(user_id):
    try:
        aluno = aluno_model.retornar_aluno_por_id(user_id)
        if aluno:
            return jsonify(aluno),200
        else:
            return jsonify({'erro':'Aluno não encontrado.'}), 404
    except Exception as e:
        return jsonify({'Erro': f'Erro ao retornar aluno: {e}'}),500


@aluno_bp.route('/', methods=['POST'])
def create_aluno():
    try:
        novo_aluno = request.get_json()
        aluno_criado = aluno_model.criar_aluno(novo_aluno)
        return jsonify({'mensagem':'Aluno criado com sucesso!',
                        'aluno': aluno_criado}), 201
    except Exception as e:
        return jsonify({'erro': f'Erro ao criar aluno: {e}'}), 500


@aluno_bp.route('/limpar', methods =['POST'])
def limpar_campos_aluno():
    try:
        campos_limpos = aluno_model.limpar_campos_aluno()
        return jsonify({'mensagem':'Campos limpos com sucesso!', 
                        'campos': campos_limpos}),200
    except Exception as e:
        return jsonify({'erro':f'Erro ao tentar limpar os campos: {e}'}), 500

#####################################################################################
@aluno_bp.route('/<int:user_id>', methods =['PATCH'])
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
    
#####################################################################################
@aluno_bp.route('/<int:user_id>', methods = ['DELETE'])
def delete_aluno(user_id):
    try:
        aluno_deletado = aluno_model.deletar_aluno_por_id(user_id)
        if aluno_deletado is True:
            return jsonify({'mensagem':'aluno deletado com sucesso!'}), 200
        return jsonify({'erro': 'aluno não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro':f'Erro ao deletar aluno: {e}'}), 500
    
