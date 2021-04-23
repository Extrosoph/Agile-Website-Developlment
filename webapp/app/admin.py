from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint
from app.models import Assessment, db
from json import dumps

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/admin", methods=["POST", "GET"])
def admin():
        return render_template("admin.html", page='admin')