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


#--------------------------------------------------------------
#ROTAS PARA POST DE /ALUNOS


@app.route('/Alunos', methods= ['POST'])
def criar_aluno():
    try:
        novo_aluno = request.get_json()
        if not novo_aluno:
            return jsonify({'mensagem': 'Não foi possível criar um novo aluno!'}), 400
       
        campos_obrigatorios = ['nome', 'idade']
        for campo in campos_obrigatorios:
            if campo not in novo_aluno or not novo_aluno[campo]:
                return jsonify({'erro': f'campo {campo} obrigatório!'}), 400
        
        dados['Aluno'].append(novo_aluno)
        return jsonify({'mensagem': 'Aluno adicionado com sucesso!',
                        'Novo aluno': novo_aluno}), 201
    
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao criar o aluno: {e}'}), 500

#--------------------------------------------------------------
#ROTA PARA PUT DE /ALUNOS

@app.route('/Alunos', methods= ['PUT'])
def limpar_campos_aluno():
    dados['Aluno'] = [{
        'nome': '',
        'idade': ''
        }]
    return jsonify({'mensagem': 'Os campos foram limpos com sucesso!',
                    'Alunos': dados['Aluno']}), 200


@app.route('/Alunos/<int:user_id>', methods= ['PATCH'])
def atualizar_aluno_por_id(user_id):
    try:
        nova_informacao = request.get_json()
        if not nova_informacao:
            return jsonify({'mensagem': 'Não há novas informações!'}), 400
        
        for aluno in dados['Aluno']:
            if aluno['id'] == user_id:
                aluno.update(nova_informacao)
                return jsonify({'mensagem': 'Aluno atualizado com sucesso!',
                                'Aluno': aluno}), 200
    
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao atualizar o aluno',
                        'erro': str(e)}), 500


#--------------------------------------------------------------
#ROTAS PARA DELETE DE /ALUNOS

@app.route('/Alunos/<int:user_id>', methods= ['DELETE'])
def deletar_aluno_por_id(user_id):
    try:
        for i, aluno in enumerate(dados['Aluno']):
            if aluno['id'] == user_id:
                dados['Aluno'].pop(i)
                return jsonify({'mensagem': 'Aluno deletado com sucesso!'}), 200
        return jsonify({'mensagem': 'Aluno não encontrado!'}), 404
        
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao deletar aluno!',
                        'erro': str(e)}), 500






if __name__ == '__main__':
    app.run(debug= True)
