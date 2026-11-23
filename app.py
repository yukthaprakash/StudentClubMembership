from flask import flask
@app.route("/")
def home():
    return "hello"