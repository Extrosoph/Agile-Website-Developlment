from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment, db
from json import dumps

admin_bp = Blueprint('admin_bp', __name__)
adminAssessment_bp = Blueprint('adminAseessment_bp', __name__)
adminUser_bp = Blueprint('adminUser_bp', __name__)

@admin_bp.route("/admin", methods=["POST", "GET"])
def admin():
    return render_template("admin.html", page='admin')

@adminAssessment_bp.route("/adminAssessment", methods=["POST", "GET"])
def adminAssessment():
    if request.method == "POST":
        assessment = Assessment.query.all()
        for x in request.form:
            print(x)
        print('a')

        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessment), assessment=assessment)
    else:
        assessment = Assessment.query.all()
        print('f')
        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessment), assessment=assessment)
@adminUser_bp.route("/adminUser", methods=["POST", "GET"])
def adminUser():
    return render_template("adminUser.html", page='admin')