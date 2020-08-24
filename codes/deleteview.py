# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteview.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_deleteview(QWidget):
    dbname=''
    deleteview=None
    def setupUi(self, deleteview,dn):
        deleteview.setObjectName("deleteview")
        deleteview.resize(304, 440)
        deleteview.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(deleteview)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(30, 10, 241, 351))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 380, 241, 51))
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
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        deleteview.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteview)
        QtCore.QMetaObject.connectSlotsByName(deleteview)







        self.dbname=dn
        self.deleteview=deleteview
        deleteview.setFixedSize(304,440)
        self.cancel.clicked.connect(self.cancelevent)
        self.deletebutton.clicked.connect(self.deleteevent)
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM VName")
        record=crob.fetchall()
        rc=1
        for entry in record:
            dbn=str(entry[1])
            if self.dbname==dbn:
                i=rc-1
                self.tables.setRowCount(rc)
                tn=QTableWidgetItem(str(entry[0]))
                self.tables.setItem(i, 0, tn)
                rc=rc+1
        cn.commit()
        cn.close()
        






    def cancelevent(self):
        self.deleteview.close()




    def deleteevent(self):
        vn=self.tables.currentItem().text()
        query="DROP VIEW "+vn+";"
        QMessageBox.about(self, "Query", query)
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute(query)
        cn.commit()
        cn.close()
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("DELETE FROM VName WHERE vname=? AND dbname=?;",(vn,self.dbname))
        cn.commit()
        cn.close()
        QMessageBox.about(self, "Message", "View Deleted")
        self.deleteview.close()

        










    def retranslateUi(self, deleteview):
        _translate = QtCore.QCoreApplication.translate
        deleteview.setWindowTitle(_translate("deleteview", "Delete View"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("deleteview", "Views"))
        self.deletebutton.setText(_translate("deleteview", "Delete"))
        self.cancel.setText(_translate("deleteview", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteview = QtWidgets.QMainWindow()
    ui = Ui_deleteview()
    ui.setupUi(deleteview)
    deleteview.show()
    sys.exit(app.exec_())

