from webapp import app
from flask import  redirect, url_for, render_template, request, session, flash

@app.route("/login")
def login():
    # if request.method == "POST":
    #
    #     if the page is a sign up
    #     if request.form['h1'] == "Sign Up":
    #
    #     if the page is a login
    #     else:
    #           session.permanent = True
    #           given_email = request.form['email']
    #           given_password = request.form['password']
    #           session["email"] = given_email
    #           current_user = users.query.filter_by(email=given_email).first()
    #           if current_user is not None and current_user.password == given_password:
    #               session["email"] = current_user.email
    #               session['logged_in'] = True
    #               session["username"] = current_user.username
    #               return render_template("account.html", username=current_user.username, page='account')
    #           elif current_user is not None and current_user.password != given_password:
    #               flash('Incorrect Password')
    #               return render_template("login.html", page='login')
    #           else:
    #               flash('Need to create an account')
    #               return render_template("login.html", page='login')
    # else:
    #    return render_template("login.html", page='login')

    return render_template("login.html", page='login')