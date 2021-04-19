from app import app
from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw
from datetime import datetime

db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(80), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(120), nullable=False)
    admin = db.Column('admin', db.Boolean(), default=False)
    assessments = db.relationship('Assessments')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')
    score = db.relationship('score', uselist=False, back_populates='user', cascade='all, delete-orphan')

    def __init__(self, username, email, password):
        salt = gensalt(rounds=12)
        self.username = username
        self.email = email
        self.password = hashpw(password.encode(), salt)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Assessment(db.Model):
    __tablename__ = 'assessment'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Questions', cascade='all, delete-orphan')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')
    correctAnswers = db.relationship('correctAnswers', cascade='all, delete-orphan')
    score = relationship('Score', userlist=False, back_populates='assessment', cascade='all, delete-orphan')

    def __repr__(self):
        return '<assessment set {}>'.format(self.id)

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column('question', db.String(100), nullable=False)
    assessmentId = db.Columnn(db.Integer, db.ForeignKey('assessment.id'))
    correctAnswer = db.relationship('correctAnswers', uselist=False, back_populates='questions', cascade='all, delete-orphan')
    userAnswers = db.relationship('userAnsers', cascade='all, delete-orphan')

    def __repr__(self):
        return '<assessment: {} questions: {} correct answer: {}>'.format(self.assessmentId, self.question, self.correctAnswer)

class userAnswers(db.Model):
    __tablename__ = 'userAnswers'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column('answer', db.String(100), nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey('questions.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    timeAttempted = db.Column(db.Datetime, default=datetime.now)

    def __repr__(self):
        return '<user: {} assessment: {} question: {} my answer: {}>'.format(self.userId, self.assessmentId, self.questionId, self.answer)

class correctAnswers(db.Model):
    __tablename__ = 'correctAnswers'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column('answer', db.String(100), nullable=False)
    questionID = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('Questions', back_populates='corectAnswers')
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))

    def __repr__(self):
        return '<assessment: {} question: {} correct answer: {}>'.format(self.assessmentId, self.question, self.answer)

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column('score', db.Integer, nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='score')
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    assessment = db.relationship('Assessment', back_populate='score')

    def __repr__(self):
        return '<user: {} assessment: {} score: {}'.format(self.user, self.assessmentId, self.score)





