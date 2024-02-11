from fastapi import Body, FastAPI, HTTPException, Path
from book import Book, BookRequest, BOOKS
from utils import find_book_id, return_year


app = FastAPI()


@app.get("/books")
async def read_all_books():
    """
    endpoint to return all boks
    """
    return BOOKS


@app.get("/books/{id}")
async def get_book_by_id(id: int = Path(gt=0)):
    """
    Endpoint to get book by id
    """
    for book in BOOKS:
        if book.id == id:
            return book
    raise ValueError(f'Book not found with ID: {id}')


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


@app.get("/books/published_date/{pd}")
async def get_by_published_date(pd: str):
    """
    get books by published date
    """
    matching_books = [book for book in BOOKS if return_year(book.publish_date)[0] == pd]
    if matching_books:
        return matching_books
    else:
        raise HTTPException(status_code=404,
                        detail=f'Date {pd} has no book published.')



@app.post("/books/create-book")
async def create_book(book_request: BookRequest):
    """
    endpoint to add a new book to BOOKS constant
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return {'message': f'Book {new_book.title} has been created.'}


@app.put("/books/update-book")
async def update_book(book_request: BookRequest):
    """
    endpoint to update books.
    """

    for i, book in enumerate(BOOKS):
        if book.id == book_request.id:
            BOOKS[i] = Book(id=book.id,
                            title=book_request.title,
                            author=book_request.author,
                            description=book_request.description,
                            rating=book_request.rating,
                            publish_date=book_request.publish_date)
            return {'message': f'Book {book.title} has been updated.'}


@app.delete("/books//{book_id}")
async def delete_book(book_id: int):
    """
    endpoint to delete a book using it's title
    """
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[i]
            return {'message': f'Book {book.title} has been deleted.'}
