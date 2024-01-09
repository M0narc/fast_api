from fastapi import Body, FastAPI, HTTPException
from constants import BOOKS

app = FastAPI()


@app.get("/books")
async def read_all_books():
    """
    endpoint to return all boks
    """
    return BOOKS


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    """
    endpoint to return books by title name
    """
    try:
        book = next(book for book in BOOKS if book.get('title').casefold() == book_title.casefold())
        return book
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"{book_title} has not been found in our repository.")
    

@app.get("/books/")
async def read_category_by_query(category: str):
    """
    endpoint to return books by category
    """
    books_to_return = [book for book in BOOKS if book.get('category').casefold() == category.casefold()]

    if not books_to_return:
        raise HTTPException(status_code=404, detail=f"No books found for category: {category}.")
    
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    """
    endpoint to return books by author name and category
    """
    books_to_return = [book for book in BOOKS 
                       if book.get('author').casefold() == book_author.casefold() and 
                       book.get('category').casefold() == category.casefold()]
    
    if not books_to_return:
        raise HTTPException(status_code=404, detail=f'no books from author: {book_author}, have been found in the category: {category}')
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    """
    function to add a new book to BOOKS constant
    """
    BOOKS.append(new_book)