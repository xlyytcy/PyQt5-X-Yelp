# Reference Page.md

### https://dev.mysql.com/doc/refman/5.7/en/set-password.html
~~~ 
- \q to quit
- mysql started XG   /Users/XG/Library/LaunchAgents/homebrew.mxcl.mysql.plist
- brew services list
- mysql.server start/stop to start/stop the server
- mysql -u root -p
~~~





### pyuic
- load ui and convert to python with pyqt5
- pyuic5 -x some.ui -o some.py
- pyuic5 -x mastergui.ui -o mastergui.py && python3 mastergui.py 

<del> 
qmake "INCLUDEPATH+=/usr/local/Cellar/mysql/5.7.21/include" "LIBS+=-L/usr/local/Cellar/mysql/5.7.21/lib -lmysqlclient_r" mysql.pro

/usr/local/Cellar/mysql/5.7.21/lib

otool -L libqsqlmysql.dylib



</del>



<del> Some new thoughts: PyQt5.sql to handle the MYSQL db </del> 

Luckily Pyqt5 connection issue is solved, how painful it was setting up simylink stuff.