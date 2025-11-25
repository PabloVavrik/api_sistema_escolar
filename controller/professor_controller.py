from flask import Blueprint, jsonify, request
import model.professor_model as professor_model

professor_bp = Blueprint('professor_bp', __name__, url_prefix= '/professor')


#####################################################################################
@professor_bp.route('/', methods=['GET'])
def get_professores():
    try:
        professores = professor_model.retornar_professores()
        return jsonify(professores),200
        
    except Exception as e:
        return jsonify({'Erro': f'não foi possivel retornar lista de professores. {e}'}),500
