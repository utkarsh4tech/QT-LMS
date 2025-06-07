# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewMember.ui'
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
from PySide6.QtWidgets import (QApplication,QMessageBox, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from src.controllers.member_controller import MemberController

class Member_UI(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 450)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.view_members)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"View Members", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        if ___qtablewidgetitem:
            ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        if ___qtablewidgetitem1:
            ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        if ___qtablewidgetitem2:
            ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Mobile", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        if ___qtablewidgetitem3:
            ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Email", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"View Members", None))
    # retranslateUi

    def view_members(self):
        """Fetch members from the database and populate QTableWidget."""
        controller = MemberController()
        members = controller.get_members()

        # Handle case where no members exist
        if not members: 
            QMessageBox.critical(None, "No Members", "No members found in the database.") 
            self.tableWidget.setRowCount(0)
            return

        # Set table properties
        self.tableWidget.setRowCount(len(members))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Mobile", "Email"])

        # Populate table with member data
        for row, member in enumerate(members):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(member["id"])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(member["name"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(member["mobile"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(member["email"]))