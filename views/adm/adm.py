from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from modelo import db, Adm, Dados


login_manager_adm = LoginManager()

admrout = Blueprint('admrout',__name__,
                template_folder='templates', static_folder='AdmStatic')


@login_manager_adm.user_loader
def load_user(user_adm):
    return Adm.query.get(int(user_adm.user_id))

#verificar se está logado ou não
def verificarAdm(f):
    def decoraAdm(*args, **kwargs):
        if not current_user.is_authenticated: #caso não for logado vai redirecionar
            return redirect(url_for('admrout.loginadm'))
        return f(*args, **kwargs)
    return decoraAdm

@admrout.route('/loginadm', methods=['POST','GET'], endpoint='loginadm')
def login_adm():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        aceito_adm = Adm.query.filter_by(email=email).first()#esta buscando
        #o primeiro dados a ser visto
        if aceito_adm and aceito_adm.senha == senha:
            login_user(aceito_adm) #passe o objeto completo para o login_user
            #ter aesso total e pegar o id pelo get_id
            return redirect(url_for('admrout.dashboardadm'))
        else:
            flash('Acesso negado')
    return render_template('LoginAdm.html')

@admrout.route('/dashboardadm', methods=['POST','GET'], endpoint='dashboardadm')
@verificarAdm
def dashboard():
    if request.method == 'POST':
            IdUsuario = request.form.get('id_usuario')
            if IdUsuario:
                deleteUsuario = Dados.query.filter(Dados.id == IdUsuario).first()
                if deleteUsuario:
                    db.session.delete(deleteUsuario)
                    db.session.commit()
                else:
                    flash('Erro ao apagar')
    TotalUsuario = Dados.query.count()
    totalAtivo = Dados.query.filter(Dados.is_active == 'True').count()
    dados_usuario = Dados.query.all()
    return render_template('dashboard.html', dados_usuario=dados_usuario,TotalUsuario=TotalUsuario,
                           totalAtivo=totalAtivo)