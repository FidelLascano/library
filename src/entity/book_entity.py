class BookEntity:
    def __init__(self,book_id, book_name, book_author, book_year, quantity):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.quantity = quantity

    def __int__(self, book):
        book.book_id = book.id
        self.book_name = book.book_name
        self.book_author = book.book_author
        self.book_year = book.book_year
        self.quantity = book.quantity

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "book_author": self.book_author,
            "book_year": self.book_year,
            "quantity": self.quantity
        }