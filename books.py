from fastapi import Body, FastAPI, HTTPException
from book import Book, BookRequest, BOOKS
from utils import find_book_id

app = FastAPI()


@app.get("/books")
async def read_all_books():
    """
    endpoint to return all boks
    """
    return BOOKS


@app.get("/books/{id}")
async def get_book_by_id(book_id: int):
    """
    Endpoint to get book by id
    """
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise ValueError(f'Book not found with ID: {book_id}')


@app.get("/books/")
async def get_books_by_rating(book_rating: int):
    """
    endpoint to return books by rating through queryparams
    """
    try:
        matching_books = []
        for book in BOOKS:
            if book.rating == book_rating:
                matching_books.append(book)
        return matching_books
    except:
        raise HTTPException(status_code=404,
                            detail=f'no matching books found for rating: {book_rating}')

@app.post("/books/create-book")
async def create_book(book_request: BookRequest):
    """
    Function to add a new book to BOOKS constant
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


@app.delete("/books/delete_book/{book_title}") # update
async def delete_book(book_title):
    """
    Function to delete a book using it's title
    """
    for i, book in enumerate(BOOKS):
        if book.get('title', '').casefold() == book_title:
            BOOKS.pop(i)
            return {"message": f"Book '{book_title}' was deleted successfully"}
            break
