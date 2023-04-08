from .models import User
from flask import Flask

from os import path
from flask_login import LoginManager
from .database import db

DB_NAME = "experiolearn"


def create_app():
    app = Flask(__name__)
    app.secret_key = 'xyzsdfg'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/experiolearn'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
