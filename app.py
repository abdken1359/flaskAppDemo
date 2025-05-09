# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return'<h1 style="color:green">Hello World!</h1>',201


if "__main__" in __name__:
    app.run(debug=True, port=1000,host="0.0.0.0")
