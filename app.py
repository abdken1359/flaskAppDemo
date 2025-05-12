from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#Assign database value(db)
db=SQLAlchemy()

#Make the flask app init a function, so that when imported, it does not execute it in a loophole
def create_app():
    app=Flask(__name__,template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///./testdb.db"
    app.secret_key="MYSECRETKEY"
    
    login_manager=LoginManager()
    login_manager.init_app(app)
    db.init_app(app)
    
    #Import User model to get user ids
    from models import User
    
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    #Initialise BCRYPT
    bcrypt=Bcrypt()
    #IMPORTS LATER ON
    from routes import register_routes
    register_routes(app,db,bcrypt)
    migrate = Migrate(app,db)
    
    return app