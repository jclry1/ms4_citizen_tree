# Initial Setup
### Based on Django for Professinoals by William S. Vincent
Create virtual environment using pipenv
Install Django (this project uses 3.2.6 - see pipfile.lock)
Install psycopg2 for using postgres in development
Start the Django project and run the server to check - ok

Stop the virtual env.

Set up the Dockerfile and docker-compose files

Change settings so that default db is postgres and not sqlite3.

Before running migratinos, set up custom user model: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

# Set up static files
Based on:
* Django for Professionals
* Django docs
* Boutique Ado

## Problem using docker-compose to install packages
For much of the basic setup of the project, I'm following Django for Professionals by William S. Vincent. To install packages, eg Crispy Forms, he recommends the following command in the terminal:
```sh
$ docker-compose exec web pipenv install <django-crispy-forms==1.9.2>
```
I found that this did not work. The problem seems to be known but I didn't find a perfect solution.
See:
https://stackoverflow.com/questions/53400385/django-docker-and-pipenv-error-adding-new-packages
https://stackoverflow.com/questions/60949436/django-docker-and-pipenv-error-adding-new-packages-not-transfering-from-con

The command that seems to work is to remove the docker-compose element and just install using pipenv. The package gets added to the pipfile and pipfile.lock:
```sh
pipenv install django-crispy-forms
```





