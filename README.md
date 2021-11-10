# PassCave (Backend)

[![Documentation Status](https://readthedocs.org/projects/passcave-backend/badge/?version=latest)](https://passcave-backend.readthedocs.io/en/latest/?badge=latest)

Backend server which has the REST API for password management services.

## Basic Requirement

*  Python 3.9.7 (Programming Language)
*  Django 3.2.7 (Backend Framework)
*  virtualenvwrapper 4.8.4 (Virtual Environment)

## Project Setup

*  Clone the project:  `git clone https://github.com/purnendukar/PassCave-backend.git`
*  Install virtualenvwrapper:  `pip install virtualenvwrapper==4.8.4`

---
Note:
To customize virtualenvwrapper refer  `https://virtualenvwrapper.readthedocs.io/en/latest/`

---

*  Create virtual environment:  `mkvirtualenv <env_name>`
*  Activate virtual environment:  `workon <env_name>`
*  Install requirements:  `pip install requirements.txt`
*  Open Project directory:  `cd path/to/project/passcave`

---
Note:
Create `.env` file and set the variable values as given in `.env_example`

---

*  Create Migration:  `python manage.py makemigrations`
*  Migrate Database:  `python manage.py migrate`
*  Start Server:  `python manage.py runserver`
