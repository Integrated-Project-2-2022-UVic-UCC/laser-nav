import threading
import serial
import time
from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.fondo=QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, self.width(),self.height()))
        self.fondo.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.fondo.setScaledContents(True)
        self.label.move(20,20)
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
    def hola(self):
        self.pos=self.pos+10
        self.pos1=self.pos1+10
        print(str(self.pos))
        print(str(self.pos1))
        self.posx= self.pos*self.width()/800
        self.posy= self.pos1*self.height()/601
        self.label_2.move(self.posx, self.posy)


    def resizeEvent(self, e):
        #print (self.width(),self.height())
        #print(self.scale())
        self.fondo.resize(self.width(),self.height())
        self.posx= self.pos*self.width()/800
        self.posy= self.pos1*self.height()/601
        #print(self.pos)
        self.label_2.move(self.posx, self.posy)


        
''' def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap ("fondo.png") # Reemplace la ruta relativa de su propia imagen
        painter.drawPixmap(self.rect(), pixmap)
        #self.label_2.setGeometry(QtCore.QRect(100, 20, 111, 131))'''
app=QApplication([])
window=MainWindows()
window.show()
app.exec_()

