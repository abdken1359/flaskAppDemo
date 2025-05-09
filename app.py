# Imports
from flask import Flask, Request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return'<h1 style="color:green">Hello World!</h1>',201
@app.route("/hi/<int:number1>/<int:number2>")
def hi(number1,number2):
    return f'{number1} + {number2} = {number1+number2}',200
if "__main__" == __name__:
    app.run(debug=True, port=1000,host="0.0.0.0")
