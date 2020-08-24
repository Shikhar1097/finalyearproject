# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderbyclause.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from display import Ui_display
import sqlite3

class Ui_orderbyclause(QWidget):
    dbname=""
    orderbyclause=None
    def setupUi(self, orderbyclause,dbname):
        orderbyclause.setObjectName("orderbyclause")
        orderbyclause.resize(454, 275)
        orderbyclause.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(orderbyclause)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.selectentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.selectentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.selectentry.setObjectName("selectentry")
        self.gridLayout.addWidget(self.selectentry, 0, 2, 1, 1)
        self.orderbyentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.orderbyentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.orderbyentry.setObjectName("orderbyentry")
        self.gridLayout.addWidget(self.orderbyentry, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.fromentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fromentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.fromentry.setObjectName("fromentry")
        self.gridLayout.addWidget(self.fromentry, 1, 2, 1, 1)
        self.whereentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.whereentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.whereentry.setObjectName("whereentry")
        self.gridLayout.addWidget(self.whereentry, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.execute = QtWidgets.QPushButton(self.centralwidget)
        self.execute.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.execute.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.execute.setObjectName("execute")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(370, 240, 75, 23))
        self.reset.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.reset.setObjectName("reset")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 220, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        orderbyclause.setCentralWidget(self.centralwidget)

        self.retranslateUi(orderbyclause)
        QtCore.QMetaObject.connectSlotsByName(orderbyclause)
        orderbyclause.setFixedSize(454,275)


        self.orderbyclause=orderbyclause
        self.dbname=dbname
        self.selectentry.setFocus()


        self.reset.clicked.connect(self.resetevent)
        self.execute.clicked.connect(self.executeevent)
        QMessageBox.about(self, "Message", "Enter '-' in where clause if where is not required.")


    def resetevent(self):
        self.selectentry.setText("")
        self.fromentry.setText("")
        self.whereentry.setText("")
        self.orderbyentry.setText("")
        self.selectentry.setFocus()


    def executeevent(self):
        se=self.selectentry.text()
        fe=self.fromentry.text()
        we=self.whereentry.text()
        obe=self.orderbyentry.text()
        if we=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif se=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif fe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif obe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        else:
            if we=="-":
                query="SELECT "+se+" FROM "+fe+" ORDER BY "+obe+";"
            else:
                query="SELECT "+se+" FROM "+fe+" WHERE "+we+" ORDER BY "+obe+";"
            cn=sqlite3.connect(self.dbname+'.db')
            crob=cn.cursor()
            crob.execute(query)
            result=crob.fetchall()
            cn.commit()
            cn.close()
                
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_display()
            self.ui.setupUi(self.window,result)
            self.window.show()
            self.orderbyclause.close()






        

    def retranslateUi(self, orderbyclause):
        _translate = QtCore.QCoreApplication.translate
        orderbyclause.setWindowTitle(_translate("orderbyclause", "ORDER BY"))
        self.label_4.setText(_translate("orderbyclause", "ORDER BY"))
        self.label.setText(_translate("orderbyclause", "SELECT"))
        self.label_3.setText(_translate("orderbyclause", "WHERE"))
        self.label_2.setText(_translate("orderbyclause", "FROM"))
        self.execute.setText(_translate("orderbyclause", "Execute"))
        self.reset.setText(_translate("orderbyclause", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderbyclause = QtWidgets.QMainWindow()
    ui = Ui_orderbyclause()
    ui.setupUi(orderbyclause)
    orderbyclause.show()
    sys.exit(app.exec_())

