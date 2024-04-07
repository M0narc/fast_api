# We are using python version 3.10

# fast_api
a project done with fastAPI

# how to run
uvicorn books:app --reload
uvicorn filename:app --reload

URL: http://127.0.0.1:8000/books

uvicorn main:app --reload --host localhost --port 8080

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

# sqlite first

after downloading add it to your path if using windows
then you can use it
sqlite3 todos.db
    .schema  # to see the tables within our db
# insert
insert into todos (title, description, priority, complete) values ('study fastApi', 'finish DB part', 5, False);
select * from todos;

# update
UPDATE todos SET complete=True where id=5;
this updates ALL todos that have an id of 5

.mode column is my favorite
      table is nice too

# delete
delete from todos where id = 4

# password hashing management
it will be done with passlib and bcrypt (4.0.1)
