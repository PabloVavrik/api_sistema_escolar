from flask import Blueprint, jsonify, request
import model.aluno_model as aluno_model

aluno_bp = Blueprint('aluno_bp', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def retornar_alunos():
    try:
        alunos = aluno_model.retornar_aluno()
        if alunos:
            return jsonify(alunos), 200
        else:
            return jsonify(f'Erro ao retornar lista de alunos.'), 404
    except Exception as e:
        return jsonify({'Erro':f'Erro ao tentar retornar lista de alunos: {e}'}), 500



@aluno_bp.route('/alunos/<int: user_id>', methods=['GET'])
def retornar_alunos_por_id(user_id):
    try:
        aluno = aluno_model.retornar_aluno_por_id(user_id)
        if aluno:
            return jsonify(aluno),200
        else:
            return jsonify(f'Aluno não encontrado.'), 404
    except Exception as e:
        return jsonify({'Erro': f'Erro ao retornar aluno: {e}'}),500
    


@aluno_bp.route('/alunos', methods=['POST'])
def criar_aluno(novo_aluno):
    try:
        novo_aluno = request.get_json
        aluno_criado = aluno_model.criar_aluno(novo_aluno)
        return jsonify({'mensagem':'Aluno criado com sucesso!',
                        'aluno': aluno_criado}), 201
    except Exception as e:
        return jsonify({'erro':f'Erro ao criar aluno: {e}'}), 500
#EU ACABEI DE FAZER A FUNÇÃO, LA NO MODEL, PARA CRIAR O ID AUTOMATICAMENTE. JA COLOQUEI NO MODEL DE ALUNO E DE PROFESSOR
#A INCREMENTAÇÃO DOS ID's. DA UMA REVISADA AQUI NO SEU CONTROLLER PRA VER SE PRECISA FAZER ALGUMA ALTERAÇÃO, EM RELAÇÃO
#AO INCREMENTO DO ID

