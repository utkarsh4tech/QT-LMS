from src.db_manager import db_manager
from datetime import datetime
from src.controllers.book_controller import BookController
from src.controllers.member_controller import MemberController

class IssueController:
    def __init__(self):
        self.db = db_manager

    def issue_book(self, book_id, member_id):
        """Issues a book to a member."""

        book_status = BookController().get_book_by_id(book_id)
    
        if not book_status:
            return {"success": False, "message": "Book not found in the system!"}

        if not book_status["isAvail"]: 
            return {"success": False, "message": "Book is already issued and not available!"}

        member_exists = MemberController().get_member_by_id(member_id)
        
        if not member_exists:
            return {"success": False, "message": "Member not found! Cannot issue book."}

        query_issue = "INSERT INTO tbl_issue (bookID, memberID, issueTime, renewCount) VALUES (?, ?, ?, ?)"
        query_update = "UPDATE tbl_addbook SET isAvail = FALSE WHERE id = ?"

        values_issue = (book_id, member_id, datetime.now(), 0)
        try:
            self.db.execute_query(query_issue, values_issue)
            self.db.execute_query(query_update, (book_id,))
            return {"success": True, "message": "Book issued successfully!"}
        except RuntimeError as e:
            return {"success": False, "message": str(e)}

    def return_book(self, book_id):
        """Returns a book and updates availability."""

        book_status = BookController().get_book_by_id(book_id)
    
        if not book_status:
            return {"success": False, "message": "Book not found in the system!"}

        if book_status["isAvail"]: 
            return {"success": False, "message": "Book needs to be issued to be returned"}
        
        query_delete = "DELETE FROM tbl_issue WHERE bookID = ?"
        query_update = "UPDATE tbl_addbook SET isAvail = TRUE WHERE id = ?"

        self.db.execute_query(query_delete, (book_id,))
        self.db.execute_query(query_update, (book_id,))
        return {"success": True, "message": "Book returned successfully!"}

    def renew_book(self, book_id):
        """Renews the issued book."""

        book_status = BookController().get_book_by_id(book_id)
    
        if not book_status:
            return {"success": False, "message": "Book not found in the system!"}

        if book_status["isAvail"]: 
            return {"success": False, "message": "Book is not issued to be renewed."}
        
        query = "UPDATE tbl_issue SET issueTime = ?, renewCount = renewCount + 1 WHERE bookID = ?"
        values = (datetime.now(), book_id)
        self.db.execute_query(query, values)
        return {"success": True, "message": "Book renewed successfully!"}

    def get_issued_books(self):
        """Fetches all issued books."""
        query = "SELECT * FROM tbl_issue"
        books = self.db.fetch_data(query)
        if books is not None and len(books) == 0:
            return  {"success": False, "message": "No books issued"}
        return  {"success": True, "books": books, "message": "All books fetched!"}
