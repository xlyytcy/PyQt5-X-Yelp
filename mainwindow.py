# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.overallTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.overallTabs.setGeometry(QtCore.QRect(10, -20, 760, 657))
        self.overallTabs.setAutoFillBackground(True)
        self.overallTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.overallTabs.setUsesScrollButtons(True)
        self.overallTabs.setMovable(True)
        self.overallTabs.setTabBarAutoHide(True)
        self.overallTabs.setObjectName("overallTabs")
        self.UserTab = QtWidgets.QWidget()
        self.UserTab.setObjectName("UserTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.UserTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_User = QtWidgets.QGridLayout()
        self.gridLayout_User.setObjectName("gridLayout_User")
        self.PB_connectDB = QtWidgets.QPushButton(self.UserTab)
        self.PB_connectDB.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_connectDB.setFont(font)
        self.PB_connectDB.setObjectName("PB_connectDB")
        self.gridLayout_User.addWidget(self.PB_connectDB, 1, 0, 2, 2)
        self.searchBox_User = QtWidgets.QLineEdit(self.UserTab)
        self.searchBox_User.setObjectName("searchBox_User")
        self.gridLayout_User.addWidget(self.searchBox_User, 1, 2, 2, 1)
        self.label_UserID = QtWidgets.QLabel(self.UserTab)
        self.label_UserID.setObjectName("label_UserID")
        self.gridLayout_User.addWidget(self.label_UserID, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.PB_searchUser = QtWidgets.QPushButton(self.UserTab)
        self.PB_searchUser.setObjectName("PB_searchUser")
        self.gridLayout_User.addWidget(self.PB_searchUser, 1, 3, 2, 1)
        self.PB_DBserver = QtWidgets.QPushButton(self.UserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_DBserver.sizePolicy().hasHeightForWidth())
        self.PB_DBserver.setSizePolicy(sizePolicy)
        self.PB_DBserver.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PB_DBserver.setAutoDefault(False)
        self.PB_DBserver.setDefault(False)
        self.PB_DBserver.setFlat(False)
        self.PB_DBserver.setObjectName("PB_DBserver")
        self.gridLayout_User.addWidget(self.PB_DBserver, 0, 0, 1, 2)
        self.tbView_User = QtWidgets.QTableView(self.UserTab)
        self.tbView_User.setObjectName("tbView_User")
        self.gridLayout_User.addWidget(self.tbView_User, 3, 0, 1, 4)
        self.gridLayout_3.addLayout(self.gridLayout_User, 0, 1, 1, 1)
        self.overallTabs.addTab(self.UserTab, "")
        self.BusinessTab = QtWidgets.QWidget()
        self.BusinessTab.setObjectName("BusinessTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.BusinessTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_Business = QtWidgets.QGridLayout()
        self.gridLayout_Business.setObjectName("gridLayout_Business")
        self.editableTableView = QtWidgets.QTableView(self.BusinessTab)
        self.editableTableView.setObjectName("editableTableView")
        self.gridLayout_Business.addWidget(self.editableTableView, 2, 0, 1, 2)
        self.lineEdit_businessID = QtWidgets.QLineEdit(self.BusinessTab)
        self.lineEdit_businessID.setObjectName("lineEdit_businessID")
        self.gridLayout_Business.addWidget(self.lineEdit_businessID, 1, 0, 1, 1)
        self.PB_searchBusiness = QtWidgets.QPushButton(self.BusinessTab)
        self.PB_searchBusiness.setObjectName("PB_searchBusiness")
        self.gridLayout_Business.addWidget(self.PB_searchBusiness, 1, 1, 1, 1)
        self.label_businessSearch = QtWidgets.QLabel(self.BusinessTab)
        self.label_businessSearch.setObjectName("label_businessSearch")
        self.gridLayout_Business.addWidget(self.label_businessSearch, 0, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_Business, 0, 0, 1, 1)
        self.overallTabs.addTab(self.BusinessTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.overallTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB_connectDB.setText(_translate("MainWindow", "Connect"))
        self.label_UserID.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">User Search by ID</span></p></body></html>"))
        self.PB_searchUser.setText(_translate("MainWindow", "Find"))
        self.PB_DBserver.setText(_translate("MainWindow", "DB Server"))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.UserTab), _translate("MainWindow", "Grading"))
        self.PB_searchBusiness.setText(_translate("MainWindow", "PushButton"))
        self.label_businessSearch.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Business Search by ID</span></p></body></html>"))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.BusinessTab), _translate("MainWindow", "Edit DB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

