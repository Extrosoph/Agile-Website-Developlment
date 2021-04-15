from app import app
from flask import  redirect, url_for, render_template, request, session, flash
from app.models import User, db


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        # if the page is a sign up
        if len(request.form) > 2:
            session.permanent = True
            session['logged_in'] = False
            username = request.form['username']
            email = request.form['email']
            password = request.form["password"]
            current_user_email = User.query.filter_by(email=email).first()
            current_user_username = User.query.filter_by(email=email).first()

            # If username is taken
            if current_user_username is not None:
                flash("The provided username is already taken!")

                # need to fix with jquery
                return render_template("login.html", page='login')

            #If email is already registered
            elif current_user_email is not None:
                flash("The provided email is already registered!")

                # need to fix with jquery
                return render_template("login.html", page='login')

            # Create a new user account and redirect to user.html
            else:
                newUser = User(username=username, email=email, password=password, admin=False)
                db.sessions.add(newUser)
                db.session.commit()

                # Logged them in
                session['logged_in'] = True
                return render_template("user.html", username=username, page='user')

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