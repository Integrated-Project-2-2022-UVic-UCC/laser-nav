import threading
import serial
import sys
import time
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import geometry

#t.start()       #start hilo
#pyuic5 -x main.ui -o mainw.py
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui',self)
        self.pushButton.clicked.connect(self.movee)
        self.recive = False
        self.arduino= False
        self.pos = 90
        self.pos1 = 350
        self.fondo=QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, self.width(),self.height()))
        self.fondo.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_2.setPixmap(QtGui.QPixmap("proto2.png"))
        self.fondo.setScaledContents(True)
        self.label.move(20,20)
        self.label.raise_()
        self.label_2.raise_()
        self.hiloSerial = threading.Thread(target=self.getangles,daemon= True)
        self.hiloCalculos = threading.Thread(target=self.getPos,daemon = True)
        try:
            self.arduino = serial.Serial("COM6",9600,timeout=1.0)
            arduino = True
        except:
          print("arduino no conectado")
        time.sleep(1)

        self.alpha1=0
        self.alpha2=0
        self.alpha3=0
        self.isRun=True
        self.hiloSerial.start()
        self.hiloCalculos.start()
        
        self.pushButton.raise_()
        
    def closeEvent(self,event):
        self.isRun=False
        self.arduino.close()
        self.hiloSerial.join(0.1)
        self.hiloCalculos.join(0.1)
        print("chauuuuuuu")

    def getangles(self):
        while self.isRun and self.arduino:
            
            cad=self.arduino.readline().decode('ascii').strip()
            if cad:
                pos=cad.index(",")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == '0':
                    self.alpha1 = float(value)
                elif label == '1':
                    self.alpha2 = float(value)
                elif label == '2':
                    self.alpha3 = float(value)
                    self.recive = True
                print(label+": "+value)
                
                
    def getPos(self):
        while self.isRun:
            if self.recive:
                pi = 3.141592653589
  
                A = geometry.Vector(2,0)#3,0.5
                B = geometry.Vector(2.25,1.5)#2.25,2
                C = geometry.Vector(0,1.5)#0,1.5
                alpha1=self.alpha2-self.alpha1#26.57*pi/180
                alpha2=self.alpha3-self.alpha2-self.alpha1#270*pi/180
                self.orientacio=self.alpha1

  
                C1,r1 =geometry.find_circle(A,B,alpha1)
                C2,r2 =geometry.find_circle(B,C,alpha2)
                i1,i2 = geometry.circle_intersection(C1,r1,C2,r2)
                print(i2.x)
                self.recive = False
                print("getting pos")
                if i2 == B:
                    self.pos=i1.x-25
                    self.pos1=i1.y-75
                else:
                    self.pos=i2.x-25
                    self.pos1=i2.y-75
                    
                self.orien = 32.01+self.alpha1
                self.posx= self.pos*self.width()/800
                self.posy= self.pos1*self.height()/601
                self.label_2.move(i2.x-25,i2.y-75)
                
        
    def movee(self):
        #self.pos=self.pos+1
        #self.pos1=self.pos1+1
        #self.pos = calculospython4.pos_sensor_x
        #self.pos1 = calculospython4.pos_sensor_x
        #print(str(self.pos))
        #print(str(self.pos1))
        #self.posx= self.pos*self.width()/800
        #self.posy= self.pos1*self.height()/601
        #self.label_2.move(self.posx, self.posy)
        self.recive=True
        print("boton press")


    def resizeEvent(self, e):
        #print (self.width(),self.height())
        #print(self.scale())
        self.fondo.resize(self.width(),self.height())
        self.posx= self.pos*self.width()/800
        self.posy= self.pos1*self.height()/601
        #print(self.pos)
        self.label_2.move(self.posx, self.posy)
    def mouseMoveEvent(self,e):
        self.label_2.move(e.x()-25,e.y()-75)
        self.pos=e.x()-25
        self.pos1=e.y()-75
        #print(label_2.size())

        
''' def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap ("fondo.png") # Reemplace la ruta relativa de su propia imagen
        painter.drawPixmap(self.rect(), pixmap)
        #self.label_2.setGeometry(QtCore.QRect(100, 20, 111, 131))'''
app=QApplication(sys.argv)
window=MainWindows()
window.show()
sys.exit(app.exec_())


