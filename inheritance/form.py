from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form_index():
    return render_template("form.html")

@app.route("/hello", methods=["GET", "POST"])
def redirect():
    if request.method == "GET":
        return "<h1>Please submit the form instead.<h1>"
    else:
        name = request.form.get("full-name")
        return render_template("redirect.html", name=name)