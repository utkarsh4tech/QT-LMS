# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddBook.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

from src.controllers.book_controller import BookController
from src.models import Book
from pydantic import ValidationError

class Add_Dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_title = QLineEdit(Dialog)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit_title.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_title)

        self.lineEdit_id = QLineEdit(Dialog)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_id.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_id)

        self.lineEdit_author = QLineEdit(Dialog)
        self.lineEdit_author.setObjectName(u"lineEdit_author")
        self.lineEdit_author.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_author.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_author)

        self.lineEdit_publisher = QLineEdit(Dialog)
        self.lineEdit_publisher.setObjectName(u"lineEdit_publisher")
        self.lineEdit_publisher.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_publisher.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_publisher)

        self.pushButton_insertbook = QPushButton(Dialog)
        self.pushButton_insertbook.setObjectName(u"pushButton_insertbook")
        self.pushButton_insertbook.setFont(font)
        self.pushButton_insertbook.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:gray;\n"
"color:white\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_insertbook)

        self.label_result = QLabel(Dialog)
        self.label_result.setObjectName(u"label_result")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_result.setFont(font1)

        self.verticalLayout.addWidget(self.label_result)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_insertbook.clicked.connect(self.insert_book)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Insert Book", None))
        self.lineEdit_title.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Title", None))
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter ID", None))
        self.lineEdit_author.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Author", None))
        self.lineEdit_publisher.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Publisher", None))
        self.pushButton_insertbook.setText(QCoreApplication.translate("Dialog", u"Insert Book", None))
        self.label_result.setText("")
    # retranslateUi

    def insert_book(self):

        title = self.lineEdit_title.text().strip()
        book_id= self.lineEdit_id.text().strip()
        author = self.lineEdit_author.text().strip()
        publisher = self.lineEdit_publisher.text().strip()
        
        try:

            if not all([title, book_id, author, publisher]):
                raise ValueError("Please fill in all fields.")

            if not book_id.isnumeric():
                raise ValueError("ID must be a number.")

        except ValueError as e:
            QMessageBox.critical(self, "Data not correct", str(e))
            self.label_result.setText(str(e))
            self.label_result.setStyleSheet("color:red")
            return
        
        try:
            book = Book(id=int(book_id), title=title, author=author, publisher=publisher)

        except ValidationError as e:
            errors = [f"Field '{error['loc'][0]}': \n  {error['msg']} (Input: {error['input']})" for error in e.errors()]
            err_msg = "\n\n".join(errors) 
            self.label_result.setText(err_msg)
            self.label_result.setStyleSheet("color:red")
            return

        controller = BookController()
        result = controller.add_book(book)

        if result["success"]:
            QMessageBox.information(self, "Book Added", result["message"])
            self.label_result.setText(result["message"])
            self.label_result.setStyleSheet('color:green')
            
        else:
            QMessageBox.warning(self,"Book Not Added", result["message"])
            self.label_result.setText("Data could not be added successfully because: " + result["message"])
            self.label_result.setStyleSheet('color:Red')   
        
        self.lineEdit_title.clear()
        self.lineEdit_id.clear()
        self.lineEdit_author.clear()
        self.lineEdit_publisher.clear()