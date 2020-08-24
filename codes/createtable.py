# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createtable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_createtable(QWidget):
    rowcount=1
    dbname=''
    createtable=None
    def setupUi(self, createtable,dn):
        createtable.setObjectName("createtable")
        createtable.resize(562, 413)
        createtable.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(createtable)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 541, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tablename = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tablename.setFont(font)
        self.tablename.setObjectName("tablename")
        self.horizontalLayout.addWidget(self.tablename)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tablenameentry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.tablenameentry.setFont(font)
        self.tablenameentry.setObjectName("tablenameentry")
        self.horizontalLayout.addWidget(self.tablenameentry)
        self.createbutton = QtWidgets.QPushButton(self.centralwidget)
        self.createbutton.setGeometry(QtCore.QRect(460, 380, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.createbutton.setFont(font)
        self.createbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.createbutton.setObjectName("createbutton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabledetails = QtWidgets.QGroupBox(self.centralwidget)
        self.tabledetails.setGeometry(QtCore.QRect(9, 70, 541, 301))
        self.tabledetails.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabledetails.setObjectName("tabledetails")
        self.tablewidget = QtWidgets.QTableWidget(self.tabledetails)
        self.tablewidget.setGeometry(QtCore.QRect(5, 21, 531, 281))
        self.tablewidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.tablewidget.setObjectName("tablewidget")
        self.tablewidget.setColumnCount(4)
        self.tablewidget.setRowCount(self.rowcount)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(3, item)
        self.removerowbutton = QtWidgets.QPushButton(self.centralwidget)
        self.removerowbutton.setGeometry(QtCore.QRect(220, 380, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.removerowbutton.setFont(font)
        self.removerowbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.removerowbutton.setObjectName("removerowbutton")
        self.addrowbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addrowbutton.setGeometry(QtCore.QRect(10, 380, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.addrowbutton.setFont(font)
        self.addrowbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addrowbutton.setObjectName("addrowbutton")
        createtable.setCentralWidget(self.centralwidget)

        self.retranslateUi(createtable)
        QtCore.QMetaObject.connectSlotsByName(createtable)







        createtable.setFixedSize(562,413)
        self.createtable=createtable
        self.tablewidget.verticalHeader().setVisible(False)
        self.addrowbutton.clicked.connect(self.addrow)
        self.removerowbutton.clicked.connect(self.removerow)
        self.createbutton.clicked.connect(self.createnewtable)
        self.dbname=dn
        
        
        
        

    def addrow(self):
        self.rowcount=self.rowcount+1
        self.tablewidget.setRowCount(self.rowcount)

    def removerow(self):
        if self.rowcount==0:
            QMessageBox.about(self, "Alert", "No rows present in the table.")
        else:
            self.rowcount=self.rowcount-1
            self.tablewidget.setRowCount(self.rowcount)

    def createnewtable(self):
        dbn=self.dbname
        print(dbn)
        st=""
        flag=0
        f=0
        check=0
        tn=self.tablenameentry.text()
        if tn!="":
            cn=sqlite3.connect('sqlgenerator.db')
            crob=cn.cursor()
            crob.execute("SELECT * FROM TName")
            record=crob.fetchall()
            for entry in record:
                t=str(entry[0])
                db=str(entry[1])
                if tn==t and db==dbn:
                    check=1
                    flag=1
                    QMessageBox.about(self, "Alert", "Table Already Exists.")
            cn.commit()
            cn.close()
            if check==0:
                st=st+"CREATE TABLE "+tn+"("
        else:
            QMessageBox.about(self, "Alert", "No table name given.")
            flag=1
            f=1
        limit=self.rowcount
        for i in range(0,limit):
            if self.tablewidget.item(i,0)!=None and self.tablewidget.item(i,1)!=None and self.tablewidget.item(i,2)!=None:
                st=st+self.tablewidget.item(i,0).text()+" "+self.tablewidget.item(i,1).text()+"("+self.tablewidget.item(i,2).text()+")"
                if self.tablewidget.item(i,3)!=None:
                    st=st+" "+self.tablewidget.item(i,3).text()
                if i!=(limit-1):
                    st=st+","
                else:
                    st=st+")"
            else:
                flag=1
                if f==0 and check==0:
                    QMessageBox.about(self, "Alert", "Fill all required entries.")
                    
            

            
        if flag==0:
            f=0
            QMessageBox.about(self, "Query", st)
            s=dbn+".db"
            cn=sqlite3.connect(s)
            crob=cn.cursor()
            try:
                crob.execute(st)
            except:
                QMessageBox.about(self, "Message", "Some ERROR occured.")
                f=1
            if f==0:
                QMessageBox.about(self, "Message", "Table Created")
                cn1=sqlite3.connect("sqlgenerator.db")
                crob1=cn1.cursor()
                crob1.execute("INSERT INTO TName(tname,dbname,query)VALUES(?,?,?);",(tn,dbn,st))
                self.createtable.close()
                cn.commit()
                cn.close()
                cn1.commit()
                cn1.close()
        
            
        









    def retranslateUi(self, createtable):
        _translate = QtCore.QCoreApplication.translate
        createtable.setWindowTitle(_translate("createtable", "Create Table"))
        self.tablename.setText(_translate("createtable", "Table Name:"))
        self.createbutton.setText(_translate("createtable", "Create"))
        self.tabledetails.setTitle(_translate("createtable", "Table"))
        item = self.tablewidget.verticalHeaderItem(0)
        item.setText(_translate("createtable", "COLUMN"))
        item = self.tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("createtable", "FIELD"))
        item = self.tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("createtable", "TYPE"))
        item = self.tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("createtable", "SIZE"))
        item = self.tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("createtable", "CONSTRAINT"))
        self.removerowbutton.setText(_translate("createtable", "Remove Row"))
        self.addrowbutton.setText(_translate("createtable", "Add Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createtable = QtWidgets.QMainWindow()
    ui = Ui_createtable()
    ui.setupUi(createtable)
    createtable.show()
    
    sys.exit(app.exec_())

