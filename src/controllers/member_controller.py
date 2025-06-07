from src.db_manager import db_manager
from src.models import Member

class MemberController:
    def __init__(self):
        self.db = db_manager

    def add_member(self, member):
        """Adds a new member to the database after validation."""
        
        existing_member = self.get_member_by_id(member.id)
        if existing_member:
            return {"success": False, "message": f"Member with ID {member.id} already exists!"}
    
        query = "INSERT INTO tbl_addmember (id, name, mobile, email) VALUES (?, ?, ?, ?)"
        values = (member.id, member.name, member.mobile, member.email)
        self.db.execute_query(query, values)
        return {"success": True, "message": "Member added successfully!"}
        

    def get_members(self):
        """Fetches all members from the database."""
        query = "SELECT * FROM tbl_addmember"
        return self.db.fetch_data(query)

    def get_member_by_id(self, member_id):
        """Fetches a single member by ID."""
        query = "SELECT * FROM tbl_addmember WHERE id = ?"
        result = self.db.fetch_data(query, (member_id,))
        if result and len(result) != 0:
            return result[0]
        else: 
            return None
