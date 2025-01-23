from ..entity.book_entity import BookEntity

books = [BookEntity(book_id=1, book_name="Principito", book_year=2024, book_author="Fidel", quantity="2").to_dict(),
         BookEntity(book_id=2, book_name="Habitos Atomicos", book_year=2025, book_author="Fhalcom",
                    quantity="5").to_dict()]


def get_books():
    return books


def get_book(book_id: int):
    for book in books:
        if str(book["book_id"]) == book_id:
            return book
    return None


def add_book(book):
    return None


def remove_book(book_id):
    return None


def update_book(book_id, book):
    return None
