from flask import Blueprint ,render_template, request, redirect, current_app, flash, url_for
from flask_login import LoginManager, current_user, login_user
from flask_sqlalchemy import SQLAlchemy, session
from werkzeug.utils import secure_filename
from modelo import db,Noticias, Dados
import os
from config.configu import *

user = Blueprint('user',__name__,
                template_folder='templates',
                static_folder='Profile_Static')

def usuarioRequest(f):
    def decoraFuncao(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('auth.login')
        return f(*args, **kwargs)
    return decoraFuncao

@user.route('/publicar',methods=['POST','GET'], endpoint='publicar')
@usuarioRequest
def publicar():
    if request.method == 'POST':#ele verifica se a requisição é POST
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')
        if 'imagem' not in request.files:
            return redirect(request.url)
        print(imagem)
        if imagem.filename == '':
            return redirect(request.url)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        ImagemSave = os.path.join(upload_folder,( secure_filename(imagem.filename)))
        if current_user.is_authenticated:
            user_id = current_user.get_id() 
            usuario_dados = Dados.query.filter_by(id=int(user_id)).first()
            imagem.save(ImagemSave)
            publicacao = Noticias(
                titulo = titulo,
                nome = usuario_dados.usuario,
                imagem = imagem.filename,
                descricao = descricao,
                id_user = int(user_id)
                )
            db.session.add(publicacao)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            return print("precisa está longado para publicar")
    return render_template('publicar.html')

@user.route('/deletar', methods=['POST','GET'],endpoint='deletar')
@usuarioRequest
def deletar():
    if request.method == 'POST':
        post_id = request.form.get('id_post')
        if post_id:
            post = Noticias.query.filter(Noticias.id == post_id, 
                            Noticias.id_user == current_user.id).first()
            if post:
                db.session.delete(post)
                db.session.commit()
                flash('Apagado com sucesso')
            else:
                flash('Erro ao apagar')
    noticia = Noticias.query.filter(Noticias.id_user==current_user.id).all()
    return render_template('deletar.html', noticia=noticia)