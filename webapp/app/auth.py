from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import User, db
from bcrypt import checkpw

login_bp = Blueprint('login_bp', __name__)
signup_bp = Blueprint('signup_bp', __name__)
logout_bp = Blueprint('logout_bp', __name__)

@login_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form['email']
        password = request.form['password']

        current_user_email = User.query.filter_by(email=email).first()
        current_user_username = User.query.filter_by(username=email).first()

        # If the given email does not have an account
        if current_user_email is None and current_user_username is None:
            flash("Need to create an account")
            return redirect(url_for("login_bp.login", page='login'))

        # Check if the given password is correct
        else:
            if current_user_email is not None and checkpw(request.form['password'].encode(), current_user_email.password) == True:
                session['logged_in'] = True
                return render_template("user.html", page='user', user=current_user_email)

            elif current_user_username is not None and checkpw(request.form['password'].encode(), current_user_username.password) == True:
                session['logged_in'] = True
                return render_template("user.html", page='user', user=current_user_username)

            else:
                flash("Incorrect password given!")
                return redirect(url_for("login_bp.login", page='login'))
    else:
       return render_template("login.html", page='login')

@signup_bp.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        session.permanent = True
        username = request.form['username']
        email = request.form['email']
        password = request.form["password"]

        current_user_email = User.query.filter_by(email=email).first()
        current_user_username = User.query.filter_by(username=username).first()

        # If username is taken
        if current_user_username is not None:
            flash("The provided username is already taken!")
            return redirect(url_for("signup_bp.signup", page='signup'))

        # If email is already registered
        elif current_user_email is not None:
            flash("The provided email is already registered!")
            return redirect(url_for("signup_bp.signup", page='signup'))

        # Create a new user account and redirect to user.html
        else:
            newUser = User(username=username, email=email, password=password)
            db.session.add(newUser)
            db.session.commit()

            # Logged them in and redirect to the user html
            session['logged_in'] = True
            return render_template("user.html", username=username, page='user')

    else:
        return render_template("signup.html", page='signup')

@logout_bp.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("logged_in", None)
    return redirect(url_for("login_bp.login", page='login'))