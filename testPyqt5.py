from PyQt5.QtSql import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('yelpdb.clzycvghm6ps.us-east-2.rds.amazonaws.com')

db.setDatabaseName(input('DB name is: '))
db.setUserName(input('User name is: '))
db.setPassword(input('PW is: '))
print(db.open())


#query = QSqlQuery(db)
#query.exec("SELECT name, salary FROM employee WHERE salary > 50000");

sqlTableModel = QSqlTableModel(db)
sqlTableModel.setTable('user')

