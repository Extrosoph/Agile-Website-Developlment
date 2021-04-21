from flask import Flask, session, Blueprint
from datetime import timedelta
from secrets import token_urlsafe

app = Flask(__name__)

#Set a safe secret key
app.secret_key = token_urlsafe(18)

#Set session variable to last only for 5 mintues instead of 30 days.
app.permanent_session_lifetime = timedelta(minutes=5)

# Import the blueprints
from app import models
from app.views import home_bp, user_bp, statistics_bp, assessment_bp
from app.auth import login_bp, signup_bp, logout_bp
from app.admin import admin_bp

# Register the blueprints
app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(assessment_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(admin_bp)