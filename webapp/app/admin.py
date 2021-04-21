from app import app
from flask import  redirect, url_for, render_template, request, session, flash, Blueprint

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/admin")
def admin():
    return render_template("admin.html", page='admin')