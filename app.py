from flask import Flask
from flask_restx import Api
from controller.aluno_controller import aluno_ns
from controller.professor_controller import professor_bp


def create_app():
    app = Flask(__name__)

    api = Api(
        app,
        title= "API Faculdade ADS",
        version= "1.0",
        description= "Documentação da API de Alunos e Professores"
    )

   
    api.add_namespace(aluno_ns)
    app.register_blueprint(professor_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug= True)
    