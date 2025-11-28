from flask import Blueprint, jsonify, request
import model.professor_model as professor_model

professor_bp = Blueprint('professor_bp', __name__, url_prefix= '/professor')



@professor_bp.route('', methods=['GET'])
def get_professores():
    try:
        professores = professor_model.retornar_professores()
        return jsonify({'professores': professores}),200
        
    except Exception as e:
        return jsonify({'erro': 'não foi possivel retornar lista de professores.',
                        'detalhes': str(e)}),500


@professor_bp.route('/<int:user_id>', methods=['GET'])
def get_professor_id(user_id):
    try:
        professor = professor_model.retornar_professor_por_id(user_id)

        if professor is None:
            return jsonify({'erro': 'Professor não encontrado'}), 404
        
        return jsonify({'professor': professor}),200
    
    except Exception as e:
        return jsonify({'erro': 'Erro interno ao tentar buscar professor',
                        'detalhes': str(e)}), 500
    

@professor_bp.route('/limpar', methods=['POST'])
def limpar_campos_professor():

    try:
        campos_limpos = professor_model.limpar_campos_professores()
        return jsonify({'resultado': campos_limpos}),200
    
    except Exception as e:
        return jsonify({'eroo': 'Não foi possível realizar operação',
                        'detalhes': str(e)}), 500
    

@professor_bp.route('/<int:user_id>', methods=['PATCH'])
def atualizar_professor(user_id):
    try:
        dados = request.get_json()
        professor_atualizado = professor_model.atualizar_prof_por_id(user_id, dados)

        if professor_atualizado is None:
            return jsonify({'erro': 'Professor não encontrado.'}), 404
        
        return jsonify({'Professor atualizado:': professor_atualizado}),200
    
    except Exception as e:
        return jsonify({'erro': 'Erro ao tentar atualizar professor.',
                        'detalhes': str(e)}), 500


@professor_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_professor(user_id):
    try:
        professor_deletado = professor_model.deletar_professor(user_id)

        if professor_deletado:
            return jsonify({'mensagem': 'Professor deletado com sucesso!'}),200
       
        return jsonify({'erro': 'Professor não encontrado!'}),404
        
    except Exception as e:
        return jsonify({'erro': 'Erro ao tentar deletar professor.',
                        'detalhe': str(e)}),500

       
    

