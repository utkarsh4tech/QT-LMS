from src.db_manager import db_manager
from src.models import Book

class BookController:
    def __init__(self):
        self.db = db_manager

    def add_book(self, book : Book):

        # Check if book already exists
        existing_book = self.get_book_by_id(book.id)
        if existing_book:
            return {"success": False, "message": f"Book with ID {book.id} already exists!"}
        
        query = "INSERT INTO tbl_addbook (id, title, author, publisher, isAvail) VALUES (?, ?, ?, ?, ?)"
        values = (book.id, book.title, book.author, book.publisher, True)
        self.db.execute_query(query, values)
        return {"success": True, "message": "Book added successfully!"}

    def get_books(self):
        """Fetches all books from the database."""
        query = "SELECT * FROM tbl_addbook"
        return self.db.fetch_data(query)

    def get_book_by_id(self, book_id):
        """Fetches a single book by ID."""
        query = "SELECT * FROM tbl_addbook WHERE id = ?"
        result = self.db.fetch_data(query, (book_id,))
        if result and len(result) != 0:
            return result[0]
        else: 
            return None