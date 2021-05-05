# Github process:

**Make sure you are in the main branch and no issues**
1. Pull from main remote
2. Make some changes
3. Commit to main local
4. Push to main remote

# How to run with venv:

## windows:

1. pip install virtualenv
2. virtualenv venv
3. venv\Scripts\activate.bat 
4. set FLASK_APP=app
5. set FLASK_ENV=development
6. flask run
   
## mac/linux:

1. source venv\Scripts\activate
2. set FLASK_ENV=development
3. flask run


# How to run without venv:

## windows:
1. set FLASK_APP=app
2. set FLASK_ENV=development
3. cd webapp 
4. pip3 install -e .
5. flask run

## mac/linux:
1. export FLASK_APP=app
2. export FLASK_ENV=development
3. cd webapp 
4. pip3 install -e .
5. flask run


*Will create a simple ERD soon too :)
