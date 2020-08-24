# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
from whereclause import Ui_whereclause
from likeclause import Ui_likeclause
from globclause import Ui_globclause
from limitclause import Ui_limitclause
from sdclause import Ui_sdclause
from orderbyclause import Ui_orderbyclause
from groupbyclause import Ui_groupbyclause
from havingclause import Ui_havingclause

class Ui_selectionwindow(QWidget):
    dbname=""
    selectionwindow=None
    def setupUi(self, selectionwindow,dbname):
        selectionwindow.setObjectName("selectionwindow")
        selectionwindow.resize(530, 109)
        selectionwindow.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(selectionwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("font: 75 12pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selectionlist = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.selectionlist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionlist.sizePolicy().hasHeightForWidth())
        self.selectionlist.setSizePolicy(sizePolicy)
        self.selectionlist.setMaximumSize(QtCore.QSize(162, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectionlist.setFont(font)
        self.selectionlist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectionlist.setObjectName("selectionlist")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.selectionlist.addItem("")
        self.horizontalLayout.addWidget(self.selectionlist)
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.open.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.open.setObjectName("open")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(440, 70, 75, 23))
        self.cancel.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.cancel.setObjectName("cancel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 50, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        selectionwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectionwindow)
        QtCore.QMetaObject.connectSlotsByName(selectionwindow)
        selectionwindow.setFixedSize(530,109)





        self.selectionwindow=selectionwindow
        self.dbname=dbname
        self.cancel.clicked.connect(self.cancelevent)
        self.open.clicked.connect(self.openevent)






    def cancelevent(self):
        self.selectionwindow.close()



    def openevent(self):
        ind=self.selectionlist.currentIndex()
        if ind==0:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_whereclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==1:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_likeclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==2:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_globclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==3:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_limitclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==4:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_sdclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==5:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_orderbyclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==6:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_groupbyclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()
        if ind==7:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_havingclause()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()
            self.selectionwindow.close()




        

    def retranslateUi(self, selectionwindow):
        _translate = QtCore.QCoreApplication.translate
        selectionwindow.setWindowTitle(_translate("selectionwindow", "Specific Selection Types"))
        self.label_2.setText(_translate("selectionwindow", "Seletion Method:"))
        self.selectionlist.setItemText(0, _translate("selectionwindow", "WHERE "))
        self.selectionlist.setItemText(1, _translate("selectionwindow", "LIKE"))
        self.selectionlist.setItemText(2, _translate("selectionwindow", "GLOB"))
        self.selectionlist.setItemText(3, _translate("selectionwindow", "LIMIT"))
        self.selectionlist.setItemText(4, _translate("selectionwindow", "DISTINCT"))
        self.selectionlist.setItemText(5, _translate("selectionwindow", "ORDER BY"))
        self.selectionlist.setItemText(6, _translate("selectionwindow", "GROUP BY"))
        self.selectionlist.setItemText(7, _translate("selectionwindow", "HAVING"))
        self.open.setText(_translate("selectionwindow", "Open"))
        self.cancel.setText(_translate("selectionwindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectionwindow = QtWidgets.QMainWindow()
    ui = Ui_selectionwindow()
    ui.setupUi(selectionwindow)
    selectionwindow.show()
    sys.exit(app.exec_())

