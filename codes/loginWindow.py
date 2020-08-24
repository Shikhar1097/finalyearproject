# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
from selectdatabasewindow import Ui_selectdatabasewindow

class Ui_loginwindow(QWidget):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(499, 224)
        loginwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 481, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.usernameentry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.usernameentry.setFont(font)
        self.usernameentry.setObjectName("usernameentry")
        self.horizontalLayout.addWidget(self.usernameentry)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 80, 481, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.passwordentry = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.passwordentry.setFont(font)
        self.passwordentry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordentry.setObjectName("passwordentry")
        self.horizontalLayout_2.addWidget(self.passwordentry)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 481, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(12)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.loginbutton.setObjectName("loginbutton")
        self.horizontalLayout_3.addWidget(self.loginbutton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.resetbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(12)
        self.resetbutton.setFont(font)
        self.resetbutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.resetbutton.setObjectName("resetbutton")
        self.horizontalLayout_3.addWidget(self.resetbutton)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        loginwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

        self.loginbutton.setAutoDefault(True)
        self.passwordentry.returnPressed.connect(self.loginbutton.click)
        self.usernameentry.returnPressed.connect(self.loginbutton.click)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Log In"))
        self.username.setText(_translate("loginwindow", "Username:"))
        self.password.setText(_translate("loginwindow", "Password :"))
        self.loginbutton.setText(_translate("loginwindow", "Login"))
        self.resetbutton.setText(_translate("loginwindow", "Reset"))



        self.resetbutton.clicked.connect(self.resetWindow)
        self.loginbutton.clicked.connect(self.logWindow)
        

    def resetWindow(self):
        self.usernameentry.setText("")
        self.passwordentry.setText("")
        self.usernameentry.setFocus()

    def logWindow(self):
        flag=0
        name=self.usernameentry.text()
        pw=self.passwordentry.text()
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        if name=='' or pw=='':
            QMessageBox.about(self, "Alert", "Enter a valid user name and password.")
        else:
            crob.execute("SELECT * FROM mainlogin")
            record=crob.fetchall()
            for entry in record:
                n=str(entry[0])
                p=str(entry[1])
                if n==name:
                    flag=1
                    if pw!=p:
                        QMessageBox.about(self, "Alert", "Enter a valid password.")
                    else:
                        loginwindow.close()
                        self.window = QtWidgets.QMainWindow()
                        self.ui = Ui_selectdatabasewindow()
                        self.ui.setupUi(self.window,name)
                        self.window.show()
                        
                    
        if flag==0:
            QMessageBox.about(self, "Alert", "Enter a valid username.")
        cn.commit()
        cn.close()
        self.usernameentry.setText("")
        self.passwordentry.setText("")
        self.usernameentry.setFocus()





        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    loginwindow.setFixedSize(loginwindow.size())
    sys.exit(app.exec_())

