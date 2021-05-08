from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

from app import app,db
from app.models import User, Assessment, Answers, correctAnswer, Questions, Score, userAnswers
@app.shell_context_processor
def make_shell_context():
    return{
        "db":db,
        "Users":Users,
        "Assessment":Assessment,
        "answers":Answers,
        "correctAnswer":correctAnswer,
        "questions":Questions,
        "score":Score,
        "userAnswers":userAnswers,        
    }