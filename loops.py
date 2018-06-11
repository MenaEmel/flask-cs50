from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_list():
    names = ["Mina", "Emil", "Fawzy"]
    return render_template("loop.html", names=names)