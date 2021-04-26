from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment, db

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
        print(len(assessment))
        for key in request.form.keys():
            for value in request.form.getlist(key):
                print(key, ":", value)
        newAssessment = Assessment(category=request.form['assessmentName'])
        print(newAssessment)
        db.session.add(newAssessment)
        db.session.commit()
        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessment), assessment=assessment)
    else:
        assessments = Assessment.query.all()
        # print(type(assessment.category))
        # for x in assessment:
        #     print(x.category)
        # print(len(assessment))
        categories = ""
        for assessment in assessments:
            categories += '<tr><th><p class="category">' + assessment.category + '</p></th></tr>'
        return render_template("adminAssessment.html", page='admin', assessmentLen=len(assessments), assessment=categories)
@adminUser_bp.route("/adminUser", methods=["POST", "GET"])
def adminUser():
    return render_template("adminUser.html", page='admin')