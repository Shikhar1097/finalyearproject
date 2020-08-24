# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'havingclause.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from display import Ui_display
import sqlite3

class Ui_havingclause(QWidget):
    dbname=""
    havingclause=""
    def setupUi(self, havingclause,dbname):
        havingclause.setObjectName("havingclause")
        havingclause.resize(454, 277)
        havingclause.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(havingclause)
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
        self.havingentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.havingentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.havingentry.setObjectName("havingentry")
        self.gridLayout.addWidget(self.havingentry, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.fromentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fromentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.fromentry.setObjectName("fromentry")
        self.gridLayout.addWidget(self.fromentry, 1, 2, 1, 1)
        self.groupbyentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.groupbyentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.groupbyentry.setObjectName("groupbyentry")
        self.gridLayout.addWidget(self.groupbyentry, 2, 2, 1, 1)
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
        havingclause.setCentralWidget(self.centralwidget)

        self.retranslateUi(havingclause)
        QtCore.QMetaObject.connectSlotsByName(havingclause)



        havingclause.setFixedSize(454,277)


        self.havingclause=havingclause
        self.dbname=dbname
        self.selectentry.setFocus()


        self.reset.clicked.connect(self.resetevent)
        self.execute.clicked.connect(self.executeevent)


    def resetevent(self):
        self.selectentry.setText("")
        self.fromentry.setText("")
        self.groupbyentry.setText("")
        self.havingentry.setText("")
        self.selectentry.setFocus()

    def executeevent(self):
        se=self.selectentry.text()
        fe=self.fromentry.text()
        gbe=self.groupbyentry.text()
        he=self.havingentry.text()
        if he=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif se=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif fe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif gbe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        else:
            query="SELECT "+se+" FROM "+fe+" GROUP BY "+gbe+" HAVING "+he+";"
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
            self.havingclause.close()

    def retranslateUi(self, havingclause):
        _translate = QtCore.QCoreApplication.translate
        havingclause.setWindowTitle(_translate("havingclause", "HAVING"))
        self.label_4.setText(_translate("havingclause", "HAVING"))
        self.label.setText(_translate("havingclause", "SELECT"))
        self.label_3.setText(_translate("havingclause", "GROUP BY"))
        self.label_2.setText(_translate("havingclause", "FROM"))
        self.execute.setText(_translate("havingclause", "Execute"))
        self.reset.setText(_translate("havingclause", "Reset"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    havingclause = QtWidgets.QMainWindow()
    ui = Ui_havingclause()
    ui.setupUi(havingclause)
    havingclause.show()
    sys.exit(app.exec_())
