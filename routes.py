from flask import render_template, request
from models import Person

def register_routes(app,db):
    @app.route("/")
    def index():
        people = Person.query.all()
        return str(people)
    @app.route("/add_someone")
    def add_someone():
        
        new_person=Person(name="Boris",age=29,job="Software engineer")
        db.session.add(new_person)
        db.session.commit()
        people=Person.query.all()
        return str(people)
        
            
    