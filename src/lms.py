from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox

from src.py.main_gui import Ui_MainWindow
from src.py.AddBook import Add_Dialog
from src.py.AddMember import Member_Dialog
from src.py.ViewBook import View_Dialog
from src.py.ViewMember import Member_UI

from src.controllers.book_controller import BookController
from src.controllers.member_controller import MemberController
from src.controllers.issue_controller import IssueController

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)
        self.toolButton_addMember.clicked.connect(self.add_member)
        self.toolButton_viewBooks.clicked.connect(self.view_books)
        self.toolButton_viewMembers.clicked.connect(self.view_members)

        self.book_id.returnPressed.connect(self.get_book_by_id)
        self.member_id.returnPressed.connect(self.get_member_by_id)
        self.toolButton_issueBook.clicked.connect(self.issue_book)

    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()   

    def add_member(self):
        dialog = QDialog()
        ui = Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_books(self):
        dialog = QDialog()
        ui = View_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def view_members(self):
        dialog = QDialog()
        ui = Member_UI()
        ui.setupUi(dialog)
        dialog.exec()

    def get_book_by_id(self):
        book_id = self.book_id.text()
        if (book_id=="") or (book_id.isnumeric()==False):
            QMessageBox.critical(self, "Wrong Book ID" , f"Either Empty or Non Numeric")
            self.book_id.clear()
        else:
            result = BookController().get_book_by_id(book_id)
            if result is not None:
                QMessageBox.information(self, "Book Found!!!" , f"Book with ID : {book_id} sucessfully fetched")
                self.label_bookName.setText("Book Name : \n" + result['title'])
                self.label_bookAuthor.setText("Book Author : \n" + result['author'])
            else:
                QMessageBox.critical(self, "Invalid Book ID" , f"Book with ID : {book_id} does not exist.")
                self.book_id.clear()
        
    def get_member_by_id(self):
        mem_id = self.member_id.text()
        if (mem_id=="") or (mem_id.isnumeric()==False):
            QMessageBox.critical(self, "Wrong Book ID" , f"Either Empty or Non Numeric")
            self.member_id.clear()
        else:
            result = MemberController().get_member_by_id(mem_id)
        
            if result is not None:
                QMessageBox.information(self, "Member Found!!!" , f"Member with ID : {mem_id} sucessfully fetched")
                self.label_memberName.setText("Member Name : \n" + result['name'])
                self.label_memberContact.setText("Member Contact : \n" + result['email'])
            else:
                QMessageBox.critical(self, "Invalid Member ID" , f"Member with ID : {mem_id} does not exist.")
                self.member_id.clear()
            
    def issue_book(self):
        b_id = self.book_id.text()
        m_id = self.member_id.text()
        result = IssueController().issue_book(b_id,m_id)
        if result["success"]:
            QMessageBox.information(self, "Issue Book", "Book issued successfully")
            self.book_id.clear()
            self.member_id.clear()
        else:
            QMessageBox.critical(self, "Issue Book", "Book could not be issued successfully")
