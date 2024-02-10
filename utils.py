from book import Book, BOOKS

def find_book_id(book: Book):
    """
    incremental ID for new books,

    TO DO: this needs to change to an actual id finder
    """
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
