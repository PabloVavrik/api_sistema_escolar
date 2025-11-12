dados = {
    'Professor':[{'id': 1, 
                  'nome': 'Pablo', 
                  'idade': 31, 
                  'materia': 'Fundamentos da natacao', 
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
                  'materia': 'Hermeneutica', 
                  'observacoes': ''}],
        }


def criar_professor(novo_professor):
    try:
        dados['Professor'].append(novo_professor)
        return novo_professor
    except Exception as e:
        raise Exception(f'Erro ao criar professor: {e}')
    

def retornar_professor():
    return dados['Professor']

def retornar_professor_por_id(user_id):
    try:
        for professor in dados['Professor']:
            if professor.get('id') == user_id:
                return professor
    except Exception as e:
        raise Exception(f'Erro ao encontrar professor: {e}')
    

def limpar_campos_professor():
    try:
        for professor in dados['Professor']:
            for campo in list(professor.keys()):
                if campo != 'id':
                    professor[campo] = ''
                return dados['Professor']
    except Exception as e:
        raise Exception(f'Erro ao limpar campos: {e}')
    
def limpar_campos_por_id(user_id, dado):
    try:
        for professor in dados.get('Professor', []):
            if professor.get('id') == user_id:
                for campo in professor.keys():
                    if campo != 'id':
                        professor[campo] = ''
                    return professor
        return None
    except Exception as e:
        raise Exception(f'Erro ao limpar campo do professor: {e}') 