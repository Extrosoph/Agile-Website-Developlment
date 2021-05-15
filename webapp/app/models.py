from app import app
from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw
from sqlalchemy import func

# Preparation for migration
from flask_script import Manager
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy(app)

# Preparation for migration
migrate = Migrate(app, db)
manager = Manager(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(80), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(120), nullable=False)
    admin = db.Column('admin', db.Boolean(), default=False)
    score = db.relationship('Score')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')
    dateJoined = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, email, password):
        salt = gensalt(rounds=12)
        self.username = username
        self.email = email
        self.password = hashpw(password.encode(), salt)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def userInfo():
        return User.query.all()

class Assessment(db.Model):
    __tablename__ = 'assessment'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    answer = db.relationship('Answers', cascade='all, delete-orphan')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')
    score = db.Column('score', db.Integer, nullable=True)
    dateCreated = db.Column(db.DateTime, default=datetime.now)
    scores = db.relationship('Score', cascade='all, delete-orphan')

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<assessment name: {}>'.format(self.category)

    def allAssessment():
        return Assessment.query.with_entities(Assessment.id, Assessment.category)

class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column('question', db.String(100), nullable=False)
    answer1 = db.Column('answer1', db.String(100), nullable=False)
    answer2 = db.Column('answer2', db.String(100), nullable=False)
    answer3 = db.Column('answer3', db.String(100), nullable=False)
    answer4 = db.Column('answer4', db.String(100), nullable=False)
    correctAnswer = db.Column('correctAnswer', db.String(100), nullable=False)
    mark = db.Column('mark', db.Integer, nullable=False)
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))

    def __init__(self, question, answer1, answer2, answer3, answer4, correctAnswer, mark):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer
        self.mark = mark

    def __repr__(self):
        return '<answer1: {} answer2: {} answer3: {} answer4: {}>'.format(self.answer1, self.answer2, self.answer3, self.answer4)

    def returnQuestion(qNumber):
        return Answers.query.all().filter_by(Answers.id==qNumber).first()

    def allAnswers():
        return Answers.query.all()

class userAnswers(db.Model):
    __tablename__ = 'userAnswers'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column('answer', db.String(100), nullable=False)
    score = db.Column('score', db.Integer, nullable=True)
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    timeAttempted = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<user: {} assessment: {}  my answer: {}>'.format(self.userId, self.assessmentId, self.answer)

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column('score', db.Integer, nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return '<user: {} assessment: {} score: {}'.format(self.user, self.assessmentId, self.score)

    def allScores():
        return Score.query.with_entities(Score.score, Score.userId, Score.assessmentId)

    def totalScores():
        return Score.query.all()

    def maxScores(id):
        return Score.query.with_entities(func.max(Score.score).label('max'), Score.userId, Score.assessmentId).filter(Score.assessmentId==id)
    
    def avgScores(id):
        return Score.query.with_entities(func.avg(Score.score).label('avg'), Score.userId, Score.assessmentId).filter(Score.assessmentId==id)




