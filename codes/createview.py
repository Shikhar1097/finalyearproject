# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createview.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_createview(QWidget):
    dbname=''
    tname=''
    createview=None
    def setupUi(self, createview,dn):
        createview.setObjectName("createview")
        createview.resize(831, 516)
        createview.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(createview)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(319, 10, 501, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 11pt \"Comic Sans MS\";\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.viewname = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.viewname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.viewname.setObjectName("viewname")
        self.horizontalLayout.addWidget(self.viewname)
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(20, 100, 221, 321))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(273, 10, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(90, 450, 75, 23))
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.tabledetails = QtWidgets.QTableWidget(self.centralwidget)
        self.tabledetails.setGeometry(QtCore.QRect(320, 100, 501, 321))
        self.tabledetails.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.setColumnCount(3)
        self.tabledetails.setRowCount(0)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(319, 440, 501, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.create.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.create.setObjectName("create")
        self.horizontalLayout_2.addWidget(self.create)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        createview.setCentralWidget(self.centralwidget)

        self.retranslateUi(createview)
        QtCore.QMetaObject.connectSlotsByName(createview)








        item = QtWidgets.QTableWidgetItem('FIELD')
        self.tabledetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('TYPE')
        self.tabledetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('SIZE')
        self.tabledetails.setHorizontalHeaderItem(2, item)
        self.dbname=dn
        self.createview=createview
        createview.setFixedSize(831,516)
        self.cancel.clicked.connect(self.cancelevent)
        self.select.clicked.connect(self.selectevent)
        self.create.clicked.connect(self.createevent)
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
        self.createview.close()




    def selectevent(self):
        query=''
        tn=self.tables.currentItem().text()
        self.tname=tn
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute('PRAGMA TABLE_INFO('+tn+')')
        titles = [tup[1] for tup in crob.fetchall()]
        cn1=sqlite3.connect('sqlgenerator.db')
        crob1=cn1.cursor()
        rc=1
        for ch in titles:
            i=rc-1
            self.tabledetails.setRowCount(rc)
            entry=QTableWidgetItem(ch)
            self.tabledetails.setItem(i, 0, entry)
            rc=rc+1
        crob1.execute("SELECT * from TName")
        record=crob1.fetchall()
        for entry in record:
            dbn=str(entry[1])
            tname=str(entry[0])
            if self.dbname==dbn and tname==tn:
                query=str(entry[2])
        cn.commit()
        cn.close()
        cn1.commit()
        cn1.close()
        start=query.index('(')+1
        temp=query[:(len(query)-1)]
        query=temp+","
        q=query[start:]
        word=""
        rc=0
        cc=1
        for ch in q:
            if ch==" ":
                word=""
            elif ch=="(":
                item=QTableWidgetItem(word)
                self.tabledetails.setItem(rc, cc, item)
                cc=cc+1
                word=""
            elif ch==")":
                item=QTableWidgetItem(word)
                self.tabledetails.setItem(rc, cc, item)
                cc=cc+1
                word=""
            elif ch==",":
                rc=rc+1
                cc=1
            else:
                word=word+ch



    def createevent(self):
        query=''
        q=''
        f=0
        if self.viewname.text()=='':
            QMessageBox.about(self, "Alert", "View Name not provided")
        else:
            vn=self.viewname.text()
            query="CREATE VIEW "+vn+" AS SELECT "
            cols=self.tabledetails.selectedItems()
            for i in cols:
                q+=i.text()+','
            query+=q[:len(q)-1]+" "+self.tname+" WHERE Discontinued = No;"
            QMessageBox.about(self, "Query", query)
            cn=sqlite3.connect(self.dbname+'.db')
            crob=cn.cursor()
            try:
                crob.execute(query)
            except:
                QMessageBox.about(self, "Alert", "Some error occured.")
                f=1
            if f==0:
                QMessageBox.about(self, "Message", "View Created.")
                cn1=sqlite3.connect('sqlgenerator.db')
                crob1=cn1.cursor()
                crob1.execute("INSERT INTO VName(vname,dbname)VALUES(?,?);",(vn,self.dbname))
                cn1.commit()
                cn1.close()
                self.createview.close()
            cn.commit()
            cn.close()
                
            
            
            









    def retranslateUi(self, createview):
        _translate = QtCore.QCoreApplication.translate
        createview.setWindowTitle(_translate("createview", "Create View"))
        self.label.setText(_translate("createview", "View Name:"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("createview", "Tables"))
        self.select.setText(_translate("createview", "Select"))
        self.create.setText(_translate("createview", "Create View"))
        self.cancel.setText(_translate("createview", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createview = QtWidgets.QMainWindow()
    ui = Ui_createview()
    ui.setupUi(createview)
    createview.show()
    sys.exit(app.exec_())

