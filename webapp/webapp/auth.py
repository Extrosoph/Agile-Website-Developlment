from webapp import app
from flask import  redirect, url_for, render_template, request, session, flash

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        # if the page is a sign up
        if len(request.form) > 2:
            session.permanent = True
            session['logged_in'] = False
            username = request.form['username']
            email = request.form['email']

            # Check if there is another user with the same email and/or username
            # If true flash already used for both email and username
            password = request.form['password']
            return render_template("user.html", user=username)

        # if the page is a login
        else:
            session.permanent = True
            session['logged_in'] = True
            email = request.form['email']
            password = request.form['password']

            #Check if user is an admin or not
            #Check if user input the correct password
            #If true flash incorrect password
            #Check if the user input incorrect email
            #If true flash incorrect email
            #If empty flash need input
            return render_template("user.html", page='user', user=email)

    else:
       return render_template("login.html", page='login')

@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("logged_in", None)
    return redirect(url_for("login", page='login'))