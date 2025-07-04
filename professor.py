from flask import Flask, jsonify, request


app = Flask(__name__)

dados = {'Professor':[{'id': 1, 'nome': 'Pablo', 'idade': 31, 'materia': 'Fundamentos da natacao', 'observacoes': ''}],
         'Aluno':[{'id': 1, 'nome': 'Stephanie', 'idade': 25}],
         'Turma': [{'id': 1, 'periodo': 'manha'}]
         }




#Rotas para o POST de /Professor
@app.route('/Professor', methods = ['POST'])
def criar_professor():
    novo_professor = request.get_json()
    
    if not novo_professor or 'id' not in novo_professor or 'nome' not in novo_professor: 
        return jsonify({'mensagem': 'Erro. Dados incompletos'}), 400
    for professor in dados['Professor']:
        if professor['id'] == novo_professor['id']:
            return jsonify({'mensagem': 'Id já existente.'}), 409
    
    dados['Professor'].append(novo_professor)
    return jsonify({'mensagem': 'Professor criado com sucesso!!!',
                    'professor': novo_professor
                    }), 201
    
    


#------------------------------------------------------------------

#Rotas para o GET de /Professor
@app.route('/Professor', methods = ['GET'])
def retornar_professor():
    professor = dados
    return jsonify(professor['Professor']), 200

#POR ID
@app.route('/Professor/<int:user_id>', methods = ['GET'])
def retornar_professor_por_id(user_id):
    for professor in dados['Professor']:
        if professor['id'] == user_id:
            return jsonify(professor), 200
    return jsonify({f'Erro ao procurar o professor: {user_id}'}), 404
              
#------------------------------------------------------------------

#ROTA para UPDATE de /Professor
@app.route('/Professor', methods = ['PUT'])
def limpar_campos_professor():
    dados['Professor'] = [{
        'id': '',
        'nome' : '',
        'idade': '',
        'materia': '',
        'observacoes': ''
    }]
    return jsonify({'mensagem':'Campos de Professor foram resetados!', 'Professor': dados['Professor']}), 200

@app.route('/Professor/<int:user_id>', methods = ['PUT'])
def limpar_campos_professor_por_id(user_id):
    
    for professor in dados['Professor']:
        if professor['id'] == user_id:
            professor.update({
                'nome': '',
                'idade': '',
                'materia': '',
                'observacoes': ''
            })
            return jsonify({'mensagem': f'Campos do Professor {user_id} foram resetados!', 
                    'Professor': professor}), 200
    return jsonify({'mensagem': f'Erro ao tentar resetar o professor de id {user_id}!'}), 404

@app.route('/Professor/<int:user_id>', methods = ['PATCH'])
def atualizar_professor_por_id(user_id):
    dados_atualizados = request.get_json()
    
    if not dados_atualizados:
        return jsonify({'mensagem' : 'Não há dados para atualizar!'}), 400
    
    for professor in dados['Professor']:
        if professor['id'] == user_id:
            for chave in dados_atualizados:
                if chave in professor:
                    professor[chave] = dados_atualizados[chave]
            return jsonify({
                'mensagem': 'Dados atualizados com sucesso!', 
                'mensagem': professor
                }), 200
   
    return jsonify({f'O Professor {user_id} não pode ser atualizado'}), 404 
        

#------------------------------------------------------------------

#ROTA PARA DELETE de /Professor

@app.route('/Professor/<int:user_id>', methods = ['DELETE'])
def deletar_professor_por_id(user_id):

    for i, professor in enumerate(dados['Professor']):
        if professor['id'] == user_id:
            dados['Professor'].pop(i)
            return jsonify({'mensagem': f'O professor {user_id} foi deletado com sucesso!'}), 200
    
    return jsonify({'mensagem': f'Erro ao tentar deletar o professor {user_id}!'}), 404


if __name__ == '__main__':
    app.run(debug= True)