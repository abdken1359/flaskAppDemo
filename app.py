#Imports
from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
@app.route('/')
def index():
    return "Testing 123"

if "__main__" in __name__:
    app.run(debug=True,port=2000)