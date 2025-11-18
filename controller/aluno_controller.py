from flask import Blueprint, jsonify, request
import model.aluno_model as aluno_model

aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/alunos')

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    try:
        alunos = aluno_model.retornar_aluno()
        if alunos:
            return jsonify(alunos), 200
        else:
            return jsonify(f'Erro ao retornar lista de alunos.'), 404
    except Exception as e:
        return jsonify({'Erro':f'Erro ao tentar retornar lista de alunos: {e}'}), 500


@aluno_bp.route('/alunos/<int: user_id>', methods=['GET'])
def get_aluno_id(user_id):
    try:
        aluno = aluno_model.retornar_aluno_por_id(user_id)
        if aluno:
            return jsonify(aluno),200
        else:
            return jsonify(f'Aluno não encontrado.'), 404
    except Exception as e:
        return jsonify({'Erro': f'Erro ao retornar aluno: {e}'}),500
    

@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno(novo_aluno):
    try:
        novo_aluno = request.get_json
        aluno_criado = aluno_model.criar_aluno(novo_aluno)
        return jsonify({'mensagem':'Aluno criado com sucesso!',
                        'aluno': aluno_criado}), 201
    except Exception as e:
        return jsonify({'erro':f'Erro ao criar aluno: {e}'}), 500


@aluno_bp.route('/alunos', methods =['PUT'])
def limpar_campos_aluno():
    try:
        campos_limpos = aluno_model.limpar_campos_aluno()
        return jsonify(f'Campos limpos com sucesso!', campos_limpos),200
    except Exception as e:
        return jsonify({'erro':f'Erro ao tentar limpar os campos. Erro: {e}'}), 500


@aluno_bp.route('/alunos/<int:user_id>', methods =['PATCH'])
def atualizar_aluno(user_id):
    try:
        novos_dados = request.get_json()
        if not novos_dados:
            return jsonify({'erro':'Dados de atualização não fornecidos'}), 400
        
        aluno_atualizado = aluno_model.atualizar_aluno_por_id(user_id, novos_dados)

        if isinstance(novos_dados, dict) and 'erro' in aluno_atualizado:
            return jsonify(aluno_atualizado), 400
        
        return jsonify({'Mensagem':'Aluno atualizado com sucesso!',
                        'Aluno': aluno_atualizado}), 200
    except Exception as e:
        return jsonify({'erro': f'Erro ao atualizar aluno. Erro: {e}'}), 500
    

@aluno_bp.route('/alunos/<int:user_id', methods = ['DELETE'])
def delete_aluno(user_id):
    try:
        aluno_deletado = aluno_model.deletar_aluno_por_id(user_id)
        if aluno_deletado is True:
            return jsonify({'Aluno deletado com sucesso!'}), 200
        return jsonify({'erro': 'Aluno não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro':f'Erro ao deletar aluno: {e}'}), 500
    
