# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_display(QWidget):
    display=None
    def setupUi(self, display,result):
        display.setObjectName("display")
        display.resize(655, 442)
        display.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(display)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 631, 341))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 400, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 12pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        display.setCentralWidget(self.centralwidget)

        self.retranslateUi(display)
        QtCore.QMetaObject.connectSlotsByName(display)
        display.setFixedSize(655,442)










        self.display=display
        self.pushButton.clicked.connect(self.closeevent)


        for entry in result:
            s=""
            for i in entry:
                s=s+str(i)+"\t"
            self.listWidget.addItem(s)
                















    def closeevent(self):
        self.display.close()









        


        

    def retranslateUi(self, display):
        _translate = QtCore.QCoreApplication.translate
        display.setWindowTitle(_translate("display", "Display Selection"))
        self.pushButton.setText(_translate("display", "OK"))
        self.label.setText(_translate("display", "Selections:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    display = QtWidgets.QMainWindow()
    ui = Ui_display()
    ui.setupUi(display)
    display.show()
    sys.exit(app.exec_())

