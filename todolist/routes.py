from flask import render_template
from todolist import app, db
from todolist.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")