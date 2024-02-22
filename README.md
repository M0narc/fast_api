# fast_api
a project done with fastAPI

# how to run
uvicorn books:app --reload

URL: http://127.0.0.1:8000/books

uvicorn books:app --reload --host localhost --port 8080

URL: http://localhost:8080/books

# swagger

URL: http://127.0.0.1:8000/docs

Localhost
URL: http://localhost:8080/docs


# query params know how

? is for sending querys
example => /?category=science

%20 is for line jumps
example => /title%20one

# Pydantics

used for data modeling, data parsing and has efficient error handling.

is commonly used as a  resource for data validation and how to handle data coming to our FastAPI application.

new objectives

To Do project.

embed a SQL DB
authentication jwt
authorization (admin, normal users)
hashing passwords

create new Todo table model for the app

using these todos to save records throughout the project
