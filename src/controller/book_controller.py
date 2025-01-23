from flask import Blueprint
from ..service.book_service import get_book, get_books
book = Blueprint('book', __name__, url_prefix='/api/books')

@book.route('/', methods=['GET'])
def get_books():
    return get_books()

@book.route('/<book_id>', methods=['GET'])
def get_book(book_id):
    return get_book(book_id = book_id)

@book.route('/', methods=['POST'])
def add_book():
    return "Add book"


@book.route('/<book_id>', methods=['PUT'])
def update_book(book_id):
    return "Update book {}".format(book_id)


@book.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return " Delete book: ".join(str(book_id))