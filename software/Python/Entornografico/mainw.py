# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

##
from PyQt5 import QtCore, QtGui, QtWidgets
##from PyQt5.QtGui import QPixmap,QPainter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setAutoFillBackground(False)
        self.fondo=QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, MainWindow.width(),MainWindow.height()))
        self.fondo.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.fondo.setScaledContents(True)
        #MainWindow.setStyleSheet("background-image: url(fondo.jpg); background-repeat: no-repeat; background-position: center;")
        print (MainWindow.width(),MainWindow.height())
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 231, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 350, 111, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("483625.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffaa00;\">Hola Mundo</span></p></body></html>"))


    def resizeEvent(self, e):
        print (e.width(),e.height())

        fondo.resize(e.width(),e.height())
    def mousePressEvent(self,e):
        if e.button()==Qt.LeftButton:
            print("Botó esquerre")
        elif e.button()==Qt.RightButton:
            print("Botó dret")
        elif e.button()==Qt.MidButton:
            print("Botó mig")

    def mouseMoveEvent(self,e):
        print(e.x(),e.y())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

