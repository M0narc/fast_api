from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal
from todos_request import TodoRequest

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    """
    db dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/', status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    """
    endpoint to get all Todos from the db
    """
    return db.query(Todos).all()


@app.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def read_todo_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    """
    endpoint to get all todos by id
    """
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,
                        detail=f'item with ID: {todo_id} not found')


@app.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    """
    endpoint to create todo
    """
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()


@app.put('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)):
    """
    endpoint to update todo by id
    """
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail=f'Todo with id: {todo_id} not found.')

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()
