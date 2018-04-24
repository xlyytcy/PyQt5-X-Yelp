# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mastergui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox

#############################################
# Global Variable
db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('yelpdb.clzycvghm6ps.us-east-2.rds.amazonaws.com')
db.setDatabaseName('yelp_db')
userIDtoSearch = ''


#############################################

class Ui_MasterGUI(object):

    def setupUi(self, MasterGUI):
        MasterGUI.setObjectName("MasterGUI")
        MasterGUI.resize(784, 743)
        self.centralWidget = QtWidgets.QWidget(MasterGUI)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.overallTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.overallTabs.setAutoFillBackground(True)
        self.overallTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.overallTabs.setUsesScrollButtons(True)
        self.overallTabs.setMovable(True)
        self.overallTabs.setTabBarAutoHide(True)
        self.overallTabs.setObjectName("overallTabs")
        self.tab_User = QtWidgets.QWidget()
        self.tab_User.setObjectName("tab_User")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_User)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_User = QtWidgets.QGridLayout()
        self.gridLayout_User.setSpacing(6)
        self.gridLayout_User.setObjectName("gridLayout_User")
        self.pb_DBserver = QtWidgets.QPushButton(self.tab_User)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_DBserver.sizePolicy().hasHeightForWidth())
        self.pb_DBserver.setSizePolicy(sizePolicy)
        self.pb_DBserver.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pb_DBserver.setAutoDefault(False)
        self.pb_DBserver.setDefault(False)
        self.pb_DBserver.setFlat(False)
        self.pb_DBserver.setObjectName("pb_DBserver")
        self.gridLayout_User.addWidget(self.pb_DBserver, 0, 0, 3, 2)
        self.pb_searchUser = QtWidgets.QPushButton(self.tab_User)
        self.pb_searchUser.setObjectName("pb_searchUser")
        self.gridLayout_User.addWidget(self.pb_searchUser, 1, 3, 2, 1)
        self.lineEdit_User = QtWidgets.QLineEdit(self.tab_User)
        self.lineEdit_User.setObjectName("lineEdit_User")
        self.gridLayout_User.addWidget(self.lineEdit_User, 1, 2, 2, 1)
        self.label_User = QtWidgets.QLabel(self.tab_User)
        self.label_User.setAlignment(QtCore.Qt.AlignCenter)
        self.label_User.setObjectName("label_User")
        self.gridLayout_User.addWidget(self.label_User, 0, 2, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_User, 0, 1, 1, 1)
        self.tableView_User = QtWidgets.QTableView(self.tab_User)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_User.sizePolicy().hasHeightForWidth())
        self.tableView_User.setSizePolicy(sizePolicy)
        self.tableView_User.setObjectName("tableView_User")
        self.gridLayout_3.addWidget(self.tableView_User, 1, 1, 1, 1)
        ###################### Added another tableView
        self.tableView_User_AllReviews = QtWidgets.QTableView(self.tab_User)
        self.tableView_User_AllReviews.setObjectName("tableView_User_AllReviews")
        ######################
        self.gridLayout_3.addWidget(self.tableView_User_AllReviews, 2, 1, 1, 1)
        self.overallTabs.addTab(self.tab_User, "")
        self.tab_Business = QtWidgets.QWidget()
        self.tab_Business.setObjectName("tab_Business")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_Business)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_Business = QtWidgets.QGridLayout()
        self.gridLayout_Business.setSpacing(6)
        self.gridLayout_Business.setObjectName("gridLayout_Business")
        self.tableView_Business = QtWidgets.QTableView(self.tab_Business)
        self.tableView_Business.setObjectName("tableView_Business")
        self.gridLayout_Business.addWidget(self.tableView_Business, 1, 0, 1, 2)
        self.pb_searchBusiness = QtWidgets.QPushButton(self.tab_Business)
        self.pb_searchBusiness.setObjectName("pb_searchBusiness")
        self.gridLayout_Business.addWidget(self.pb_searchBusiness, 0, 1, 1, 1)
        self.lineEdit_businessInput = QtWidgets.QLineEdit(self.tab_Business)
        self.lineEdit_businessInput.setObjectName("lineEdit_businessInput")
        self.gridLayout_Business.addWidget(self.lineEdit_businessInput, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_Business, 0, 0, 1, 1)
        self.overallTabs.addTab(self.tab_Business, "")
        self.gridLayout_2.addWidget(self.overallTabs, 0, 0, 1, 1)
        MasterGUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MasterGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 784, 22))
        self.menuBar.setObjectName("menuBar")
        MasterGUI.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MasterGUI)
        self.mainToolBar.setObjectName("mainToolBar")
        MasterGUI.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MasterGUI)
        self.statusBar.setObjectName("statusBar")
        MasterGUI.setStatusBar(self.statusBar)

        self.retranslateUi(MasterGUI)
        self.overallTabs.setCurrentIndex(0)
        # self.pb_DBserver.clicked.connect(MasterGUI.close)

        #############################################
        ## Signal and Slots

        # Adding DB connection
        self.pb_DBserver.clicked.connect(self.connectDB)
        self.pb_searchUser.clicked.connect(self.displayUsers)

        #############################################

        QtCore.QMetaObject.connectSlotsByName(MasterGUI)

    def retranslateUi(self, MasterGUI):
        _translate = QtCore.QCoreApplication.translate
        MasterGUI.setWindowTitle(_translate("MasterGUI", "MasterGUI"))
        self.pb_DBserver.setText(_translate("MasterGUI", "DB Server Usr/PW"))
        self.pb_searchUser.setText(_translate("MasterGUI", "Search"))
        self.label_User.setText(_translate("MasterGUI",
                                           "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">User Search</span></p></body></html>"))

        self.overallTabs.setTabText(self.overallTabs.indexOf(self.tab_User), _translate("MasterGUI", "User"))
        self.pb_searchBusiness.setText(_translate("MasterGUI", "Search"))
        self.overallTabs.setTabText(self.overallTabs.indexOf(self.tab_Business), _translate("MasterGUI", "Business"))

    def connectDB(self):
        userName, ok = QInputDialog.getText(MasterGUI, "Input User Name", "User Name:", QLineEdit.Password)

        if ok and userName != '':
            # print(userName)
            db.setUserName(userName)

        passWord, ok = QInputDialog.getText(MasterGUI, "Input Password", "Password:", QLineEdit.Password)

        if ok and passWord != '':
            # print(passWord)
            db.setPassword(passWord)
            print(db.open())

            if db.open() == True:  # Essential to have DB connected
                self.printDBstatusOK()
            else:
                self.printDBstatusNO()

    def printDBstatusOK(self):
        QMessageBox.about(MasterGUI, "DB Status", "DB Connected!")

    def printDBstatusNO(self):
        QMessageBox.about(MasterGUI, "DB Status", "DB connection failed!")

    def displayUsers(self):
        userTableView = self.tableView_User
        userIDtoSearch = str(self.lineEdit_User.text())  # assure this is a string instead of QString

        # QSqlQuery
        queryUser = QSqlQuery()
        queryUser.prepare(" SELECT * FROM user WHERE id = :userIDtoSearch ")
        queryUser.bindValue(":userIDtoSearch", userIDtoSearch)
        queryUser.exec_()

        # QSqlQueryModel
        tablemodel = QSqlQueryModel()
        # if queryUser.exec('SELECT * FROM user WHERE id = :userIDtoSearch'):
        tablemodel.setQuery(queryUser)

        print(userIDtoSearch)
        # tablemodel.setQuery('SELECT * FROM user WHERE id = userIDtoSearch', db)
        # tablemodel.bindValue(":userIDtoSearch", userIDtoSearch)

        userTableView.setModel(tablemodel)
        print(tablemodel.lastError().text())
        userTableView.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MasterGUI = QtWidgets.QMainWindow()
    ui = Ui_MasterGUI()
    ui.setupUi(MasterGUI)
    MasterGUI.show()
    sys.exit(app.exec_())
