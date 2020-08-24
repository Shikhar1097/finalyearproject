# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletetable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_deletetable(QWidget):
    dbname=''
    deletetable=None
    def setupUi(self, deletetable,dn):
        deletetable.setObjectName("deletetable")
        deletetable.resize(320, 451)
        deletetable.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(deletetable)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(15, 10, 281, 381))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 400, 271, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deletebutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deletebutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.deletebutton.setObjectName("deletebutton")
        self.horizontalLayout.addWidget(self.deletebutton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancelbutton.setFont(font)
        self.cancelbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancelbutton.setObjectName("cancelbutton")
        self.horizontalLayout.addWidget(self.cancelbutton)
        deletetable.setCentralWidget(self.centralwidget)

        self.retranslateUi(deletetable)
        QtCore.QMetaObject.connectSlotsByName(deletetable)










        self.dbname=dn
        self.deletetable=deletetable
        deletetable.setFixedSize(320,451)
        self.tables.verticalHeader().setVisible(False)
        self.cancelbutton.clicked.connect(self.cancelevent)
        self.deletebutton.clicked.connect(self.deleteevent)
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM TName")
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
        self.deletetable.close()


    def deleteevent(self):
        tn=self.tables.currentItem().text()
        query="DROP TABLE "+tn+";"
        QMessageBox.about(self, "Query", query)
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute(query)
        cn.commit()
        cn.close()
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("DELETE FROM TName WHERE tname=? AND dbname=?;",(tn,self.dbname))
        cn.commit()
        cn.close()
        QMessageBox.about(self, "Message", "Table Deleted")
        self.deletetable.close()

















    def retranslateUi(self, deletetable):
        _translate = QtCore.QCoreApplication.translate
        deletetable.setWindowTitle(_translate("deletetable", "Delete Table"))
        item = self.tables.verticalHeaderItem(0)
        item.setText(_translate("deletetable", "New Row"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("deletetable", "Tables"))
        self.deletebutton.setText(_translate("deletetable", "Delete"))
        self.cancelbutton.setText(_translate("deletetable", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deletetable = QtWidgets.QMainWindow()
    ui = Ui_deletetable()
    ui.setupUi(deletetable)
    deletetable.show()
    sys.exit(app.exec_())

