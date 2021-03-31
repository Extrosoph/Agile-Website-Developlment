from webapp import app
from flask import  redirect, url_for, render_template, request, session, flash

@app.route("/")
def home():
    return render_template("home.html", page='home')

@app.route("/user")
def user():
    return render_template("user.html", page='user')

@app.route("/login")
def login():
    return render_template("login.html", page='login')

@app.route("/admin")
def admin():
    return render_template("admin.html", page='admin')

@app.route("/statistics")
def statistic():
    return render_template("statistics.html", page='statistics')

@app.route("/assessment")
def assessment():
    return render_template("assessment.html", page='assessment')
