from flask_restx import Namespace, Resource, fields
import model.aluno_model as aluno_model


aluno_ns = Namespace(
    'alunos',
    description= 'Operacoes relacionadas a alunos'
)


#==================================================================================================================================


aluno_model_swagger = aluno_ns.model('Aluno',{
    'nome': fields.String(required=True, description= 'Nome do aluno'),
    'idade': fields.Integer(required=True, description= 'Idade do aluno')
})

aluno_response_model = aluno_ns.model('AlunoResponse', {
    'id': fields.Integer(description='Id do aluno'),
    'nome': fields.String(description='Nome do aluno'),
    'idade': fields.Integer(description='Idade do aluno')
})

aluno_patch_model = aluno_ns.model('AlunoPatch',{
    'nome': fields.String(description='Nome do aluno'),
    'idade': fields.Integer(description='Idade do aluno')
})


#==================================================================================================================================


@aluno_ns.route('/')   
class AlunoList(Resource):
    @aluno_ns.marshal_list_with(aluno_response_model)             #GET
    def get(self):   
        alunos = aluno_model.retornar_aluno()
        return alunos, 200
    


    @aluno_ns.expect(aluno_model_swagger, validate=True)
    @aluno_ns.marshal_with(aluno_response_model, code=201)        #POST
    def post(self):     
        dados = aluno_ns.payload
        aluno_criado = aluno_model.criar_aluno(dados)
        return aluno_criado, 201


#==================================================================================================================================

@aluno_ns.route('/<int:id>')    
class AlunoResource(Resource):
    @aluno_ns.marshal_with(aluno_response_model)
    @aluno_ns.response(200, 'Aluno encontrado')
    @aluno_ns.response(404, 'Aluno não encontrado')                #GET por ID
    def get(self, id):      #GET POR ID
        aluno= aluno_model.retornar_aluno_por_id(id)
        if not aluno:
            aluno_ns.abort(404, 'Aluno não encontrado')
        return aluno
    


    @aluno_ns.expect(aluno_patch_model, validate= True)
    @aluno_ns.marshal_with(aluno_response_model)
    @aluno_ns.response(200, 'Aluno atualizado!')
    @aluno_ns.response(400, 'Dados invalidos')
    @aluno_ns.response(404, 'Aluno nao encontrado')                 #PATCH
    def patch(self, id):

        dados = aluno_ns.payload

        if not dados:
            aluno_ns.abort(400, 'Nenhum dado enviado para atualizacao')

        aluno_atualizado = aluno_model.atualizar_aluno_por_id(id, dados)

        if not aluno_atualizado:
            aluno_ns.abort(404, 'Aluno nao encontrado!')

        return aluno_atualizado, 200


    
    @aluno_ns.response(204, 'Aluno deletado!')                      #DELETE
    @aluno_ns.response(404, 'Aluno nao encontrado')
    def delete(self, id):
        aluno_deletado = aluno_model.deletar_aluno_por_id(id)

        if not aluno_deletado:
            aluno_ns.abort(404, 'Aluno nao encontrado!')
        
        return '', 204
    