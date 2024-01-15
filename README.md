# fast_api
a proyect done with fastAPI

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



TODO:

update every function later on with try except or HTTP EXCEPTIONS &
check if logic applies