## Welcome to AIG_Task Repository.
```
A web app that counts the number of words in a piece of text that the user submits
```

It's built with Python & Django
* Ubuntu 14.0+
* Python 3.4+
* Django 1.7+

### Project Setup
##### Virtual Environment

Install virtual environment and create the environment for the project:
```
$ apt-get install python-virtualenv
$ mkvirtualenv aig_task
```

Activate the environment, and install packages according to the requirements.txt file:
```
$ pip install -r /path/to/requirements.txt
```

When done working on the project, you may deactivate virtualenv.
```
$ deactivate aig_task
```

### Coding Style
[PEP 8](https://www.python.org/dev/peps/pep-0008/).

### Setting up the project
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

127.0.0.1:8000/
```

### Extras
```
* Created a function in views.py that gets user's ip address once they register with their email address.
* Created a function in views.py that generates Universal Unique Identifiers (UUIDs) and 
  assigns them to each registered user.
* Implemented Jumbotron Template for Bootstrap.
```

