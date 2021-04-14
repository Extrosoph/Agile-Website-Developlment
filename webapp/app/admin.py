from webapp1 import app
from flask import  redirect, url_for, render_template, request, session, flash


@app.route("/admin")
def admin():
    return render_template("admin.html", page='admin')