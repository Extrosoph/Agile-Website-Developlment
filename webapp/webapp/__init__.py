from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Extrosoph"
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#Set session variable to last only for 5 mintues instead of 30 days.
app.permanent_session_lifetime = timedelta(minutes=5)

from webapp import views, auth, models
