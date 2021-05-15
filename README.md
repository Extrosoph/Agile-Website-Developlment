# How to run with venv:

## windows:

### How to install venv through pip:

1. pip install virtualenv
2. virtualenv venv

### Must install requirements!

* pip install -r requirements.txt

#### Must create the DB file first!

1. flask db migrate
2. flask db upgrade
3. venv\Scripts\activate.bat
4. set FLASK_APP=webapp\app
5. set FLASK_ENV=development
6. flask run
   
## mac/linux:

### Must install requirements!

* pip3 install -r requirements.txt

#### Must create the DB file first!

1. flask db migrate
2. flask db upgrade
3. source venv/bin/activate
4. export FLASK_APP=webapp\app
5. export FLASK_ENV=development
6. flask run

## How to deactivate venv:

* deactivate

# How to run without venv:

## windows:

### Must install requirements!

* pip3 install -r requirements.txt

#### Must create the DB file first!

1. flask db migrate
2. flask db upgrade
3. set FLASK_APP=webapp\app
4. set FLASK_ENV=development
5. flask run

## mac/linux:

### Must install requirements!

* pip install -r requirements.txt

#### Must create the DB file first!

1. flask db migrate
2. flask db upgrade
3. export FLASK_APP=webapp\app
4. export FLASK_ENV=development
5. flask run

# Testing with selenium:

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
