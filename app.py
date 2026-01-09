from flask import Flask
from controller.aluno_controller import aluno_bp
from controller.professor_controller import professor_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(aluno_bp)
    app.register_blueprint(professor_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug= True)
            

