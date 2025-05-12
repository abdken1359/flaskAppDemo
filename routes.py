from flask import render_template, request
from models import Person

def register_routes(app,db):
    @app.route("/")
    def index():
        people = Person.query.all()
        return render_template("index.html",people=people)
    @app.route("/add_someone",methods=["POST"])
    def add_someone():
        username=request.form.get("username")
        age=int(request.form.get("age"))
        job=request.form.get("job")
        
        
        new_person=Person(name=username,age=age,job=job)
        db.session.add(new_person)
        db.session.commit()
        people=Person.query.all()
        return render_template("index.html",people=people)
        
            
    