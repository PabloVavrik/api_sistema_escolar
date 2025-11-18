from flask import Flask
from controller.aluno_controller import aluno_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(aluno_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug= True)
            

