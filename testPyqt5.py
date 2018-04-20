from PyQt5.QtSql import *

db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName("yelpdb.clzycvghm6ps.us-east-2.rds.amazonaws.com")

db.setDatabaseName(input('DB name is: '))
db.setUserName(input('User name is: '))
db.setPassword(input('PW is: '))
db.open()