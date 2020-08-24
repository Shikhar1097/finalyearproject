# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectdatabasewindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeyEvent
import sqlite3
from mainwindow import Ui_mainwindow


class Ui_selectdatabasewindow(QWidget):
    selectdatabasewindow=None
    uname=""
    def setupUi(self, selectdatabasewindow,uname):
        selectdatabasewindow.setObjectName("selectdatabasewindow")
        selectdatabasewindow.resize(460, 151)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        selectdatabasewindow.setFont(font)
        selectdatabasewindow.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(selectdatabasewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectdb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.selectdb.setFont(font)
        self.selectdb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.selectdb.setStyleSheet("font: 75 12pt \"Comic Sans MS\";")
        self.selectdb.setTextFormat(QtCore.Qt.RichText)
        self.selectdb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.selectdb.setObjectName("selectdb")
        self.horizontalLayout.addWidget(self.selectdb)
        self.dblist = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.dblist.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: italic 12pt \"Comic Sans MS\";")
        self.dblist.setObjectName("dblist")
        self.horizontalLayout.addWidget(self.dblist)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 80, 451, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 110, 91, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        selectdatabasewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectdatabasewindow)
        QtCore.QMetaObject.connectSlotsByName(selectdatabasewindow)
        selectdatabasewindow.setFixedSize(460,151)







        self.selectdatabasewindow=selectdatabasewindow
        self.pushButton.clicked.connect(self.openWindow)
        self.uname=uname
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM DTBS")
        record=crob.fetchall()
        for entry in record:
            un=str(entry[0])
            if self.uname==un:
                self.dblist.addItem(str(entry[1]))
        self.dblist.addItem("Create New Database")
        cn.commit()
        cn.close()

        





        

    def retranslateUi(self, selectdatabasewindow):
        _translate = QtCore.QCoreApplication.translate
        selectdatabasewindow.setWindowTitle(_translate("selectdatabasewindow", "Select Database"))
        self.selectdb.setText(_translate("selectdatabasewindow", "Select Database"))
        self.pushButton.setText(_translate("selectdatabasewindow", "Open"))







        
        

    def openWindow(self):
        entry=self.dblist.currentText()
        if entry!="Create New Database":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_mainwindow()
            self.ui.setupUi(self.window,entry,self.uname)
            self.window.showMaximized()
            self.selectdatabasewindow.close()
        else:
            text,ok = QInputDialog.getText(self, 'Create Database', 'Enter Database Name:')
            txt=str(text)
            if ok:
                if txt=='':
                    QMessageBox.about(self, "Alert", "Enter a valid database name.")
                else:
                    flag=0
                    cn=sqlite3.connect('sqlgenerator.db')
                    crob=cn.cursor()
                    crob.execute("SELECT * FROM DTBS")
                    record=crob.fetchall()
                    for entry in record:
                        un=str(entry[0])
                        if self.uname==un:
                            dbn=str(entry[1])
                            if txt==dbn:
                                flag=1
                    cn.commit()
                    cn.close()
                    if flag==1:
                        QMessageBox.about(self, "Alert", "Database already exists.")
                    else:
                        self.window = QtWidgets.QMainWindow()
                        self.ui = Ui_mainwindow()
                        self.ui.setupUi(self.window,txt,self.uname)
                        self.window.showMaximized()
                        self.selectdatabasewindow.close()
                        cn=sqlite3.connect('sqlgenerator.db')
                        crob=cn.cursor()
                        crob.execute("INSERT INTO DTBS(UN,DBN)VALUES(?,?);",(self.uname,txt))
                        cn.commit()
                        cn.close()
        
        










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectdatabasewindow = QtWidgets.QMainWindow()
    ui = Ui_selectdatabasewindow()
    ui.setupUi(selectdatabasewindow)
    selectdatabasewindow.show()
    sys.exit(app.exec_())

