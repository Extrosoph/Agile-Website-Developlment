from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from app.models import userAnswers, Answers, Score, User, db
from flask import session

class AssessmentForm1(FlaskForm):
    question1 = Answers.query.get(1)
    answer1 = SelectField(
        "Question 1: "+question1.question,
        choices=[
            ("", "---Select one of the following---"),
            ("1", question1.answer1),
            ("2", question1.answer2),
            ("3", question1.answer3),
            ("4", question1.answer4),
        ],
        validators=[DataRequired()]
    )
    question2 = Answers.query.get(2)
    answer2 = SelectField(
        "Question 2: "+question2.question,
        choices=[
            ("", "---Select one of the following---"),
            ("1", question2.answer1),
            ("2", question2.answer2),
            ("3", question2.answer3),
            ("4", question2.answer4),
        ],
        validators=[DataRequired()]
    )
    question3 = Answers.query.get(3)
    answer3 = SelectField(
        "Question 3: "+question3.question,
        choices=[
            ("", "---Select one of the following---"),
            ("1", question3.answer1),
            ("2", question3.answer2),
            ("3", question3.answer3),
            ("4", question3.answer4),
        ],
        validators=[DataRequired()]
    )
    question4 = Answers.query.get(4)
    answer4 = SelectField(
        "Question 4: "+question4.question,
        choices=[
            ("", "---Select one of the following---"),
            ("1", question4.answer1),
            ("2", question4.answer2),
            ("3", question4.answer3),
            ("4", question4.answer4),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit Answer")

class AssessmentForm2(FlaskForm):
    question = Answers.query.get(5)
    answer = SelectField(
        "Question 1: "+question.question,
        choices=[
            ("", "---Select one of the following---"),
            ("1", question.answer1),
            ("2", question.answer2),
            ("3", question.answer3),
            ("4", question.answer4),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit Answer")

def AssessmentAttempt1():
    form = AssessmentForm1()
    user = User.query.filter_by(id=session['id']).first()
    if form.validate_on_submit():
        userAttempt1 = userAnswers(userId = session['id'], assessmentId = 1)
        userAttempt2 = userAnswers(userId = session['id'], assessmentId = 1)
        userAttempt3 = userAnswers(userId = session['id'], assessmentId = 1)
        userAttempt4 = userAnswers(userId = session['id'], assessmentId = 1)
        answer1 = form.answer1.data
        answer2 = form.answer2.data
        answer3 = form.answer3.data
        answer4 = form.answer4.data
        userAttempt1.updateTable(question=1, answer = answer1)
        userAttempt2.updateTable(question=2, answer = answer2)
        userAttempt3.updateTable(question=3, answer = answer3)
        userAttempt4.updateTable(question=4, answer = answer4)
        db.session.add(userAttempt1)
        db.session.add(userAttempt2)
        db.session.add(userAttempt3)
        db.session.add(userAttempt4)
        db.session.commit()

        userScore = Score(userId = session['id'], assessmentId = 1)
        userScore.getScore(userAttempt1.score, userAttempt2.score, userAttempt3.score, userAttempt4.score)
        db.session.add(userScore)
        db.session.commit()
        return form

def AssessmentAttempt2():
    form = AssessmentForm2()
    user = User.query.filter_by(id=session['id']).first()
    if form.validate_on_submit():
        userAttempt = userAnswers(userId = session['id'], assessmentId = 2)
        answer = form.answer.data
        userAttempt.updateTable(question=5, answer = answer)
        db.session.add(userAttempt)
        db.session.commit()
        userScore = Score(userId = session['id'], assessmentId = 2)
        userScore.score = userAttempt.score
        db.session.add(userScore)
        db.session.commit()
        return form





