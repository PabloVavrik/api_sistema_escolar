dados = {
    'Professor':[{'id': 1, 
                  'nome': 'Pablo', 
                  'idade': 31, 
                  'materia': 'Fundamentos da natação', 
                  'observacoes': ''},
                  {'id': 2, 
                  'nome': 'Giovanni', 
                  'idade': 33, 
                  'materia': 'Matemática Aplicada', 
                  'observacoes': ''},
                  {'id': 3, 
                  'nome': 'Flávio', 
                  'idade': 63, 
                  'materia': 'Geometria básica', 
                  'observacoes': ''},
                  {'id': 4, 
                  'nome': 'Sandra', 
                  'idade': 56, 
                  'materia': 'Hermenêutica', 
                  'observacoes': ''}],
        }


def gerar_novo_id():
    if len(dados['Professor']) == 0:
        return 1
    ultimo_id = dados['Professor'][-1]['id'] 
    return ultimo_id +1


#CREATE
def criar_professor(novo_professor):
    try:
        novo_id = gerar_novo_id()
        novo_professor['id'] = novo_id
        dados['Professor'].append(novo_professor)
        return novo_professor
    except Exception as e:
        raise Exception(f'Erro ao criar professor. Erro: {e}')
    

#READ
def retornar_professores():
    return dados['Professor']

#READ (por Id)
def retornar_professor_por_id(user_id):
    try:
        for professor in dados['Professor']:
            if professor.get('id') == user_id:
                return professor
        return False
    except Exception as e:
        raise Exception(f'Erro ao encontrar professor. Erro: {e}')
    

#UPDATE
def limpar_campos_professores():
    try:
        for professor in dados['Professor']:
            for campo in list(professor.keys()):
                if campo != 'id':
                    professor[campo] = ''
                return dados['Professor']
        return False
    except Exception as e:
        raise Exception(f'Erro ao limpar campos. Erro: {e}')
    

#PATCH
def limpar_campos_professor_por_id(user_id):
    try:
        for professor in dados.get('Professor', []):
            if professor.get('id') == user_id:
                for campo in professor.keys():
                    if campo != 'id':
                        professor[campo] = ''
                    return professor
        return False
    except Exception as e:
        raise Exception(f'Erro ao limpar campo do professor. Erro: {e}') 
    

#PATCH
def atualizar_prof_por_id(user_id, dado):
    try:
        for professor in dados['Professor']:
            if professor.get('id') == user_id:
                professor.update(dado)
                return professor
        return False
    except Exception as e:
        raise Exception(f'Não foi possível atualizar professor. Erro: {e}')
    

#DELETE (Por Id)
def deletar_professor(user_id):
    try:    
        professor_encontrado = next(
                (p for p in dados['Professor'] if p.get('id') == user_id), None)
        if professor_encontrado: 
            dados['Professor'].remove(professor_encontrado)
            return dados['Professor']
        return False
    except Exception as e:
        raise Exception(f'Erro ao deletar professor. Erro: {e}')