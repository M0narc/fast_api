from pydantic import BaseModel, Field


class CreateUserRequests(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str = Field(min_length=8)
    role: str

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'randomUserName',
                'email': 'test@gmail.com',
                'first_name': 'Random',
                'last_name': 'Name',
                'password': 'Test123',
                'role': 'client'
            }
        }
