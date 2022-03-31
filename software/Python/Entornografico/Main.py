import threading
import serial
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
t = threading.Thread(target=""""funcion de este hilo """)
#t.start()       #start hilo
#pyuic5 -x main.ui -o mainw.py
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui',self)
        self.pushButton.clicked.connect(self.hola)
        self.pos = 90
        self.pos1 = 350
    def hola(self):
        self.pos=self.pos+10
        self.pos1=self.pos1+10
        print(str(self.pos))
        print(str(self.pos1))
        self.label_2.move(self.pos, self.pos1)
        #self.label_2.setGeometry(QtCore.QRect(100, 20, 111, 131))
app=QApplication([])
window=MainWindows()
window.show()
app.exec_()

