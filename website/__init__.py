from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets11
import pymysql

db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = "helloworld"
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{username}:{password}@{server}/PyroTD".format(username=secrets11.dbuser, password=secrets11.dbpass, server=secrets11.dbhost)
    db.init_app(application)
    
    from .views import views    
    from .auth import auth
    from .apis import apis

    
    application.register_blueprint(views, url_prefix="/")
    application.register_blueprint(auth, url_prefix="/")
    application.register_blueprint(apis, url_prefix="/api/")

    from .models import User
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(application)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return application


# def create_database(app):
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("DB created!")




#  ______   _______   _        _   _        _____   _______
# /  __  \ |  ___  | | |      | | | |      |  ___| |  ___  |
# | |  |_| | |___| | | |      | | | |      | |__   | |   | |
# | | ___  |  ___  | | |      | | | |      |  __|  | |   | |
# | ||_  | | |   | | | |      | | | |      | |     | |   | |
# | |__| | | |   | | | |____  | | | |____  | |___  | |___| |
#  \_____/ |_|   |_| |______| |_| |______| |_____| |_______|
