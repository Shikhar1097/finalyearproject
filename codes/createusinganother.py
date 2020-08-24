# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createusinganother.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_createusinganother(QWidget):
    dbname=''
    createusinganother=None
    def setupUi(self, createusinganother,dn):
        createusinganother.setObjectName("createusinganother")
        createusinganother.resize(288, 431)
        createusinganother.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.centralwidget = QtWidgets.QWidget(createusinganother)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 271, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.selecttable = QtWidgets.QLabel(self.centralwidget)
        self.selecttable.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selecttable.setFont(font)
        self.selecttable.setStyleSheet("color: rgb(255, 255, 255);")
        self.selecttable.setObjectName("selecttable")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 271, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectbutton.setFont(font)
        self.selectbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectbutton.setObjectName("selectbutton")
        self.horizontalLayout.addWidget(self.selectbutton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelbutton.setFont(font)
        self.cancelbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancelbutton.setObjectName("cancelbutton")
        self.horizontalLayout.addWidget(self.cancelbutton)
        createusinganother.setCentralWidget(self.centralwidget)

        self.retranslateUi(createusinganother)
        QtCore.QMetaObject.connectSlotsByName(createusinganother)





        
        createusinganother.setFixedSize(288,431)
        self.createusinganother=createusinganother
        self.cancelbutton.clicked.connect(self.cancelevent)
        self.selectbutton.clicked.connect(self.selectevent)
        self.dbname=dn
        self.tableWidget.verticalHeader().setVisible(False)
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        crob.execute("SELECT * FROM TName")
        record=crob.fetchall()
        rc=1
        for entry in record:
            dbn=str(entry[1])
            if self.dbname==dbn:
                i=rc-1
                self.tableWidget.setRowCount(rc)
                tn=QTableWidgetItem(str(entry[0]))
                self.tableWidget.setItem(i, 0, tn)
                rc=rc+1
        cn.commit()
        cn.close()

        


    def cancelevent(self):
        self.createusinganother.close()


    def selectevent(self):
        cn=sqlite3.connect('sqlgenerator.db')
        crob=cn.cursor()
        cn1=sqlite3.connect(self.dbname+'.db')
        crob1=cn1.cursor()
        text,ok = QInputDialog.getText(self, 'Create Table', 'Enter Table Name:')
        txt=str(text)
        if ok:
            if txt=='':
                QMessageBox.about(self, "Alert", "Enter a valid table name.")
            else:
                flag=0
                crob.execute("SELECT * FROM TName;")
                record=crob.fetchall()
                for TableName in record:
                    tbn=str(TableName[0])
                    dbn=str(TableName[1])
                    if tbn==txt and dbn==self.dbname:
                        flag=1
                if flag==0:
                    tn=self.tableWidget.currentItem().text()
                    crob.execute("SELECT * FROM TName;")
                    record=crob.fetchall()
                    for TableName in record:
                        tbn=str(TableName[0])
                        dbn=str(TableName[1])
                        q=str(TableName[2])
                        if tbn==tn and dbn==self.dbname:
                            ind=q.index('(')
                            query='CREATE TABLE '+txt+q[ind:]
                                    
                            QMessageBox.about(self, "Query", query)
                            crob1.execute(query)
                            crob.execute("INSERT INTO TName(tname,dbname,query)VALUES(?,?,?);",(txt,dbn,query))
                            QMessageBox.about(self, "Alert", "Table Created")
                            self.createusinganother.close()
                else:
                    QMessageBox.about(self, "Alert", "Table already exists.")
        cn.commit()
        cn1.commit()
        cn.close()
        cn1.close()
        








        

    def retranslateUi(self, createusinganother):
        _translate = QtCore.QCoreApplication.translate
        createusinganother.setWindowTitle(_translate("createusinganother", "Create Using Another Table"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("createusinganother", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("createusinganother", "Tables Available"))
        self.selecttable.setText(_translate("createusinganother", "Select Table:"))
        self.selectbutton.setText(_translate("createusinganother", "select"))
        self.cancelbutton.setText(_translate("createusinganother", "cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createusinganother = QtWidgets.QMainWindow()
    ui = Ui_createusinganother()
    ui.setupUi(createusinganother)
    createusinganother.show()
    
    sys.exit(app.exec_())

