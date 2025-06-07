from src.db_manager import db_manager
from datetime import datetime

class IssueController:
    def __init__(self):
        self.db = db_manager

    def issue_book(self, book_id, member_id):
        """Issues a book to a member."""
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
        query_delete = "DELETE FROM tbl_issue WHERE bookID = ?"
        query_update = "UPDATE tbl_addbook SET isAvail = TRUE WHERE id = ?"

        self.db.execute_query(query_delete, (book_id,))
        self.db.execute_query(query_update, (book_id,))
        return {"success": True, "message": "Book returned successfully!"}

    def renew_book(self, book_id):
        """Renews the issued book."""
        query = "UPDATE tbl_issue SET issueTime = ?, renewCount = renewCount + 1 WHERE bookID = ?"
        values = (datetime.now(), book_id)
        self.db.execute_query(query, values)
        return {"success": True, "message": "Book renewed successfully!"}

    def get_issued_books(self):
        """Fetches all issued books."""
        query = "SELECT * FROM tbl_issue"
        return self.db.fetch_data(query)
