# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createuser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_createuser(QWidget):
    createuser=None
    def setupUi(self, createuser,dn):
        createuser.setObjectName("createuser")
        createuser.resize(475, 247)
        createuser.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(createuser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.conpass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.conpass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.conpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpass.setObjectName("conpass")
        self.gridLayout.addWidget(self.conpass, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 451, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.create.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.create.setObjectName("create")
        self.horizontalLayout.addWidget(self.create)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 255, 255);")
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        createuser.setCentralWidget(self.centralwidget)

        self.retranslateUi(createuser)
        QtCore.QMetaObject.connectSlotsByName(createuser)








        self.createuser=createuser
        self.reset.clicked.connect(self.resetWindow)
        self.create.clicked.connect(self.createWindow)
        createuser.setFixedSize(475,247)



    def resetWindow(self):
        self.username.setText("")
        self.password.setText("")
        self.conpass.setText("")
        self.username.setFocus()



    def createWindow(self):
        f=0
        fl=0
        un=self.username.text()
        pw=self.password.text()
        cp=self.conpass.text()
        if un=='' or pw=='':
            QMessageBox.about(self, "Alert", "Enter valid username and password.")
        else:
            cn=sqlite3.connect('sqlgenerator.db')
            crob=cn.cursor()
            crob.execute("SELECT * FROM mainlogin")
            record=crob.fetchall()
            for entry in record:
                uname=str(entry[0])
                if uname==un:
                    f=1
                    fl=1
                    self.username.setText("")
                    self.password.setText("")
                    self.conpass.setText("")
                    self.username.setFocus()
            if pw!=cp:
                QMessageBox.about(self, "Alert", "Passwords don't match.")
                self.password.setText("")
                self.conpass.setText("")
                self.password.setFocus()
                f=1
            if fl==1:
                QMessageBox.about(self, "Alert", "User Already Exists.")
            if f==0:
                crob.execute("INSERT INTO mainlogin(NAME, PASSWORD)VALUES(?,?);",(un,pw))
                QMessageBox.about(self, "Message", "User Created.")
                self.createuser.close()
            cn.commit()
            cn.close()
        self.username.setText("")
        self.password.setText("")
        self.conpass.setText("")
        self.username.setFocus()
        
            










    def retranslateUi(self, createuser):
        _translate = QtCore.QCoreApplication.translate
        createuser.setWindowTitle(_translate("createuser", "Create User"))
        self.label_2.setText(_translate("createuser", "Create Password:"))
        self.label.setText(_translate("createuser", "Create Username:"))
        self.label_3.setText(_translate("createuser", "Confirm Password:"))
        self.create.setText(_translate("createuser", "Create"))
        self.reset.setText(_translate("createuser", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createuser = QtWidgets.QMainWindow()
    ui = Ui_createuser()
    ui.setupUi(createuser)
    createuser.show()
    sys.exit(app.exec_())

