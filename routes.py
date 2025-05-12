from flask import render_template, request,redirect
from models import User
from flask_login import login_user, logout_user,current_user

def register_routes(app,db,bcrypt):
    @app.route("/")
    def index():
        return render_template("index.html")
        
    @app.route("/signup",methods=["GET","POST"])
    def signup():
        if request.method=="GET":
            return render_template("signup.html")
        if request.method=="POST":
            username=request.form.get("username")
            password=request.form.get("password")
            hashed_password=bcrypt.generate_password_hash(password)
            user=User(username=username,password=hashed_password,role="user")
            db.session.add(user)
            db.session.commit()
            return redirect(f"/user/{username}")
    @app.route("/login",methods=["GET","POST"])
    def login():
       if request.method=="GET":
           return render_template("login.html")
       if request.method=="POST":
           pass
    
    @app.route("/user/<string:username>")
    def user(username):
        return render_template("userDashboard.html", username=username)
    @app.route("/logout")
    def logout():
        logout_user()
        return "successfully logout!",200