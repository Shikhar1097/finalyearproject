# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dswindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_dswindow(QWidget):
    dbname=''
    dswindow=None
    def setupUi(self, dswindow,dn):
        dswindow.setObjectName("dswindow")
        dswindow.resize(554, 247)
        dswindow.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(dswindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 81))
        self.groupBox.setObjectName("groupBox")
        self.tables = QtWidgets.QComboBox(self.groupBox)
        self.tables.setGeometry(QtCore.QRect(130, 40, 361, 22))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 601, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dstruct = QtWidgets.QTextEdit(self.groupBox_2)
        self.dstruct.setGeometry(QtCore.QRect(20, 30, 481, 41))
        self.dstruct.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.dstruct.setObjectName("dstruct")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(440, 110, 75, 23))
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.cancel.setObjectName("cancel")
        dswindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(dswindow)
        QtCore.QMetaObject.connectSlotsByName(dswindow)







        self.dstruct.setReadOnly(True)
        self.dbname=dn
        self.dswindow=dswindow
        dswindow.setFixedSize(554,247)
        self.cancel.clicked.connect(self.cancelevent)
        self.select.clicked.connect(self.selectevent)
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM TName;")
        while True:
            record=crob.fetchone()
            if record!=None:
                dbn=str(record[1])
                tn=str(record[0])
                if dbn==self.dbname:
                    self.tables.addItem(tn)
            else:
                break
        cn.commit()
        cn.close()







    def cancelevent(self):
        self.dswindow.close()





    def selectevent(self):
        tname=str(self.tables.currentText())
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM TName;")
        while True:
            record=crob.fetchone()
            if record!=None:
                dbn=str(record[1])
                tn=str(record[0])
                if dbn==self.dbname and tn==tname:
                    s=str(record[2])
                    self.dstruct.setText(s)
            else:
                break
        cn.commit()
        cn.close()
        
        















    def retranslateUi(self, dswindow):
        _translate = QtCore.QCoreApplication.translate
        dswindow.setWindowTitle(_translate("dswindow", "Data Structure"))
        self.groupBox.setTitle(_translate("dswindow", "Table"))
        self.label.setText(_translate("dswindow", "Select Table:"))
        self.groupBox_2.setTitle(_translate("dswindow", "Data Structure"))
        self.select.setText(_translate("dswindow", "Select"))
        self.cancel.setText(_translate("dswindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dswindow = QtWidgets.QMainWindow()
    ui = Ui_dswindow()
    ui.setupUi(dswindow)
    dswindow.show()
    sys.exit(app.exec_())

