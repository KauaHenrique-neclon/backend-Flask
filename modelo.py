from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class Dados(db.Model , UserMixin):
    __tablename__ = 'dados'
    id = db.Column(db.Integer,primary_key=True)
    usuario = db.Column(db.String(30),nullable=False)
    senha = db.Column(db.String(20),nullable=False)
    is_active = db.Column(db.Boolean, default=True)#Por padrão, o usuário está ativo ou esta desativado
    noticias = db.relationship('Noticias', backref='author', lazy=True, primaryjoin="Dados.id == Noticias.id_user")

    def __init__(self, usuario, senha,is_active, id):
        self.usuario = usuario
        self.senha = senha
    
    def get_id(self): #passa para que Flask-login acesse ele para obter o id
        return self.id
    
    def __repr__(self):
        return f"Dados('{self.usuario}')"

class Noticias(db.Model):
    __tablename__ = 'noticias'
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(20),nullable=False)
    nome = db.Column(db.String(20),nullable=False)
    data_publicacao = db.Column(db.Date,default=datetime.date.today)
    imagem = db.Column(db.String(255),nullable=True)
    descricao = db.Column(db.String(256),nullable=False)
    id_user = db.Column(db.Integer,db.ForeignKey('dados.id'),nullable=False)

    def __repr__(self):
        return f"Noticias('{self.titulo}', '{self.nome}')"
    
class Adm(db.Model):
    __tablename__ = 'adm'
    id_adm = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),unique=True,nullable=False)
    senha = db.Column(db.String(30),nullable=False)

    def get_id(self):
        return str(self.id_adm)  #o user sempre vai pedir o get_id
                                #passa esse get_id para retornar um valor

    def is_active(self):
        return True #essa merda de model sempre vai pedir o is_active
                    #para evitar cor de cabeça, passe como true

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Adm('{self.email}','{self.senha}')"