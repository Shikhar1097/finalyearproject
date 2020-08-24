# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteuser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_deleteuser(QWidget):
    deleteuser=None
    un=""
    def setupUi(self, deleteuser,dn,uname):
        deleteuser.setObjectName("deleteuser")
        deleteuser.resize(314, 477)
        deleteuser.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 8pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(deleteuser)
        self.centralwidget.setObjectName("centralwidget")
        self.users = QtWidgets.QTableWidget(self.centralwidget)
        self.users.setGeometry(QtCore.QRect(10, 10, 291, 391))
        self.users.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.users.setObjectName("users")
        self.users.setColumnCount(2)
        self.users.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.users.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.users.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.users.setHorizontalHeaderItem(1, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 410, 291, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deletebutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deletebutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.deletebutton.setObjectName("deletebutton")
        self.horizontalLayout.addWidget(self.deletebutton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.cancelbutton.setObjectName("cancelbutton")
        self.horizontalLayout.addWidget(self.cancelbutton)
        deleteuser.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteuser)
        QtCore.QMetaObject.connectSlotsByName(deleteuser)









        
        self.deleteuser=deleteuser
        self.un=uname
        deleteuser.setFixedSize(314,477)
        self.users.verticalHeader().setVisible(False)
        self.cancelbutton.clicked.connect(self.cancelevent)
        self.deletebutton.clicked.connect(self.deleteevent)
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM mainlogin")
        record=crob.fetchall()
        rc=1
        for entry in record:
            un=str(entry[0])
            i=rc-1
            self.users.setRowCount(rc)
            tn=QTableWidgetItem(un)
            self.users.setItem(i, 0, tn)
            if un!="Shikhar" and un!="Ritvik" :
                tn=QTableWidgetItem("User")
                self.users.setItem(i, 1, tn)
            else:
                tn=QTableWidgetItem("Admin")
                self.users.setItem(i, 1, tn)
           
            rc=rc+1
        cn.commit()
        cn.close()



    def cancelevent(self):
        self.deleteuser.close()



    def deleteevent(self):
        if self.un!="Shikhar" and self.un!="Ritvik":
            QMessageBox.about(self, "Alert", "Only the Admin can delete the users.")
        else:
            f=0
            un=self.users.currentItem().text()
            if un=="Shikhar" or un=="Ritvik":
                QMessageBox.about(self, "Alert", "Cannot delete Admin")
            elif un=="Admin" or un=="User":
                QMessageBox.about(self, "Alert", "Select a username")
            else:
                cn=sqlite3.connect('sqlgenerator.db')
                crob=cn.cursor()
                try:
                    crob.execute("DELETE FROM mainlogin WHERE NAME='"+un+"'")
                except:
                    QMessageBox.about(self, "Alert", "No such user.")
                    f=1
                if f==0:
                    QMessageBox.about(self, "Message", "User Deleted.")
                    self.deleteuser.close()
                cn.commit()
                cn.close()
            














    def retranslateUi(self, deleteuser):
        _translate = QtCore.QCoreApplication.translate
        deleteuser.setWindowTitle(_translate("deleteuser", "Delete User"))
        item = self.users.verticalHeaderItem(0)
        item.setText(_translate("deleteuser", "New Row"))
        item = self.users.horizontalHeaderItem(0)
        item.setText(_translate("deleteuser", "UserName"))
        item = self.users.horizontalHeaderItem(1)
        item.setText(_translate("deleteuser", "Property"))
        self.deletebutton.setText(_translate("deleteuser", "Delete"))
        self.cancelbutton.setText(_translate("deleteuser", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteuser = QtWidgets.QMainWindow()
    ui = Ui_deleteuser()
    ui.setupUi(deleteuser)
    deleteuser.show()
    sys.exit(app.exec_())

