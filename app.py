from flask import Flask, render_template
application = Flask(__name__)

# Default Route == same as index.html
@application.route("/")
def hello_world():
    return 'Hello, World!'

@application.route("/david")
def hello_david():
    return "Hello, David!"

# Making the app dynamic. e.g., for any string passed not just david, the content should appear as Hello, name

@application.route("/<string:name>")
def hello_all(name):
    return "<h1>Hello, {}<h1>".format(name[0].upper() + name[1:])


# P.S: For Flask to render test.html, it must be placed in a subdirectory named "templates" which is on the same level as the Flask application
# Note: This is rendering a static web page
@application.route("/test")
def view_test_page():
    return render_template("test.html")

# Example rendering a dynamic web page
@application.route("/dynamic")
def view_dynamic_page():
    x = "Let's Roll"
    return render_template("variable.html", headline=x)