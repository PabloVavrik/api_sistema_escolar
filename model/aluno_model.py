from flask import Flask, jsonify, request

dados = {
    'Aluno' : [
        { 'id': 1, 'nome': 'Stephanie', 'idade': 25},
        {'id': 2, 'nome': 'Pablo', 'idade': 31},
        {'id': 3, 'nome': 'Yago', 'idade': 30}
        ]
}

def retornar_aluno():
    return dados['Aluno']


def retornar_aluno_por_id(user_id):
    for aluno in dados['Aluno']:
        if aluno.get('id') == user_id:
            return aluno
        return None
    
def criar_aluno(novo_aluno):
    try:
        dados['Aluno'].append(novo_aluno)
        return novo_aluno
    except Exception as e:
        raise Exception(f'Erro ao criar um novo aluno {e}')
    

def limpar_campos_alunos():
    try:
        for aluno in dados['Aluno']:
            for campo in list(aluno.keys()):
                if campo != 'id':
                    aluno[campo] = ''
        return dados['Aluno']
    except Exception as e:
        raise Exception(f'Erro ao limpar os campos de aluno {e}')
    
def atualizar_aluno_por_id(user_id, nova_informacao):
    try:
        for aluno in dados['Aluno']:
            if aluno.get('id') == user_id:
                aluno.update(nova_informacao)
        return aluno
    except Exception as e:
        raise Exception(f'Erro ao atualizar aluno {e}')
    

def deletar_aluno_por_id(user_id):
    for aluno in dados['Aluno']:
        if aluno.get('id') == user_id:
            dados['Aluno'].remove(aluno)
            return True
    return False