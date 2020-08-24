# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'limitclause.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from display import Ui_display
import sqlite3

class Ui_limitclause(QWidget):
    dbname=""
    limitclause=None
    def setupUi(self, limitclause,dbname):
        limitclause.setObjectName("limitclause")
        limitclause.resize(454, 222)
        limitclause.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(limitclause)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fromentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fromentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.fromentry.setObjectName("fromentry")
        self.gridLayout.addWidget(self.fromentry, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.selectentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.selectentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.selectentry.setObjectName("selectentry")
        self.gridLayout.addWidget(self.selectentry, 0, 2, 1, 1)
        self.limitentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.limitentry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.limitentry.setObjectName("limitentry")
        self.gridLayout.addWidget(self.limitentry, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.execute = QtWidgets.QPushButton(self.centralwidget)
        self.execute.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.execute.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.execute.setObjectName("execute")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(370, 190, 75, 23))
        self.reset.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.reset.setObjectName("reset")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 160, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        limitclause.setCentralWidget(self.centralwidget)

        self.retranslateUi(limitclause)
        QtCore.QMetaObject.connectSlotsByName(limitclause)
        limitclause.setFixedSize(454,222)



        self.limitclause=limitclause
        self.dbname=dbname
        self.selectentry.setFocus()


        self.reset.clicked.connect(self.resetevent)
        self.execute.clicked.connect(self.executeevent)


    def resetevent(self):
        self.selectentry.setText("")
        self.fromentry.setText("")
        self.limitentry.setText("")
        self.selectentry.setFocus()


    def executeevent(self):
        se=self.selectentry.text()
        fe=self.fromentry.text()
        le=self.limitentry.text()
        if le=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif se=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif fe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        else:
            query="SELECT "+se+" FROM "+fe+" LIMIT "+le+";"
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
            self.limitclause.close()






        

    def retranslateUi(self, limitclause):
        _translate = QtCore.QCoreApplication.translate
        limitclause.setWindowTitle(_translate("limitclause", "LIMIT"))
        self.label_2.setText(_translate("limitclause", "FROM"))
        self.label.setText(_translate("limitclause", "SELECT"))
        self.label_4.setText(_translate("limitclause", "LIMIT"))
        self.execute.setText(_translate("limitclause", "Execute"))
        self.reset.setText(_translate("limitclause", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    limitclause = QtWidgets.QMainWindow()
    ui = Ui_limitclause()
    ui.setupUi(limitclause)
    limitclause.show()
    sys.exit(app.exec_())

