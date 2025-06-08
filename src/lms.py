from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox , QTableWidgetItem
from PySide6.QtGui import QColor, QFont

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
        self.book_id_2.returnPressed.connect(self.load_issued)
        self.toolButton_submit.clicked.connect(self.submit_issued)
        self.toolButton_renew.clicked.connect(self.renew_book)

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

        if not book_id.isnumeric():
            QMessageBox.critical(self, "Wrong Book ID" , f"Book ID either Empty or Non Numeric")
            self.book_id.clear()
            self.label_bookName.setText("Book Name")
            self.label_bookAuthor.setText("Book Author")
            return

        result = BookController().get_book_by_id(book_id)
        if result is not None:
            QMessageBox.information(self, "Book Found!!!" , f"Book with ID : {book_id} sucessfully fetched")
            self.label_bookName.setText("Book Name : \n" + result['title'])
            self.label_bookAuthor.setText("Book Author : \n" + result['author'])
        else:
            QMessageBox.critical(self, "Invalid Book ID" , f"Book with ID : {book_id} does not exist.")
            self.book_id.clear()
            self.label_bookName.setText("Book Name")
            self.label_bookAuthor.setText("Book Author")
    
    def get_member_by_id(self):
        mem_id = self.member_id.text()
        
        if not mem_id.isnumeric():
            QMessageBox.critical(self, "Wrong Book ID" , f"Member ID either Empty or Non Numeric")
            self.member_id.clear()
            self.label_memberName.setText("Member Name")
            self.label_memberContact.setText("Member Contact")
            return
        
        result = MemberController().get_member_by_id(mem_id)
        
        if result is not None:
            QMessageBox.information(self, "Member Found!!!" , f"Member with ID : {mem_id} sucessfully fetched")
            self.label_memberName.setText("Member Name : \n" + result['name'])
            self.label_memberContact.setText("Member Contact : \n" + result['email'])
        else:
            QMessageBox.critical(self, "Invalid Member ID" , f"Member with ID : {mem_id} does not exist.")
            self.member_id.clear()
            self.label_memberName.setText("Member Name")
            self.label_memberContact.setText("Member Contact")
        
    def issue_book(self):

        b_id = self.book_id.text()
        m_id = self.member_id.text()

        if not b_id.isnumeric() or not m_id.isnumeric():
            QMessageBox.critical(self, "Issue Book", "Both Book id and Member id need to be present and should be a Number")
            return
        
        result = IssueController().issue_book(b_id,m_id)
        
        if result["success"]:
            QMessageBox.information(self, "Issue Book", result["message"])
            self.book_id.clear()
            self.member_id.clear()
            return
        else:
            QMessageBox.critical(self, "Issue Book", result["message"])
        
        self.label_memberName.setText("Member Name")
        self.label_memberContact.setText("Member Contact")
        self.label_bookName.setText("Book Name")
        self.label_bookAuthor.setText("Book Author")

    def load_issued(self):
        issued_id = self.book_id_2.text()
        if not issued_id.isnumeric():
            QMessageBox.critical(self, "Issued Books", "Book id need to be present and should be a Number")
            return
        
        result = IssueController().get_issued_books()

        self.tableWidget_bookinfo.setRowCount(0)

        if result["success"]==False:
            QMessageBox.critical(self, "All Issued Books", result["message"])
            return
        
        books = result["books"]

        for row_number, book_data in enumerate(books):
            self.tableWidget_bookinfo.insertRow(row_number)

            for column_number, (column_name, data) in enumerate(book_data.items()):
                item = QTableWidgetItem(str(data))

            
                if book_data["bookID"] == int(issued_id):
                    item.setBackground(QColor("lightblue"))  
                    item.setForeground(QColor("black"))  

                self.tableWidget_bookinfo.setItem(row_number, column_number, item)

    def submit_issued(self):
        issued_id = self.book_id_2.text()

        if not issued_id.isnumeric():
            QMessageBox.critical(self, "Issued Books", "Book id need to be present and should be a Number")
            return

        result = IssueController().return_book(issued_id)

        if result["success"]:
            QMessageBox.information(self, "Submit Book", result["message"])
            self.load_issued()
            return
        else:
            QMessageBox.critical(self, "Submit Book", result["message"])
            return
    
    def renew_book(self):
        issued_id = self.book_id_2.text()

        if not issued_id.isnumeric():
            QMessageBox.critical(self, "Issued Books", "Book id need to be present and should be a Number")
            return
        
        result = IssueController().renew_book(issued_id)

        if result["success"]:
            QMessageBox.information(self, "Submit Book", result["message"])
            self.load_issued()
            return
        else:
            QMessageBox.critical(self, "Submit Book", result["message"])
            return