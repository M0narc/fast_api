from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    # this is how alchemy knows how to name the table
    __tablename__='todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
