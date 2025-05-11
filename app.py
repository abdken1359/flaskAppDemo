from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Assign database value(db)
db=SQLAlchemy()

#Make the flask app init a function, so that when imported, it does not execute it in a loophole
def create_app():
    app=Flask(__name__,template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///./testdb.db"
    db.init_app(app)
    
    #IMPORTS LATER ON
    from routes import register_routes
    register_routes(app,db)
    Migrate(app,db)
    
    return app