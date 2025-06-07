# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowUelEDb.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
from src.py import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 550)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Triangular)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.IssueBook = QWidget()
        self.IssueBook.setObjectName(u"IssueBook")
        self.verticalLayout_4 = QVBoxLayout(self.IssueBook)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.IssueBook)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.book_id = QLineEdit(self.widget)
        self.book_id.setObjectName(u"book_id")
        font1 = QFont()
        font1.setFamilies([u"Academy Engraved LET"])
        font1.setPointSize(14)
        self.book_id.setFont(font1)

        self.horizontalLayout_2.addWidget(self.book_id)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_bookName = QLabel(self.widget)
        self.label_bookName.setObjectName(u"label_bookName")
        self.label_bookName.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_bookName)

        self.label_bookAuthor = QLabel(self.widget)
        self.label_bookAuthor.setObjectName(u"label_bookAuthor")
        self.label_bookAuthor.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_bookAuthor)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget1 = QWidget(self.IssueBook)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.member_id = QLineEdit(self.widget1)
        self.member_id.setObjectName(u"member_id")
        self.member_id.setFont(font1)

        self.horizontalLayout_3.addWidget(self.member_id)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_memberName = QLabel(self.widget1)
        self.label_memberName.setObjectName(u"label_memberName")
        self.label_memberName.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_memberName)

        self.label_memberContact = QLabel(self.widget1)
        self.label_memberContact.setObjectName(u"label_memberContact")
        self.label_memberContact.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_memberContact)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.widget1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.toolButton_issueBook = QToolButton(self.IssueBook)
        self.toolButton_issueBook.setObjectName(u"toolButton_issueBook")
        self.toolButton_issueBook.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/src/resources/icons/issue_book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_issueBook.setIcon(icon)
        self.toolButton_issueBook.setIconSize(QSize(36, 36))
        self.toolButton_issueBook.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.toolButton_issueBook)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.IssueBook, "")
        self.Submit_Renew = QWidget()
        self.Submit_Renew.setObjectName(u"Submit_Renew")
        self.verticalLayout_5 = QVBoxLayout(self.Submit_Renew)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.book_id_2 = QLineEdit(self.Submit_Renew)
        self.book_id_2.setObjectName(u"book_id_2")
        self.book_id_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.book_id_2)

        self.tableWidget_bookinfo = QTableWidget(self.Submit_Renew)
        if (self.tableWidget_bookinfo.columnCount() < 4):
            self.tableWidget_bookinfo.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_bookinfo.setObjectName(u"tableWidget_bookinfo")
        self.tableWidget_bookinfo.setFont(font1)
        self.tableWidget_bookinfo.horizontalHeader().setDefaultSectionSize(185)

        self.verticalLayout_5.addWidget(self.tableWidget_bookinfo)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.toolButton_renew = QToolButton(self.Submit_Renew)
        self.toolButton_renew.setObjectName(u"toolButton_renew")
        self.toolButton_renew.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/src/resources/icons/renew_book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_renew.setIcon(icon1)
        self.toolButton_renew.setIconSize(QSize(36, 36))
        self.toolButton_renew.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.toolButton_renew)

        self.toolButton_submit = QToolButton(self.Submit_Renew)
        self.toolButton_submit.setObjectName(u"toolButton_submit")
        self.toolButton_submit.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/src/resources/icons/submit_book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_submit.setIcon(icon2)
        self.toolButton_submit.setIconSize(QSize(36, 36))
        self.toolButton_submit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.toolButton_submit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.Submit_Renew, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton_addBook = QToolButton(self.centralwidget)
        self.toolButton_addBook.setObjectName(u"toolButton_addBook")
        self.toolButton_addBook.setMaximumSize(QSize(145, 145))
        self.toolButton_addBook.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/src/resources/icons/add_book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_addBook.setIcon(icon3)
        self.toolButton_addBook.setIconSize(QSize(68, 68))
        self.toolButton_addBook.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.toolButton_addBook)

        self.toolButton_addMember = QToolButton(self.centralwidget)
        self.toolButton_addMember.setObjectName(u"toolButton_addMember")
        self.toolButton_addMember.setMaximumSize(QSize(145, 145))
        self.toolButton_addMember.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/src/resources/icons/add_member.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_addMember.setIcon(icon4)
        self.toolButton_addMember.setIconSize(QSize(68, 68))
        self.toolButton_addMember.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.toolButton_addMember)

        self.toolButton_viewBooks = QToolButton(self.centralwidget)
        self.toolButton_viewBooks.setObjectName(u"toolButton_viewBooks")
        self.toolButton_viewBooks.setMaximumSize(QSize(145, 145))
        self.toolButton_viewBooks.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/src/resources/icons/view_book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_viewBooks.setIcon(icon5)
        self.toolButton_viewBooks.setIconSize(QSize(68, 68))
        self.toolButton_viewBooks.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.toolButton_viewBooks)

        self.toolButton_viewMembers = QToolButton(self.centralwidget)
        self.toolButton_viewMembers.setObjectName(u"toolButton_viewMembers")
        self.toolButton_viewMembers.setMaximumSize(QSize(145, 145))
        self.toolButton_viewMembers.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/src/resources/icons/view_person.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_viewMembers.setIcon(icon6)
        self.toolButton_viewMembers.setIconSize(QSize(68, 68))
        self.toolButton_viewMembers.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.toolButton_viewMembers)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qt-LMS", None))
        self.book_id.setText("")
        self.book_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter Book Id", None))
        self.label_bookName.setText(QCoreApplication.translate("MainWindow", u"Book name", None))
        self.label_bookAuthor.setText(QCoreApplication.translate("MainWindow", u"Book Author", None))
        self.member_id.setText("")
        self.member_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter Member Id", None))
        self.label_memberName.setText(QCoreApplication.translate("MainWindow", u"Member Name", None))
        self.label_memberContact.setText(QCoreApplication.translate("MainWindow", u"Member Contact", None))
        self.toolButton_issueBook.setText(QCoreApplication.translate("MainWindow", u"Issue Book", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IssueBook), QCoreApplication.translate("MainWindow", u"Issue Book", None))
        self.book_id_2.setText("")
        self.book_id_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter Book Id", None))
        ___qtablewidgetitem = self.tableWidget_bookinfo.horizontalHeaderItem(0)
        if ___qtablewidgetitem is not None:
            ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem1 = self.tableWidget_bookinfo.horizontalHeaderItem(1)
        if ___qtablewidgetitem1 is not None:
            ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Member ID", None));
        ___qtablewidgetitem2 = self.tableWidget_bookinfo.horizontalHeaderItem(2)
        if ___qtablewidgetitem2 is not None:
            ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Issue Time", None));
        ___qtablewidgetitem3 = self.tableWidget_bookinfo.horizontalHeaderItem(3)
        if ___qtablewidgetitem3 is not None:
            ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Renew Count", None));
        self.toolButton_renew.setText(QCoreApplication.translate("MainWindow", u"Renew", None))
        self.toolButton_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Submit_Renew), QCoreApplication.translate("MainWindow", u"Submit / Renew", None))
        self.toolButton_addBook.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.toolButton_addMember.setText(QCoreApplication.translate("MainWindow", u"Add Member", None))
        self.toolButton_viewBooks.setText(QCoreApplication.translate("MainWindow", u"View Books", None))
        self.toolButton_viewMembers.setText(QCoreApplication.translate("MainWindow", u"View Members", None))
    # retranslateUi



