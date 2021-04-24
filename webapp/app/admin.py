from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment, db

admin_bp = Blueprint('admin_bp', __name__)
adminAseessment_bp = Blueprint('adminAseessment_bp', __name__)
adminUser_bp = Blueprint('adminUser_bp', __name__)

@admin_bp.route("/admin", methods=["POST", "GET"])
def admin():
        return render_template("admin.html", page='admin')

@adminAseessment_bp.route("/adminAssessment", methods=["POST", "GET"])
def admin():
        return render_template("adminAssessment.html", page='admin')

@adminUser_bp.route("/adminUser", methods=["POST", "GET"])
def admin():
        return render_template("adminUser.html", page='admin')