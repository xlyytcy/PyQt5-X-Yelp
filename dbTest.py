from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView, QApplication
import sys

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("yelp_db")
db.setUserName("root")
db.setPassword("")
db.open()

testModel = QSqlTableModel()
testModel.setTable("checkin")
testModel.setEditStrategy(QSqlTableModel.OnFieldChange)
testModel.select()

testView = QTableView()
testtView.setModel(testModel)

app.exec_()

#install_name_tool -change /opt/local/lib/mysql55/mysql/libmysqlclient.18.dylib /usr/local/mysql/lib/libmysqlclient.20.dylib /Users/XG/Qt/5.10.1/clang_64/plugins/sqldrivers/libqsqlmysql.dylib
#install_name_tool -change /opt/local/lib/mysql55/mysql/libmysqlclient.18.dylib /usr/local/Cellar/mysql/5.7.10/lib/libmysqlclient.dylib libqsqlmysql.dylib


#install_name_tool -change /usr/local/Cellar/mysql/5.7.21/lib/libmysqlclient.dylib /usr/local/Cellar/mysql/5.7.21/lib/libmysqlclient.20.dylib libqsqlmysql.dylib

i#nstall_name_tool -change libqsqlmysql_debug.dylib /Users/foob/Qt/5.3/Src/qtbase/plugins/sqldrivers/libqsqlmysql_debug.dylib Qt/5.3/clang_64/plugins/sqldrivers/libqsqlmysql_debug.dylib
