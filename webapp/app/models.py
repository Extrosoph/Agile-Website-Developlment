from app import app
from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw

# Preparation for migration
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

# App configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseModel.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Preparation for migration
# migrate = Migrate(app, db)
#
#
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# manager.run()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(80), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(120), nullable=False)
    admin = db.Column('admin', db.Boolean(), default=False)
    assessments = db.relationship('Assessment')
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

class Assessment(db.Model):
    __tablename__ = 'assessment'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Questions', cascade='all, delete-orphan')
    answer = db.relationship('Answers', cascade='all, delete-orphan')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')
    correctAnswer = db.relationship('correctAnswer', cascade='all, delete-orphan')
    score = db.relationship('Score', uselist=False, back_populates='assessment', cascade='all, delete-orphan')

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<assessment name: {}>'.format(self.category)

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column('question', db.String(100), nullable=False)
    answers = db.relationship('Answers')
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    correctAnswer = db.relationship('correctAnswer', uselist=False, cascade='all, delete-orphan')
    userAnswers = db.relationship('userAnswers', cascade='all, delete-orphan')

    def __repr__(self):
        return '<assessment: {} questions: {} correct answer: {}>'.format(self.assessmentId, self.question, self.correctAnswer)

class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    answer1 = db.Column('answer1', db.String(100), nullable=False)
    answer2 = db.Column('answer2', db.String(100), nullable=False)
    answer3 = db.Column('answer3', db.String(100), nullable=False)
    answer4 = db.Column('answer4', db.String(100), nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey('questions.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    correctAnswer = db.relationship('correctAnswer', uselist=False, cascade='all, delete-orphan')

    def __init__(self, answer1, answer2, answer3, answer4):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4

    def __repr__(self):
        return '<answer1: {} answer2: {} answer3: {} answer4: {}>'.format(self.answer1, self.answer2, self.answer3, self.answer4)

class userAnswers(db.Model):
    __tablename__ = 'userAnswers'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column('answer', db.String(100), nullable=False)
    score = db.Column('score', db.Integer, nullable=True)
    questionId = db.Column(db.Integer, db.ForeignKey('questions.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    timeAttempted = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<user: {} assessment: {} question: {} my answer: {}>'.format(self.userId, self.assessmentId, self.questionId, self.answer)

class correctAnswer(db.Model):
    __tablename__ = 'correctanswer'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column('answer', db.String(100), nullable=False)
    mark = db.Column('mark', db.Integer, nullable=True)
    questionId = db.Column(db.Integer, db.ForeignKey('questions.id'))
    answerId = db.Column(db.Integer, db.ForeignKey('answers.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))

    def __init__(self, given, mark):
        self.answer = given
        self.mark = mark

    def __repr__(self):
        return '<assessment: {} question: {} correct answer: {}>'.format(self.assessmentId, self.questionId, self.answer)

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column('score', db.Integer, nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessmentId = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    assessment = db.relationship('Assessment', back_populates='score')
    timeAttempted = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return '<user: {} assessment: {} score: {}'.format(self.user, self.assessmentId, self.score)

db.create_all()



