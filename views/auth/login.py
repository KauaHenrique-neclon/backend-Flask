from flask import Blueprint ,render_template, request, redirect,flash
from flask_login import LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy, session
from modelo import db, Noticias, Dados
from config.configu import configura

login_manager = LoginManager()


auth = Blueprint('auth',__name__,
                template_folder='templates', static_folder='Auth_Static')

@login_manager.user_loader
def load_user(user_dados):
    return Dados.query.get(int(user_dados))

@auth.route('/',methods=['POST','GET'], endpoint='index')
def index():
    if current_user.is_authenticated:
        is_admin = current_user.is_active
    else:
        is_admin = False
    dados = Noticias.query.all()
    return render_template('index.html',dados=dados, usuario=current_user)

@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        nome_usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        user_dados = Dados.query.filter_by(usuario=nome_usuario).first()
        if user_dados and user_dados.senha == senha and user_dados.is_active:
            login_user(user_dados)
            return redirect('/')
        else:
            print("erro na senha")
    return render_template('login.html')