# SiTechTask

## Installation
---
> First we need to create a virtualenv
`python3 -m venv env`, then `cd env/` and run `source/bin activate`



> Clone this repo into your env directory `git clone https://github.com/saedyousef/SiTechTask.git`

---
## Migrations

`cd SiTechTask & python3 manage.py migrate`
> Create a Superuser
`python3 manage.py createsuperuser` enter a username, email and password.

> Install packages using pip
`pip3 install -r requirements.txt`

> Now lets create all migrations required by these packages and our Models
`python3 manage.py makemigrations & python3 manage.py migrate`

--- 

## Usage

---
> Run the webserver
`python3 manage.py runserver` and click on this link [Link](http://127.0.0.1:8000/admin)

> Login with the user you've already created, and click on the __Category__ and add one, the go back and click on the __Article__ and add an article

---
> APIs


