from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint, jsonify, make_response
from app.models import Assessment, Questions, Answers, correctAnswer, Score, db
from datetime import datetime
from json import dumps

admin_bp = Blueprint('admin_bp', __name__)
adminAssessment_bp = Blueprint('adminAseessment_bp', __name__)
adminUser_bp = Blueprint('adminUser_bp', __name__)
getAssessment_bp = Blueprint('getAssessment_bp', __name__)

@admin_bp.route("/admin", methods=["POST", "GET"])
def admin():
    return render_template("admin.html", page='admin')

@getAssessment_bp.route("/getAssessment", methods=["POST"])
def getAssessment():

    req = request.get_json()
    category = request.form['category']
    assessment = Assessment.query.filter_by(category=category).first()

    questions = []
    answers = [[], [], [], []]
    correctAnswer = []

    # Get questions from db
    for question in assessment.questions:
        questions.append(question.question)

    # Get answers from db
    for answer in assessment.answer:
        answers[0].append(answer.answer1)
        answers[1].append(answer.answer2)
        answers[2].append(answer.answer3)
        answers[3].append(answer.answer4)

    # Get correct answer from db
    for correct_answer in assessment.correctAnswer:
        correctAnswer.append(correct_answer.answer)

    response = make_response(jsonify({'name': assessment.category,
                                 'questions': dumps(questions),
                                 'answers': dumps(answers),
                                 'correctAnswer': dumps(correctAnswer)
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
        scores = []
        for key in request.form.keys():

            # Add questions to db
            if 'question' in key:
                newQuestion = Questions(question=request.form[key])
                questions_from_form.append(newQuestion)
                db.session.add(newQuestion)
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
            answer = Answers(answer1=answers[a1], answer2=answers[a2], answer3=answers[a3], answer4=answers[a4])
            db.session.add(answer)
            correct_answer = correctAnswer(given=answers[a4], mark=int(scores[i]))
            db.session.add(correct_answer)
            answer.correctAnswer = correct_answer

            # Set the values for DB
            questions_from_form[i].answers.append(answer)
            questions_from_form[i].correctAnswer = correct_answer

            newAssessment.answer.append(answer)
            newAssessment.correctAnswer.append(correct_answer)
            newAssessment.questions.append(questions_from_form[i])
            a1 += 4
            a2 += 4
            a3 += 4
            a4 += 4

        # Sum up scores to get the final result
        result = Score(score=sum([int(i) for i in scores]))
        newAssessment.score = result
        db.session.commit()

        assessment = Assessment.query.all()
        if assessment is not None:
            categories = ""
            for items in assessment:
                categories += '<tr><th><p class="categoryAssessment" id="Assessment>' + items.category + '</p></th></tr>'

        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessment), assessment=categories)

    else:
        assessment = Assessment.query.all()
        if assessment is not None:
            categories = ""
            counter = 0
            for items in assessment:
                categories += '<tr><th><p class="categoryAssessment" id="Assessment" >' + items.category + '</p></th></tr>'

            return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessment), assessment=categories)
        else:
            return render_template("adminAssessment.html", page='admin', assessmentLen=0)

@adminUser_bp.route("/adminUser", methods=["POST", "GET"])
def adminUser():
    return render_template("adminUser.html", page='admin')