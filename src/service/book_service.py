from ..entity.book_entity import BookEntity
books = [BookEntity(book_id = 1, book_name="Principito", book_year=2024, book_author="Fidel", quantity="2"),
             BookEntity(book_id = 2,book_name = "Habitos Atomicos", book_year=2025, book_author="Fhalcom", quantity="5")]

def get_books(self):
    return books

def get_book(self, book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None

def add_book(self, book):
    return None

def remove_book(self, bookId):
    return None

def update_book(self, bookId, book):
    return None
