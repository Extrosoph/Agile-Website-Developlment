Group:
22764884: Theoridho Andily
22723671: Saksham Chopra
21499457: Isaac Chegwidden

# Design and Set up

## Venv
The best way to run the web server is through the use of python virtual environment and so
far we have been utilising it. To install venv we ran **[ pip install venv ]** and then ran **[ virtualenv venv ]** to create the venv folder.

## Flask Migrate
Once we have the venv setup we ran use flask migrate to create the database file.
To run set up flask migrate we initially ran **[ flask db init ]** to create the migration folder, then
we ran **[ flask db migrate ]** to create the first migration. After the first migrations are finished, we
ran **[ flask db upgrade ]** to make and update the database based on changes being made to the model.py file.

## Structure
For the set up of the webapp we followed the structure from large flask webapp. We have the first folder
called webapp and another folder called app inside which holds all the routing, static files and html templates.
We also made setup.py which is from the large flask application website and also created a config file which sets the flask configurations.
Every time we need to include a specific dependencies we add them to requirements.txt which can then be installed through pip.
We have always been using bluerpints from the beginning.

## Flask, Jquery and Ajax 
We had chosen to keep using Jquery for our main.js file to make it neater. Throughout main.js we implemented many ajax POST and GET request
to make our website more efficient. We kept the Js to be external and only one file for the same reason. Unfortunately we were unable to keep the css
file in one file, but we maintained a unique naming sceme. We also had to consider whether to use single application or multiple page 
application for certain pages using Jquery.

## Gits
We added certain files which did not need to be in git, and they are placed in .gitignore file.
We had always ran git commits and push with specific messages and resolve any merge conflict together.

## Database
For the database we initially created them through the sqlalchemy until we started using flask migrate
We had an initial design which were changed numerous amount until we had the design now. They include multiple type of relationship
from one-to-one, one-to-many and many-to-many. In the initial design there were a lot of unnecessary tables which were then removed to 
make the design better. There is an included erd diagram which shows the structure of our database including the relationships.

## Initial Set UP
Depending on the OS it will either be pip or pip3 and set or export. 
pip3 and export is used for mac/linux.
pip and set is used for windows.

1. To set up the server we first run **[ pip install -r -requirements.txt ]** to download all the required dependencies
2. We go into the webapp folder and run **[ pip intall -e . ]** to set up the application
3. exit the webapp folder **[ cd .. ]**
4. run **[flask db upgrade 9f85057d656a]** to set up the database based on the latest version
5. Depending on the required task we either set environment to development or production:
    * **[ set FLASK_ENV=development ]**
    * **[ set FLASK_ENV=production ]**
6. flask run

# Testing with selenium:

We had started on testing with selenium in test.py file using chromebrowser but we also planned on using Safary driver as well as mozilla Firefor driver.
So far test.py can click on links and login only.

## Accounts made

When the web server starts it will create a new user which can be used for testing.
The details of the account is:
* username: admin
* email: admin@admin.com
* password: admin

## References
for webapp structure: https://flask.palletsprojects.com/en/1.1.x/patterns/packages/

for creating erd: erdplus.com

for config.py: https://flask.palletsprojects.com/en/1.1.x/config/

for flask_migrate: https://flask-migrate.readthedocs.io/en/latest/

