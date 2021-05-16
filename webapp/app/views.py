from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint, jsonify, make_response
from app.models import Assessment, User, Score, Answers, db
from json import dumps

home_bp = Blueprint('home_bp', __name__)
user_bp = Blueprint('user_bp', __name__)
statistics_bp = Blueprint('statistics_bp', __name__)
assessment_bp = Blueprint('assessments_bp', __name__)
getValue_bp = Blueprint('getValue_bp', __name__)
setQuestions_bp = Blueprint('setQuestions_bp', __name__)

@home_bp.route("/")
def home():
    print(app.config)
    return render_template("home.html", page='home')

@user_bp.route("/user")
def user():
    return render_template("user.html", page='user', users = User.userInfo(), 
    scores = Score.allScores(), assess= Assessment.allAssessment())

@statistics_bp.route("/statistics")
def statistic():
    return render_template("statistics.html", 
        page='statistics', users = User.userInfo(), 
        scores = Score.allScores(), maxScore1 = Score.maxScores(1), 
        maxScore2 = Score.maxScores(2), avgScore1 = Score.avgScores(1), 
        avgScore2 = Score.avgScores(2), numUsers = len(User.userInfo()),
        numAssess = len(Score.totalScores()))

@assessment_bp.route("/assessment")
def assessment():
    questions = Answers.query.all()
    questions1 = []
    answers11 = []
    answers12 = []
    answers13 = []
    answers14 = []

    if questions is not None:
        for i in range(4):
            questions1.append(questions[i].question)
            answers11.append(questions[i].answer1)
            answers12.append(questions[i].answer2)
            answers13.append(questions[i].answer3)
            answers14.append(questions[i].answer4)

        answers1 = []
        answers1.append(answers11)
        answers1.append(answers12)
        answers1.append(answers13)
        answers1.append(answers14)

        return render_template("assessment.html", page='assessment', questions1=questions1, answers1=answers1)
    else:

        return render_template("assessment.html", page='assessment', questions1=0, answers1=0,
                               questions2=0, answers2=0)

@getValue_bp.route("/getValue", methods=["POST"])
def getValue():
    questions = Answers.query.all()
    correct_answers = []

    for i in range(5):
        correct_answers.append(questions[i].correctAnswer)

    response = make_response(jsonify({'answers': dumps(correct_answers)}), 200)

    return response

@setQuestions_bp.route("/setQuestions", methods=["POST"])
def setQuestions():
    set = Answers.query.all()
    if set is None:
        set1 = Answers(question='What is are the phases of the Moon caused by?', answer1='Sunlight reflecting at different angles on the surface of the Moon as seen from Earth.',
                      answer2='The effect of Earth’s shadow covering specific parts of the Moon.', answer3='The rotation of the Moon about its axis.',
                      answer4='Due to the Earth’s rotation.', correctAnswer='Sunlight reflecting at different angles on the surface of the Moon as seen from Earth.', mark=10)

        set2 = Answers(question='Why does Ocean water rise up and down periodically on Earth?', answer1='Due to the gravitational attraction of the Moon as Earth rotates.',
                      answer2='Due to the gravitational attraction of the Sun.', answer3='Due to the centrifugal force acting outwards as the Earth rotates.',
                      answer4='Due to earthquakes occurring beneath the ocean floor.', correctAnswer='Due to the gravitational attraction of the Moon as Earth rotates.', mark=10)

        set3 = Answers(question='Approximately how far beneath our feet does the barycenter lie?', answer1='1700 km',
                      answer2='4671 km', answer3='2971 km', answer4='6371 km', correctAnswer='1700 km', mark=10)

        set4 = Answers(question='A solar eclipse occurs when the Earth, Moon and Sun are in a straight line whereas this is not necessary for a lunar eclipse.',
                      answer1='A lunar eclipse occurs when the Moon comes between the Earth and Sun and a solar eclipse occurs when the earth comes between the sun and the moon.',
                      answer2='A solar eclipse is when the moon comes between the Earth and the Sun, and a lunar eclipse occurs when the Earth comes between the Moon and the Sun.',
                      answer3='The rotation of the Moon about its axis.',
                      answer4='A solar eclipse is when the moon turns red due to the red light hitting it from the sun, and a lunar eclipse is when the sun gets completely blocked by the Moon.',
                      correctAnswer='A solar eclipse is when the moon comes between the Earth and the Sun, and a lunar eclipse occurs when the Earth comes between the Moon and the Sun.', mark=10)

        db.session.add(set1)
        db.session.add(set2)
        db.session.add(set3)
        db.session.add(set4)
        db.session.commit()

        response = make_response(jsonify({'return': 'complete'}), 200)

        return response

    else:
        response = make_response(jsonify({'return': 'complete'}), 200)

        return response

