from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Extrosoph"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Set session variable to last only for 5 mintues instead of 30 days.
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __int__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@app.route("/")
def home():
    return render_template("index.html", page='index')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        given_email = request.form['email']
        given_password = request.form['password']
        session["email"] = given_email
        current_user = users.query.filter_by(email=given_email).first()
        if current_user is not None and current_user.password == given_password:
            session["email"] = current_user.email
            session['logged_in'] = True
            session["username"] = current_user.username
            return render_template("account.html", username=current_user.username, page='account')
        elif current_user is not None and current_user.password != given_password:
            flash('Incorrect Password')
            return render_template("login.html", page='login')
        else:
            flash('Need to create an account')
            return render_template("login.html", page='login')
    else:
        # log_status = session['logged_in']
        # if log_status == True:
        #     flash("Already Logged In")
        #     return redirect(url_for("account"))
        return render_template("login.html", page='login')

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form["email"]
        password = request.form["password"]
        usr = users(username=username, email=email, password=password)
        db.session.add(usr)
        db.session.commit()
        session['logged_in'] = True
        return render_template("account.html", username=username, page='account')
    else:
        return render_template("signup.html", page='signup')

@app.route("/account", methods=["POST", "GET"])
def account():
    username = session["username"]
    return render_template("account.html", username=username, page='account')

@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("logged_in", None)
    return redirect(url_for("login", page='login'))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/about")
def about():
    return render_template("about.html", page='about')

@app.route("/tictactoe")
def tictactoe():
    return render_template("tictactoe.html", page='about')

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
