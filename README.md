CSV_MANAGER

REQUIREMENTS:
- python 3.6.8 or greater 
- venv module

INSTALLATION:
- go to the project directory and run "python3 -m venv" after de python environment is created use "source ./<env_name>/bin/activate" ,
  then run "pip install -r requirements.txt" once the installation is completed you should be able to run the server with"python manage.py runserver"
  and you are ready to go :D

MIGRATIONS:
- in the manage.py directoy run "python manage.py makemigrations" and then "python manage.py migrate" this will apply all model changes to 
  sqlite database and create the tables

TEST:
- use "python manage.py test csv_manager" to run unit tests

UPLOAD CSV FILE:
- to upload a a csv file run the django server and go to localhost

FETCH DATA:
- getting data trough the API can be done with this endpoint "http://localhost/store/?<zub_id=int>" providing the zubale id of the store
  it will return store description and all information about the location of the store
