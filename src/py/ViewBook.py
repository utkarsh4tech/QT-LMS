# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewBook.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog,QMessageBox, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from src.controllers.book_controller import BookController

class View_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 450)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        
        self.pushButton.clicked.connect(self.view_books)
        
        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"View Books", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        if ___qtablewidgetitem is not None:
            ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Title", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        if ___qtablewidgetitem1 is not None:
            ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        if ___qtablewidgetitem2 is not None:
            ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Author", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        if ___qtablewidgetitem3 is not None:
            ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Publisher", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        if ___qtablewidgetitem4 is not None:
            ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Available", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"View Books", None))
    # retranslateUi

    def view_books(self):
        """Fetch books from database and populate QTableWidget."""
        controller = BookController()
        books = controller.get_books()

        # Handle case where no books exist
        if not books:
            QMessageBox.warning(None, "No Books", "No books found in the database.")
            self.tableWidget.setRowCount(0)
            return

        # Set table properties
        self.tableWidget.setRowCount(len(books))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Title", "ID", "Author", "Publisher", "Available"])

        # Populate table with book data
        for row, book in enumerate(books):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(book["title"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(book["id"])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(book["author"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(book["publisher"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem("Yes" if book["isAvail"] else "No"))


