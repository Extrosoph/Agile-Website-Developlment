from flask import Flask
from webapp import views, auth

app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)