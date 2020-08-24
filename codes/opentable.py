# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opentable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_opentable(QWidget):
    dbname=''
    opentable=None
    def setupUi(self, opentable,dn):
        opentable.setObjectName("opentable")
        opentable.resize(774, 434)
        font = QtGui.QFont()
        font.setPointSize(11)
        opentable.setFont(font)
        opentable.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(opentable)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 201, 371))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.openbutton = QtWidgets.QPushButton(self.centralwidget)
        self.openbutton.setGeometry(QtCore.QRect(70, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.openbutton.setFont(font)
        self.openbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.openbutton.setObjectName("openbutton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 10, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.openedtable = QtWidgets.QTableWidget(self.centralwidget)
        self.openedtable.setGeometry(QtCore.QRect(250, 10, 511, 371))
        self.openedtable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.openedtable.setObjectName("openedtable")
        self.openedtable.setColumnCount(1)
        self.openedtable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.openedtable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.openedtable.setHorizontalHeaderItem(0, item)
        self.okbutton = QtWidgets.QPushButton(self.centralwidget)
        self.okbutton.setGeometry(QtCore.QRect(470, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.okbutton.setFont(font)
        self.okbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.okbutton.setObjectName("okbutton")
        opentable.setCentralWidget(self.centralwidget)

        self.retranslateUi(opentable)
        QtCore.QMetaObject.connectSlotsByName(opentable)







        self.tables.verticalHeader().setVisible(False)
        self.openedtable.verticalHeader().setVisible(False)
        self.dbname=dn
        self.opentable=opentable
        opentable.setFixedSize(774,434)
        self.okbutton.clicked.connect(self.okevent)
        self.openbutton.clicked.connect(self.openevent)
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






    def okevent(self):
        self.opentable.close()


    def openevent(self):
        i=1
        tn=self.tables.currentItem().text()
        QMessageBox.about(self, "Query", "SELECT * FROM "+tn)
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute('PRAGMA TABLE_INFO('+tn+')')
        titles = [tup[1] for tup in crob.fetchall()]
        for ch in titles:
            self.openedtable.setColumnCount(i)
            item = QtWidgets.QTableWidgetItem()
            item.setText(ch)
            self.openedtable.setHorizontalHeaderItem((i-1), item)
            i+=1
        crob.execute("SELECT * FROM "+tn)
        record=crob.fetchall()
        rc=1
        for entry in record:
            self.openedtable.setRowCount(rc)
            cc=0
            for i in entry:
                item=QTableWidgetItem(str(i))
                self.openedtable.setItem((rc-1), cc, item)
                cc+=1
            rc+=1
        cn.commit()
        cn.close()
        








    def retranslateUi(self, opentable):
        _translate = QtCore.QCoreApplication.translate
        opentable.setWindowTitle(_translate("opentable", "Open Table"))
        item = self.tables.verticalHeaderItem(0)
        item.setText(_translate("opentable", "New Row"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("opentable", "Tables Available"))
        self.openbutton.setText(_translate("opentable", "Open"))
        item = self.openedtable.verticalHeaderItem(0)
        item.setText(_translate("opentable", "New Row"))
        item = self.openedtable.horizontalHeaderItem(0)
        item.setText(_translate("opentable", "New Column"))
        self.okbutton.setText(_translate("opentable", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    opentable = QtWidgets.QMainWindow()
    ui = Ui_opentable()
    ui.setupUi(opentable)
    opentable.show()
    sys.exit(app.exec_())

