# Imports
from flask import Flask, request,render_template 
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="templates")
print(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        myValue="AB Services"
        myResult=3+4
        evenTens=[10,20,30,40,50,60,70,80,90,100]
        return render_template('index.html',myValue=myValue,myResult=myResult,evenTens=evenTens)
    elif request.method=="POST":
        username = request.form.get('username')
        return f"This is a post request {username}",200

@app.route("/other")
def other():
    some_text="Just a text sentence"
    return render_template("other.html",some_text=some_text)

@app.route("/file_upload",methods=["POST"])
def file_upload():
     return "Almost done with the magic"

@app.template_filter("alternate_case")
def alternate_case(s):
    return ''.join([t.upper() if i%2==0 else t.lower() for i,t in enumerate(s)])

if  __name__ == "__main__":
    app.run(debug=True, port=1000,host="0.0.0.0")
