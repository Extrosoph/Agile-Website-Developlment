from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment

home_bp = Blueprint('home_bp', __name__)
user_bp = Blueprint('user_bp', __name__)
statistics_bp = Blueprint('statistics_bp', __name__)
assessment_bp = Blueprint('assessments_bp', __name__)

@home_bp.route("/")
def home():
    return render_template("home.html", page='home')

@user_bp.route("/user")
def user():
    return render_template("user.html", page='user')

@statistics_bp.route("/statistics")
def statistic():
    current_user_id = User.query.filter_by(id=current_user.id).first()
    return render_template("statistics.html", page='statistics', uAssess=Assessment.userAssessment(userId=current_user_id.id))

@assessment_bp.route("/assessment")
def assessment():
    return render_template("assessment.html", page='assessment')