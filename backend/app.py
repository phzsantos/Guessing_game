from flask import Flask
from flask_session import Session

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['SESSION_TYPE'] = 'filesystem'

    Session(app)

    return app

app = create_app()
