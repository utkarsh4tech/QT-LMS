# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddMember.ui'
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

from src.controllers.member_controller import MemberController
from src.models import Member
from pydantic import ValidationError

class Member_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_mid = QLineEdit(Dialog)
        self.lineEdit_mid.setObjectName(u"lineEdit_mid")
        self.lineEdit_mid.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit_mid.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_mid)

        self.lineEdit_mname = QLineEdit(Dialog)
        self.lineEdit_mname.setObjectName(u"lineEdit_mname")
        self.lineEdit_mname.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_mname.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_mname)

        self.lineEdit_mmobile = QLineEdit(Dialog)
        self.lineEdit_mmobile.setObjectName(u"lineEdit_mmobile")
        self.lineEdit_mmobile.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_mmobile.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_mmobile)

        self.lineEdit_memail = QLineEdit(Dialog)
        self.lineEdit_memail.setObjectName(u"lineEdit_memail")
        self.lineEdit_memail.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_memail.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_memail)

        self.pushButton_save = QPushButton(Dialog)
        self.pushButton_save.setObjectName(u"pushButton_save")
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_save.setFont(font1)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:gray;\n"
"color:white\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_save)

        self.label_result = QLabel(Dialog)
        self.label_result.setObjectName(u"label_result")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_result.setFont(font2)

        self.verticalLayout.addWidget(self.label_result)

        self.pushButton_save.clicked.connect(self.insert_member)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Insert Member", None))
        self.lineEdit_mid.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Member ID", None))
        self.lineEdit_mname.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Member Name", None))
        self.lineEdit_mmobile.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Member Mobile", None))
        self.lineEdit_memail.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please Enter Member Email", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog", u"Insert Member", None))
        self.label_result.setText("")
    # retranslateUi

    def insert_member(self):
        """Handles member insertion with validation & user feedback."""

        # Fetch input values
        member_id = self.lineEdit_mid.text().strip()
        name = self.lineEdit_mname.text().strip()
        mobile = self.lineEdit_mmobile.text().strip()
        email = self.lineEdit_memail.text().strip()

        try:
            
            if not all([member_id, name, mobile, email]):
                raise ValueError("Please fill in all fields.")
            
            if not member_id.isnumeric():
                raise ValueError("ID must be a number.")
            
        except ValueError as e:
            QMessageBox.critical(self, "Data not correct", str(e))
            self.label_result.setText(str(e))
            self.label_result.setStyleSheet("color:red")
            return
        
        try:
            member = Member(id=int(member_id), name=name, mobile=mobile, email=email)
        
        except ValidationError as e:
            errors = [f"Field '{error['loc'][0]}': \n {error['msg']} (Input: {error['input']})" for error in e.errors()]
            err_msg = "\n\n".join(errors) 
            self.label_result.setText(err_msg)
            self.label_result.setStyleSheet("color:red")
            return
        
        controller = MemberController()
        result = controller.add_member(member)

        if result["success"]:
            self.label_result.setText(result["message"])
            self.label_result.setStyleSheet("color:green")
            QMessageBox.information(self, "Member Added", result["message"])
            self.accept()

        else:
            self.label_result.setText(f"Error: {result['message']}")
            self.label_result.setStyleSheet("color:red")

        self.lineEdit_mid.clear()
        self.lineEdit_mname.clear()
        self.lineEdit_mmobile.clear()
        self.lineEdit_memail.clear()
