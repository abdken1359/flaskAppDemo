# Imports
from flask import Flask, request,render_template ,send_from_directory,session,make_response
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")
app.config["UPLOAD_FOLDER"]="uploads/"
app.secret_key="MYKEY"
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        myValue="AB Services"
        myResult=3+4
        evenTens=[10,20,30,40,50,60,70,80,90,100]
        return render_template('index.html',myValue=myValue,myResult=myResult,evenTens=evenTens)
  
@app.route("/set_session")
def set_session():
    session["name"]="Abdiel"
    session["age"]=18
    return render_template("index.html",message="Session data")
@app.route("/get_session")
def get_session():
    name=session["name"]
    age=session["age"]
    return render_template("index.html",message=f"Hi, my name is {name}, and I am {age}")
     

@app.template_filter("alternate_case")
def alternate_case(s):
    return ''.join([t.upper() if i%2==0 else t.lower() for i,t in enumerate(s)])

if  __name__ == "__main__":
    app.run(debug=True, port=1000,host="0.0.0.0")
