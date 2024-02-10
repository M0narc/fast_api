from fastapi import Body, FastAPI, HTTPException
from book import Book, BookRequest,BOOKS

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


@app.get("/books/byauthor/{author_name}")
async def get_books_by_author_name(author_name: str):
    """
    endpoint to get all books using the author name
    """
    books_to_return = [book for book in BOOKS if book.get('author').casefold() == author_name.casefold()]

    if not books_to_return:
        raise HTTPException(status_code=404, detail=f'no books from auhor: {author_name}')
    return books_to_return


@app.post("/books/create-book")
async def create_book(book_request: BookRequest):
    """
    Function to add a new book to BOOKS constant
    """
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(update_book: dict = Body(...)):
    """
    Function to update a book.
    """
    title_to_update = update_book.get('title', '').casefold()
    for i, book in enumerate(BOOKS):
        if book.get('title', '').casefold() == title_to_update:
            BOOKS[i] = update_book
            return {"message": f"Book '{title_to_update}' updated successfully"}

    raise HTTPException(status_code=404, detail=f"Book '{title_to_update}' not found in our repository")


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title):
    """
    Function to delete a book using it's title
    """
    for i, book in enumerate(BOOKS):
        if book.get('title', '').casefold() == book_title:
            BOOKS.pop(i)
            return {"message": f"Book '{book_title}' was deleted successfully"}
            break
