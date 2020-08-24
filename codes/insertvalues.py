# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertvalues.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_insertvalues(QWidget):
    dbname=''
    insertvalues=None
    rowcount=0
    colcount=0
    query='INSERT INTO '
    def setupUi(self, insertvalues,dn):
        insertvalues.setObjectName("insertvalues")
        insertvalues.resize(779, 542)
        insertvalues.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(insertvalues)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 221, 391))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 409, 131, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.verticalLayout.addWidget(self.select)
        self.done = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.done.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.done.setObjectName("done")
        self.verticalLayout.addWidget(self.done)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 10, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.values = QtWidgets.QTableWidget(self.centralwidget)
        self.values.setGeometry(QtCore.QRect(270, 10, 491, 391))
        self.values.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.values.setObjectName("values")
        self.values.setColumnCount(0)
        self.values.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(269, 410, 491, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addrow = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addrow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.addrow.setObjectName("addrow")
        self.horizontalLayout.addWidget(self.addrow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.removerow = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removerow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.removerow.setObjectName("removerow")
        self.horizontalLayout.addWidget(self.removerow)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 480, 491, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        insertvalues.setCentralWidget(self.centralwidget)

        self.retranslateUi(insertvalues)
        QtCore.QMetaObject.connectSlotsByName(insertvalues)







        self.dbname=dn
        self.insertvalues=insertvalues
        insertvalues.setFixedSize(779,542)
        self.done.clicked.connect(self.doneevent)
        self.select.clicked.connect(self.selectevent)
        self.addrow.clicked.connect(self.addrowevent)
        self.removerow.clicked.connect(self.removerowevent)
        self.pushButton.clicked.connect(self.insertevent)
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



    def doneevent(self):
        self.insertvalues.close()



    def selectevent(self):
        q='('
        i=1
        tn=self.tables.currentItem().text()
        self.query+=tn
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute('PRAGMA TABLE_INFO('+tn+')')
        titles = [tup[1] for tup in crob.fetchall()]
        for ch in titles:
            self.values.setColumnCount(i)
            item = QtWidgets.QTableWidgetItem()
            item.setText(ch)
            q=q+ch+','
            self.values.setHorizontalHeaderItem((i-1), item)
            i+=1
        self.colcount=i-1
        cn.commit()
        cn.close()
        self.query+=q[:len(q)-1]+')VALUES('



    def addrowevent(self):
        self.rowcount=self.rowcount+1
        self.values.setRowCount(self.rowcount)



    def removerowevent(self):
        if self.rowcount==0:
            QMessageBox.about(self, "Alert", "No rows present in the table.")
        else:
            self.rowcount=self.rowcount-1
            self.values.setRowCount(self.rowcount)



    def insertevent(self):
        q=''
        f=0
        flag=0
        query1=''
        for i in range(0,self.colcount):
            if self.values.item(0,i)==None:
                f=1
        if f==1:
            QMessageBox.about(self, "Alert", "Provide all required values.") 
        else:
            for i in range(0,self.colcount):
                fl=0
                entry=self.values.item(0,i).text()
                if entry.isdigit():
                    q+=entry+','  
                elif entry.isalpha():
                    q+='"'+entry+'",'
                else:
                    q+=entry+','
            self.query+=q[:len(q)-1]+');'
            cn=sqlite3.connect(self.dbname+'.db')
            crob=cn.cursor()
            try:
                crob.execute(self.query)
            except e:
                QMessageBox.about(self, "Alert", "Some error occured.")
                flag=1
            if flag==0:
                QMessageBox.about(self, "Query", self.query)
                QMessageBox.about(self, "Message", "Values Inserted.")
                self.values.setRowCount(0)
                self.query=''
            cn.commit()
            cn.close()
            self.rowcount=0
            self.colcount=0
            













    def retranslateUi(self, insertvalues):
        _translate = QtCore.QCoreApplication.translate
        insertvalues.setWindowTitle(_translate("insertvalues", "Insert Values"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("insertvalues", "Tables"))
        self.select.setText(_translate("insertvalues", "Select"))
        self.done.setText(_translate("insertvalues", "Done"))
        self.addrow.setText(_translate("insertvalues", "Add Row"))
        self.removerow.setText(_translate("insertvalues", "Remove Row"))
        self.pushButton.setText(_translate("insertvalues", "Insert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    insertvalues = QtWidgets.QMainWindow()
    ui = Ui_insertvalues()
    ui.setupUi(insertvalues)
    insertvalues.show()
    sys.exit(app.exec_())

