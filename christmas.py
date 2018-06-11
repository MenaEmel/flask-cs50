import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def is_christmas():
    today = datetime.datetime.now()
    new_year = today.month == 1 and today.day == 1
    return render_template("christmas.html", new_year=new_year)
