from fastapi import Body, FastAPI, HTTPException, Path, Query
from book import Book, BookRequest, BOOKS
from utils import find_book_id, return_year
from starlette import status


app = FastAPI()


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    """
    endpoint to return all boks
    """
    return BOOKS


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(id: int = Path(gt=0)):
    """
    Endpoint to get book by id
    """
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail=f'Book not found with ID: {id}')


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
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


@app.get("/books/published_date/{pd}", status_code=status.HTTP_200_OK)
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



@app.post("/books/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    """
    endpoint to add a new book to BOOKS constant
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return {'message': f'Book {new_book.title} has been created.'}


@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    """
    endpoint to update books.
    """
    book_updated = False
    for i, book in enumerate(BOOKS):
        if book.id == book_request.id:
            BOOKS[i] = Book(id=book.id,
                            title=book_request.title,
                            author=book_request.author,
                            description=book_request.description,
                            rating=book_request.rating,
                            publish_date=book_request.publish_date)
            book_updated = True
            return {'message': f'Book {book.title} has been updated.'}
        if not book_updated:
            raise HTTPException(status_code=404, detail='book not found')


@app.delete("/books//{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    """
    endpoint to delete a book using it's title
    """
    book_deleted = False
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[i]
            book_deleted = True
            return {'message': f'Book {book.title} has been deleted.'}
        if not book_deleted:
            raise HTTPException(status_code=404, detail='book not found')
