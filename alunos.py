from flask import Flask, jsonify, request

app = Flask(__name__)


dados = {'Professor':[{'id': 1, 'nome': 'Pablo', 'idade': 31, 'materia': 'Fundamentos da natacao', 'observacoes': ''}],
         'Aluno':[{'id': 1, 'nome': 'Stephanie', 'idade': 25}],
         'Turma': [{'id': 1, 'periodo': 'manha'}]
         }

#--------------------------------------------------------------
#ROTAS PARA GET DE /ALUNOS

@app.route("/Alunos", methods = ['GET'])
def retornar_alunos():
    try:
        alunos = dados['Aluno']
        if alunos:
            return jsonify({'mensagem': 'Esta é a lista de alunos',
                            'alunos': alunos}), 200
        else: 
            return jsonify({'mensagem': 'Nenhum aluno foi encontrado!'}), 404
    except Exception as e:
        return jsonify({'mensagem': f'Não foi possível retornar a lista de Alunos!',
                        'erro': f'Erro: {e}'}), 500
    

#retornar aluno por ID
@app.route('/Alunos/<int:user_id>', methods = ['GET'])
def retornar_aluno_id(user_id):
    try:
        alunos = dados['Aluno']
        for aluno in alunos:
            if aluno['id'] == user_id:
                return jsonify({'mensagem': 'O aluno encontrado',
                                'aluno': aluno}), 200
        return jsonify({'mensagem': 'Não foi possível encontrar o aluno com este id!'}), 404 
    except Exception as e:
        return jsonify({'mensagem': 'Erro na requisição!',
                        'erro': str(e)}), 500


