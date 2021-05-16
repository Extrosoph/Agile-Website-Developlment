from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment, User, Score, Answers
from json import dumps

home_bp = Blueprint('home_bp', __name__)
user_bp = Blueprint('user_bp', __name__)
statistics_bp = Blueprint('statistics_bp', __name__)
assessment_bp = Blueprint('assessments_bp', __name__)
getValue_bp = Blueprint('getValue_bp', __name__)

@home_bp.route("/")
def home():
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

        questions2 = []
        answers2 = []

        questions2.append(questions[4].question)
        answers2.append(questions[4].answer1)
        answers2.append(questions[4].answer2)
        answers2.append(questions[4].answer3)
        answers2.append(questions[4].answer4)

        return render_template("assessment.html", page='assessment', questions1=questions1, answers1=answers1,
                               questions2=questions2, answers2=answers2)
    else:

        return render_template("assessment.html", page='assessment', questions1=0, answers1=0,
                               questions2=0, answers2=0)

@getValue_bp.route("/getValue", methods=["POST"])
def getValue():
    req = request.get_json()
    query = request.form['query']

    questions = Answers.query.all()
    correct_answers = []

    for i in range(5):
        correct_answers.append(questions[i].correctAnswer)

    response = make_response(jsonify({'username': dumps(correct_answers)}), 200)

    return response

