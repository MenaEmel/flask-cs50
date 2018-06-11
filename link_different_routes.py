from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_func():
    return render_template("index.html")

@app.route("/more")
def more_func():
    return render_template("more.html")