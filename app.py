from flask import Flask, current_app
from views.auth.login import auth , login_manager
from views.profiles.user import user
from views.adm.adm import admrout , login_manager_adm
from config.configu import configura
from modelo import db


def CriandoApp():
    app = Flask(__name__)
    # carregando as configurações
    app.config.from_object(configura)
    app.config['UPLOAD_FOLDER'] = 'upload'
    db.__init__(app)

    # carregando os blueprint
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(admrout)

    login_manager_adm.init_app(app)
    login_manager_adm.login_view = 'admrout.loginadm'

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' 

    return app



app = CriandoApp()
if __name__ == '__main__':
    app.run(debug=True)