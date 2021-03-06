from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint, jsonify, make_response
from app.models import Assessment, Answers, Score, db, User
from datetime import datetime
from json import dumps

admin_bp = Blueprint('admin_bp', __name__)
adminAssessment_bp = Blueprint('adminAseessment_bp', __name__)
adminUser_bp = Blueprint('adminUser_bp', __name__)
getAssessment_bp = Blueprint('getAssessment_bp', __name__)
getUser_bp = Blueprint('getUser_bp', __name__)
makeAdmin_bp = Blueprint('makeAdmin_bp', __name__)
removeUser_bp = Blueprint('removeUser_bp', __name__)
adminAccount_bp = Blueprint('adminAccount_bp', __name__)
deleteAssessment_bp = Blueprint('deleteAssessment_bp', __name__)


@admin_bp.route("/admin", methods=["POST", "GET"])
def admin():
    return render_template("admin.html", page='admin')

@makeAdmin_bp.route("/makeAdmin", methods=["POST"])
def makeAdmin():
    # Function to get user details from ajax
    req = request.get_json()
    username = request.form['username']

    current_user_username = User.query.filter_by(username=username).first()

    current_user_username.admin = True
    db.session.commit()

    response = make_response(jsonify({'return': 'complete'}), 200)

    return response

@deleteAssessment_bp.route("/deleteAssessment", methods=["POST"])
def deleteAssessment():
    # Function to get user details from ajax
    req = request.get_json()
    name = request.form['category']

    assessment = Assessment.query.filter_by(category=name).first()

    db.session.delete(assessment)
    db.session.commit()

    response = make_response(jsonify({'return': 'complete'}), 200)

    return response

@removeUser_bp.route("/removeUser", methods=["POST"])
def removeUser():
    # Function to get user details from ajax
    username = request.form['username']

    current_user_username = User.query.filter_by(username=username).first()

    db.session.delete(current_user_username)
    db.session.commit()

    response = make_response(jsonify({'return': 'complete'}), 200)

    return response

@getUser_bp.route("/getUser", methods=["POST"])
def getUser():
    # Function to get user details from ajax
    query = request.form['query']

    current_user_email = User.query.filter_by(email=query).first()
    current_user_username = User.query.filter_by(username=query).first()

    # If there is no such us`ername or email
    if current_user_email is None and current_user_username is None:
        response = make_response(jsonify({'result': 'none'}), 200)

    # If the user sends an email
    elif current_user_email is not None:
        response = make_response(jsonify({'username': current_user_email.username,
                                          'email': current_user_email.email,
                                          'Admin': current_user_email.admin,
                                          'dateJoined': current_user_email.dateJoined,
                                          }), 200)

    # If the user sends a username
    else:
        response = make_response(jsonify({'username': current_user_username.username,
                                          'email': current_user_username.email,
                                          'Admin': current_user_username.admin,
                                          'dateJoined': current_user_username.dateJoined,
                                          }), 200)

    return response

@getAssessment_bp.route("/getAssessment", methods=["POST"])
def getAssessment():

    req = request.get_json()
    category = request.form['category']
    assessment = Assessment.query.filter_by(category=category).first()

    questions = []
    answers = []
    correctAnswer = []
    mark = []

    # Get questions from db
    for question in assessment.answer:
        questions.append(question.question)


    # Get answers from db
    for answer in assessment.answer:
        answers.append(answer.answer1)
        answers.append(answer.answer2)
        answers.append(answer.answer3)
        answers.append(answer.answer4)


    # Get correct answer from db
    for correct_answer in assessment.answer:
        correctAnswer.append(correct_answer.correctAnswer)
        mark.append(correct_answer.mark)

    response = make_response(jsonify({'name': assessment.category,
                                 'questions': dumps(questions),
                                 'answers': dumps(answers),
                                 'correctAnswer': dumps(correctAnswer),
                                 'mark': dumps(mark)
                                 }), 200)

    return response

@adminAssessment_bp.route("/adminAssessment", methods=["POST", "GET"])
def adminAssessment():
    if request.method == "POST":

        # Add new assessment to db
        newAssessment = Assessment(category=request.form['assessmentName'])
        db.session.add(newAssessment)

        number_of_question = 0
        questions_from_form = []
        for key in request.form.keys():

            # Add questions to db
            if 'question' in key:
                newQuestion = request.form[key]
                questions_from_form.append(newQuestion)
                number_of_question += 1

        # Get the scores
        scores = []
        for value in request.form.getlist('score'):
            scores.append(value)

        # Get the answers
        answers = []
        for value in request.form.getlist('answer'):
            answers.append(value)

        a1, a2, a3, a4 = 0,1,2,3
        for i in range(number_of_question):

            # Add answers and correct answers to db
            answer = Answers(question=questions_from_form[i], answer1=answers[a1], answer2=answers[a2], answer3=answers[a3], answer4=answers[a4], correctAnswer=answers[a4], mark=scores[i])
            db.session.add(answer)

            # Set the values for DB
            newAssessment.answer.append(answer)

            a1 += 4
            a2 += 4
            a3 += 4
            a4 += 4

        # Sum up scores to get the final result
        result = sum([int(i) for i in scores])
        newAssessment.score = result
        db.session.commit()

        assessments = Assessment.query.order_by(Assessment.dateCreated.desc())[:10]
        category = []
        for assessment in assessments:
            category.append(assessment.category)
        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessments), assessment=category)

    else:
        assessments = Assessment.query.order_by(Assessment.dateCreated.desc())[:10]
        category = []
        for assessment in assessments:
            category.append(assessment.category)
        if assessments is not None:
            return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessments), assessment=category)
        else:
            return render_template("adminAssessment.html", page='admin', assessmentLen=0)

@adminUser_bp.route("/adminUser", methods=["POST", "GET"])
def adminUser():
    users = User.query.order_by(User.dateJoined.desc())[:10]
    if users is not None:
        usernames = ""
        for user in users:
            usernames += '<tr><th><p class="categoryAssessment" id="User" >' + user.username + '</p></th></tr>'
        return render_template("adminUser.html", page='admin', userLen=len(users), user=usernames)

    else:
        return render_template("adminUser.html", page='admin', userLen=0)

@adminAccount_bp.route("/adminAccount", methods=["POST"])
def adminAccount():
    admin = User.query.filter_by(username='admin').first()
    if admin is None:
        new_admin = User(username='admin', email='admin@admin.com', password='admin')
        new_admin.admin = True
        db.session.add(new_admin)
        db.session.commit()
        response = make_response(jsonify({'result': 'completed'}), 200)

    else:
        response = make_response(jsonify({'result': 'completed'}), 200)
    return response