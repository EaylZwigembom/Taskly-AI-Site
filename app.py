from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/integrations")
def integrations():
    return render_template("integrations.html")

@app.route("/early-access")
def early_access():
    return render_template("early-access.html")