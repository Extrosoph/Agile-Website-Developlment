from app import app
from flask import  redirect, url_for, render_template, request, session, flash
from app.models import User, db
from bcrypt import checkpw


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form['email']
        password = request.form['password']

        # If no email/password is given
        if email == ""  and password == "":
            flash("Need to fill all the fields!")
            return redirect(url_for("login", page='login'))

        else:
            current_user = User.query.filter_by(email=email).first()

            # If the given email does not have an account
            if current_user is None:
                flash("Need to create an account")
                return redirect(url_for("login", page='login'))

            # Check if the given password is correct
            else:
                if checkpw(request.form['password'].encode(), current_user.password) == False:
                    flash("Incorrect password given!")
                    return redirect(url_for("login", page='login'))
                else:
                    session['logged_in'] = True
                    return render_template("user.html", page='user', user=current_user)
    else:
       return render_template("login.html", page='login')

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        session.permanent = True
        username = request.form['username']
        email = request.form['email']
        password = request.form["password"]

        # If no email/username/password
        if email == "" and username == "" and password == "":
            flash("Need to fill all the fields!")
            return redirect(url_for("signup", page='signup'))

        else :
            current_user_email = User.query.filter_by(email=email).first()
            current_user_username = User.query.filter_by(username=username).first()

            # If username is taken
            if current_user_username is not None:
                flash("The provided username is already taken!")
                return redirect(url_for("signup", page='signup'))

            # If email is already registered
            elif current_user_email is not None:
                flash("The provided email is already registered!")
                return redirect(url_for("signup", page='signup'))

            # Create a new user account and redirect to user.html
            else:
                newUser = User(username=username, email=email, password=password)
                db.session.add(newUser)
                db.session.commit()

                # Logged them in and redirect to the user html
                session['logged_in'] = True
                return render_template("user.html", username=username, page='user')

    else:
        return render_template("signup.html", page=signup)

@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("logged_in", None)
    return redirect(url_for("login", page='login'))