# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if "__main__" in __name__:
    app.run(debug=True, port=2000)
