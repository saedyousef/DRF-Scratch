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
`python3 manage.py runserver` and click [here](http://127.0.0.1:8000/admin)

> Login with the user you've already created, and click on the __Category__ and add one, the go back and click on the __Article__ and add an article

---
## APIs

---

You may need and app to interact with apis, so here you can install and run [Postman](https://www.postman.com/downloads/) to test the apis

---
> ## Articles
Articles list, an API that returns a list of all created articles, accepts only GET method.

In Postman place this url `http://127.0.0.1:8000/api/blog/articles`

Expected response code 200

Then the Article Detail, which returns all details related to an Article by passing the article's id in the url, accepts only GET method.

In Postman place this url `http://127.0.0.1:8000/api/blog/articles/1/`

Expected response code 200

---
> ## Categories
Categories list, an API that returns a list of all created categories, accepts only GET method.

In Postman place this url `http://127.0.0.1:8000/api/blog/categories`

Expected response code 200

Then the Category Detail, which returns all details related to a Category by passing the category's id in the url, accepts only GET method.

In Postman place this url `http://127.0.0.1:8000/api/blog/categories/1/`

Expected response code 200

---
> ## Users
Users list, an API that returns a list of all registerd users, accepts only GET method, authentication reqruied.

Need to pass the token in the header, `Authorization: Token your_auth_token`

In Postman place this url `http://127.0.0.1:8000/api/auth/users/`

Expected response code 200

Then the User Detail, which returns all details related to a User by passing the users's id in the url, accepts only GET method.

Need to pass the token in the header, `Authorization: Token your_auth_token`

In Postman place this url `http://127.0.0.1:8000/api/auth/users/1/`

Expected response code 200
> ## To obtain token for a user

In postman place this url `http://127.0.0.1:8000/api/auth/token`, change the Request method to POST.

This API requires two body params, username and password.
If the provided credentials macthces, the result will be token key.

Expected response code 200

---

> ## React(Like) to an article

React is an POST API that store a reaction(Like) for a specified article by the logged in user.
User can't react more than once 

Need to pass the token in the header, `Authorization: Token your_auth_token`

In the body params, `article_id` is a required integer param for an existing record.

In Postman place this url `127.0.0.1:8000/api/blog/article/react/`

Expected response code 201

---

## Test

`python3 manage.py test`

You should see 6 tests that ran successfully with 0 errors