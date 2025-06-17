from flask import Flask, jsonify, request

app = Flask(__name__)

dados = {'Professor':[{'id': 1, 'nome': 'Pablo', 'idade': 31, 'materia': 'Fundamentos da natacao', 'observacoes': ''}],
         'Aluno':[{'id': 1, 'nome': 'Stephanie', 'idade': 25}],
         'Turma': [{'id': 1, 'periodo': 'manha'}]
         }



#CREATE
def criar_professor(novo_professor):
    dados['Professor'].append(novo_professor)
    return dados['Professor']

#READ
def retornar_professor():
    return dados['Professor']

def retornar_professor_id(id):
    for professor in dados['Professor']:
        if professor['id'] == id:
            return professor
    return None

#UPDATE
def atualizar_professor(id, atualiza_professor):
    for professor in dados['Professor']:
        if professor['id'] == id:
            professor.update(atualiza_professor)
            return professor['id']
        return False 

#DELETE
def deleta_professor(id):
    try:
        if 'Professor' not in dados:
            raise KeyError("Chave 'Professor' não encontrada nos dados!")
        
        for i, professor in enumerate(dados['Professor']):
            if professor['id'] == id:
                dados['Professor'].pop(i)
                return True
        return False
    except KeyError as e:
        print(f'Erro ao deletar professor: {e}')
        return False
    

#___________________________________________________________________________________________________________________

#Rotas para o POST de /Professor
@app.route('/Professor', methods = ['POST'])
def create_professor():
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
def get_professor():
    professor = dados
    return jsonify(professor['Professor']), 200

#POR ID
@app.route('/Professor/<int:user_id>', methods = ['GET'])
def get_professor_id(user_id):
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

if __name__ == '__main__':
    app.run(debug= True)
            

