from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Import the blueprints and models
from app import models
from app.views import home_bp, user_bp, statistics_bp, assessment_bp
from app.auth import login_bp, signup_bp, logout_bp
from app.admin import admin_bp, adminAssessment_bp, adminUser_bp, getAssessment_bp, getUser_bp, makeAdmin_bp, removeUser_bp, adminAccount_bp, deleteAssessment_bp

# Register the blueprints
app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(assessment_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(adminAssessment_bp)
app.register_blueprint(adminUser_bp)
app.register_blueprint(getAssessment_bp)
app.register_blueprint(getUser_bp)
app.register_blueprint(makeAdmin_bp)
app.register_blueprint(removeUser_bp)
app.register_blueprint(adminAccount_bp)
app.register_blueprint(deleteAssessment_bp)