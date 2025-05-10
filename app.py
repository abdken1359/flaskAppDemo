# Imports
from flask import Flask, request,render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="templates")
print(__name__)

@app.route("/")
def home():
    myValue="AB Services"
    myResult=3+4
    evenTens=[10,20,30,40,50,60,70,80,90,100]
    return render_template('index.html',myValue=myValue,myResult=myResult,evenTens=evenTens)
@app.route("/other")
def other():
    some_text="Just a text sentence"
    return render_template("other.html",some_text=some_text)

if  __name__ == "__main__":
    app.run(debug=True, port=1000,host="0.0.0.0")
