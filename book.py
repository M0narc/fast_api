from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: str

    def __init__(self, id, title, author, description, rating, publish_date) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    publish_date: str


    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Author Name',
                'description': 'a brief description if possible',
                'rating': 5,
                'publish_date': datetime.now().strftime('%Y-%m-%d')
            }
        }

BOOKS = [
    Book(id=1, title="The Enchanted Garden", author="Luna Mystique", description="A magical journey through a secret garden filled with talking animals and enchanted plants.", rating=4, publish_date=datetime.now().strftime('%Y-%m-%d')),
    Book(id=2, title="Stellar Adventures", author="Cosmo Explorer", description="Join Captain Nova on an intergalactic quest to explore distant galaxies and encounter extraterrestrial civilizations.", rating=5, publish_date=datetime.now().strftime('%Y-%m-%d')),
    Book(id=3, title="Whimsical Wonderland", author="Alice Dreamweaver", description="Follow Alice as she ventures into a whimsical wonderland where talking cards, eccentric characters, and curious creatures await.", rating=3, publish_date=datetime.now().strftime('%Y-%m-%d')),
    Book(id=4, title="Mysteries of the Abyss", author="Marina Deepsea", description="Dive into the depths of the ocean to unravel mysteries hidden beneath the waves, encountering mythical sea creatures and lost civilizations.", rating=2, publish_date=datetime.now().strftime('%Y-%m-%d')),
    Book(id=5, title="The Quest for Cosmic Harmony", author="Zen Mastermind", description="Embark on a philosophical journey to discover the cosmic harmony that connects all living beings, blending wisdom and whimsy.", rating=4, publish_date=datetime.now().strftime('%Y-%m-%d'))
]
