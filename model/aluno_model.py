from flask import Flask, jsonify

dados = {
    'Aluno' : [
        { 'id': 1, 'nome': 'Stephanie', 'idade': 25}
        ]
}

def retornar_aluno():
    return dados['Aluno']


def retornar_aluno_por_id(user_id):
    for aluno in dados['Aluno']:
        if aluno == user_id:
            return aluno
        return jsonify({'mensagem':'Id não encontrado'}), 500
    
