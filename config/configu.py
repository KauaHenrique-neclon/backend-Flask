from modelo import db
import secrets
import os

class configura:
    # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:5115@localhost/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração da chave secreta
    SECRET_KEY = secrets.token_hex(16)  # Chave aleatória

    # Configuração de upload de imagem
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')