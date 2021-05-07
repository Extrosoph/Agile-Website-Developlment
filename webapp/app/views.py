from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint

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
    return render_template("statistics.html", page='statistics')

@assessment_bp.route("/assessment")
def assessment():
    return render_template("assessment.html", page='assessment')