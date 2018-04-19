import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  self.setWindowTitle("Insertar datos") #Título
  self.resize(300, 300) #Tamaño inicial
  self.setMinimumSize(300, 300) #Tamaño mínimo
  self.setMaximumSize(300, 300) #Tamaño máximo
  self.layout = QGridLayout() #Crear un layout grid
  self.setLayout(self.layout) #Agregar el layout al cuadro de diálogo
  self.label_nombre = QLabel("Nombre:") #Etiqueta nombre
  self.txt_nombre = QLineEdit() #Campo para ingresar el nombre
  self.label_edad = QLabel("Edad:") #Etiqueta edad
  self.txt_edad = QSpinBox() #Campo para ingresar la edad
  #Botones
  self.btn_insertar = QPushButton("Insertar")
  self.btn_cancelar = QPushButton("Cancelar")
  #Agregar elementos al layout divido en dos columnas
  self.layout.addWidget(self.label_nombre, 1, 1)
  self.layout.addWidget(self.txt_nombre, 1, 2)
  self.layout.addWidget(self.label_edad, 2, 1)
  self.layout.addWidget(self.txt_edad, 2, 2)
  self.layoutButton = QGridLayout() #Layout para agrupar los botones
  #Agregar los botones al layoutButton
  self.layoutButton.addWidget(self.btn_insertar, 1, 1)
  self.layoutButton.addWidget(self.btn_cancelar, 1, 2)
  #Agregar el layoutButton en la fila 3 columna 2
  self.layout.addLayout(self.layoutButton, 3, 2)

  #Establecer conexión a la base de datos MySql
  self.db = QSqlDatabase.addDatabase("QMYSQL")
  self.db.setHostName("localhost")
  self.db.setDatabaseName("usuarios")
  self.db.setUserName("root")
  self.db.setPassword("")

  self.btn_insertar.clicked.connect(self.Insertar)
  self.btn_cancelar.clicked.connect(self.Cancelar)

 def Insertar(self):
  estado = self.db.open()
  if estado == False:
   QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
  else:
   nombre = self.txt_nombre.text()
   edad = self.txt_edad.text()
   sql = "INSERT INTO usuarios(nombre, edad) VALUES (:nombre, :edad)"
   consulta = QSqlQuery()
   consulta.prepare(sql)
   consulta.bindValue(":nombre", nombre)
   consulta.bindValue(":edad", edad)
   estado = consulta.exec_()
   if estado == True:
    QMessageBox.information(self, "Correcto", "Datos guardados", QMessageBox.Discard)
   else:
    QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)

   self.db.close()

 def Cancelar(self):
  self.close()

app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()