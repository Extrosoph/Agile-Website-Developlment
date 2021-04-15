from app import app
from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, username, email, password):
        salt = gensalt(rounds=12)
        self.username = username
        self.email = email
        self.password = hashpw(password, salt)

    #To check password if cehckpw(given password, hashed value): True or False

    def __repr__(self):
        return '<Post %r>' % self.id

# class Assessments(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     QuestionID = db.Column(db.String(50), nullable=False)
#
# class Questions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
# class userAnswers(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


