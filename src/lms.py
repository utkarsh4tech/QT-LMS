from PySide6.QtWidgets import QMainWindow, QDialog

from src.py.main_gui import Ui_MainWindow
from src.py.AddBook import Add_Dialog
from src.py.AddMember import Member_Dialog
from src.py.ViewBook import View_Dialog
from src.py.ViewMember import Member_UI

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)
        self.toolButton_addMember.clicked.connect(self.add_member)
        self.toolButton_viewBooks.clicked.connect(self.view_books)
        self.toolButton_viewMembers.clicked.connect(self.view_members)

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
