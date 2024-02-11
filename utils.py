from book import Book, BOOKS
import re

def find_book_id(book: Book):
    """
    incremental ID for new books,

    TO DO: this needs to change to an actual id finder
    """
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

def return_year(date):
    """
    util function to return year from dates
    """
    pattern = r'\d{4}'
    date_match = re.findall(pattern, date)
    return date_match
