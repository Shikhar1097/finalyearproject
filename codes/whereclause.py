# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whereclause.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from display import Ui_display
import sqlite3

class Ui_whereclause(QWidget):
    dbname=""
    whereclause=None
    def setupUi(self, whereclause,dbname):
        whereclause.setObjectName("whereclause")
        whereclause.resize(403, 283)
        whereclause.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(whereclause)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 381, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fromlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fromlabel.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.fromlabel.setObjectName("fromlabel")
        self.gridLayout.addWidget(self.fromlabel, 1, 0, 1, 1)
        self.whereentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.whereentry.setStyleSheet("font: 75 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.whereentry.setObjectName("whereentry")
        self.gridLayout.addWidget(self.whereentry, 2, 2, 1, 1)
        self.selectlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.selectlabel.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.selectlabel.setObjectName("selectlabel")
        self.gridLayout.addWidget(self.selectlabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.wherelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wherelabel.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.wherelabel.setObjectName("wherelabel")
        self.gridLayout.addWidget(self.wherelabel, 2, 0, 1, 1)
        self.fromentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fromentry.setStyleSheet("font: 75 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.fromentry.setObjectName("fromentry")
        self.gridLayout.addWidget(self.fromentry, 1, 2, 1, 1)
        self.selectentry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.selectentry.setStyleSheet("font: 75 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.selectentry.setObjectName("selectentry")
        self.gridLayout.addWidget(self.selectentry, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.execute = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.execute.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.execute.setObjectName("execute")
        self.horizontalLayout.addWidget(self.execute)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(17, 200, 371, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        whereclause.setCentralWidget(self.centralwidget)

        self.retranslateUi(whereclause)
        QtCore.QMetaObject.connectSlotsByName(whereclause)
        whereclause.setFixedSize(403,283)



        self.whereclause=whereclause
        self.dbname=dbname
        self.selectentry.setFocus()



        self.reset.clicked.connect(self.resetevent)
        self.execute.clicked.connect(self.executeevent)




    def resetevent(self):
        self.selectentry.setText("")
        self.fromentry.setText("")
        self.whereentry.setText("")
        self.selectentry.setFocus()



    def executeevent(self):
        se=self.selectentry.text()
        fe=self.fromentry.text()
        we=self.whereentry.text()
        if we=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif se=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        elif fe=="":
            QMessageBox.about(self, "Alert", "Fill all required entries.")
        else:
            query="SELECT "+se+" FROM "+fe+" WHERE "+we+";"
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
            self.whereclause.close()




        


    def retranslateUi(self, whereclause):
        _translate = QtCore.QCoreApplication.translate
        whereclause.setWindowTitle(_translate("whereclause", "WHERE"))
        self.fromlabel.setText(_translate("whereclause", "FROM"))
        self.selectlabel.setText(_translate("whereclause", "SELECT"))
        self.wherelabel.setText(_translate("whereclause", "WHERE"))
        self.execute.setText(_translate("whereclause", "Execute"))
        self.reset.setText(_translate("whereclause", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    whereclause = QtWidgets.QMainWindow()
    ui = Ui_whereclause()
    ui.setupUi(whereclause)
    whereclause.show()
    sys.exit(app.exec_())

