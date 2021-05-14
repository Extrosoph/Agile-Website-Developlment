# How to run with venv:

## How to install venv through pip and create the venv folder
1. pip install virtualenv
2. virtualenv venv

## windows:

1. venv\Scripts\activate.bat 
2. set FLASK_APP=webapp\app
3. set FLASK_ENV=development
4. flask run
   
## mac/linux:

1. source venv/bin/activate 
2. export FLASK_APP=webapp\app
3. export FLASK_ENV=development
4. flask run

## How to deactivate venv

* deactivate

# How to run without venv:

## Must create the DB file first!

1. flask db migrate
2. flask db upgrade

## windows:

1. set FLASK_APP=webapp\app
2. set FLASK_ENV=development
3. flask run

## mac/linux:

1. export FLASK_APP=webapp\app
2. export FLASK_ENV=development
3. flask run

# Testing with selenium

1. run test.py

# Account with admin privileges for testing: 
**This account will be created once the server starts**

* username: admin
* password: admin
* email: admin@admin.com

# Github process:

* git clone <linktorepo> to clone the repository
* git pull to pull updated file
* git commit to commit changes to a file
* git add . to add the commits
* git push to push the changes from local to remote branch
* git checkout <branchname> to check out to another branch
* git fetch to update the project
* git log to show the commits log
* git status to show the changes between the local and remote branch
*Will create a simple ERD soon too :)
