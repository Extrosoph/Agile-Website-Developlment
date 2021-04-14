from flask import Flask, session
from datetime import timedelta
from secrets import token_urlsafe

app = Flask(__name__)

#Need to change secret key
app.secret_key = token_urlsafe(18)

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#Set session variable to last only for 5 mintues instead of 30 days.
app.permanent_session_lifetime = timedelta(minutes=5)

from app import views, auth
