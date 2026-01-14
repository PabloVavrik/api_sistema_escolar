from flask_restx import Namespace, Resource, fields 
import model.professor_model as professor_model


professor_ns = Namespace(
    'Professores',
    description= 'Operacoes relacionadas a professores'
)

#==================================================================================================================================

professor_response_model = professor_ns.model('ProfessorResponse',{
    'id' : fields.Integer(description= 'Id do professor'),
    'nome': fields.String(description= 'Nome do professor'),
    'idade': fields.Integer(description= 'Idade do professor'),
    'materia': fields.String(description= 'Materia que o professor leciona'),
    'observacoes': fields.String(description= '')
})



professor_model_swagger = professor_ns.model('Professor', {
    'nome': fields.String(required= True, description= 'Nome do professor'),
    'idade': fields.Integer(required=True, description= 'Idade do professor'),
    'materia': fields.String(required=True, description= 'Materia que o professor leciona'),
    'observacoes': fields.String(required=True, description= '')
})



professor_patch_model = professor_ns.model('ProfessorPatch', {
    'nome': fields.String(description= 'Nome do professor'),
    'idade': fields.Integer(description= 'Idade do professor'),
    'materia': fields.String(description= 'Materia que o professor leciona'),
    'observacoes': fields.String(description= '')
})

#==================================================================================================================================

@professor_ns.route('/')
class ProfessorList(Resource):
    @professor_ns.marshal_list_with(professor_response_model)               #GET
    def get(self):
        professores = professor_model.retornar_professores()
        return professores, 200


    @professor_ns.expect(professor_model_swagger, validate=True)            #POST
    @professor_ns.marshal_with(professor_response_model, code=201)
    def post(self):

        dados = professor_ns.payload
        novo_professor = professor_model.criar_professor(dados)
        
        return novo_professor, 201

#==================================================================================================================================

@professor_ns.route('/<int:id>')                                            #GET por Id
class ProfessorResource(Resource):
    @professor_ns.marshal_with(professor_response_model)
    @professor_ns.response(200, 'Professor encontrado')
    @professor_ns.response(404, 'Professor não encontrado')
    def get(self, id):
        
        professor = professor_model.retornar_professor_por_id(id)
        if not professor:
            professor_ns.abort(404, 'Professor não encontrado')
        return professor, 200


    @professor_ns.marshal_with(professor_response_model)     #PATCH
    @professor_ns.expect(professor_patch_model, validate= True)
    @professor_ns.response(200, 'Campo atualizado')
    @professor_ns.response(400, 'Dados invalidos')
    @professor_ns.response(404, 'Professor nao contrado')
    def patch(self, id):
        dados = professor_ns.payload
        professor_atualizado = professor_model.atualizar_prof_por_id(id, dados)

        if not any(dados.values()):
            professor_ns.abort(400, 'Informe ao menos um dos campos: nome, idade, materia ou observacoes')
        return professor_atualizado, 200
    
    
    
    @professor_ns.response(204, 'Professor deletado')                       #DELETE
    @professor_ns.response(400, 'Erro ao deletar professor')
    def delete(self, id):
        professor_deletado = professor_model.deletar_professor(id)
        if not professor_deletado:
            professor_ns.abort(404, 'Professor nao encontrado')
        return '', 204



