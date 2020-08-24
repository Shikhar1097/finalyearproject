# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altertable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_altertable(QWidget):
    dbname=''
    altertable=None
    rowcount=1
    strows=1
    def setupUi(self, altertable,dn):
        altertable.setObjectName("altertable")
        altertable.resize(784, 520)
        altertable.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(altertable)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 211, 381))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(74, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.select.setFont(font)
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(74, 470, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.done.setFont(font)
        self.done.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.done.setObjectName("done")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(223, 10, 20, 501))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabledetails = QtWidgets.QTableWidget(self.centralwidget)
        self.tabledetails.setGeometry(QtCore.QRect(250, 10, 521, 381))
        self.tabledetails.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Comic Sans MS\";")
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.setColumnCount(3)
        self.tabledetails.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tabledetails.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledetails.setHorizontalHeaderItem(2, item)
        self.addrow = QtWidgets.QPushButton(self.centralwidget)
        self.addrow.setGeometry(QtCore.QRect(250, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addrow.setFont(font)
        self.addrow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.addrow.setObjectName("addrow")
        self.removerow = QtWidgets.QPushButton(self.centralwidget)
        self.removerow.setGeometry(QtCore.QRect(664, 400, 111, 31))
        self.removerow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.removerow.setObjectName("removerow")
        self.addbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addbutton.setGeometry(QtCore.QRect(470, 400, 75, 31))
        self.addbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.addbutton.setObjectName("addbutton")
        altertable.setCentralWidget(self.centralwidget)

        self.retranslateUi(altertable)
        QtCore.QMetaObject.connectSlotsByName(altertable)






        


        item = QtWidgets.QTableWidgetItem('FIELD')
        self.tabledetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('TYPE')
        self.tabledetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('SIZE')
        self.tabledetails.setHorizontalHeaderItem(2, item)
        altertable.setFixedSize(784,520)
        self.tables.verticalHeader().setVisible(False)
        self.tabledetails.verticalHeader().setVisible(False)
        self.dbname=dn
        self.altertable=altertable
        self.select.clicked.connect(self.selectevent)
        self.done.clicked.connect(self.doneevent)
        self.addrow.clicked.connect(self.addrowevent)
        self.removerow.clicked.connect(self.removerowevent)
        self.addbutton.clicked.connect(self.addcolumnevent)
        
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
        self.altertable.close()


    def selectevent(self):
        query=''
        tn=self.tables.currentItem().text()
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
        self.rowcount=rc
        self.strows=rc



    def addrowevent(self):
        self.rowcount=self.rowcount+1
        self.tabledetails.setRowCount(self.rowcount)



    def removerowevent(self):
        if self.rowcount==0:
            QMessageBox.about(self, "Alert", "No rows present in the table.")
        else:
            self.rowcount=self.rowcount-1
            self.tabledetails.setRowCount(self.rowcount)

    def addcolumnevent(self):
        f=0
        query=''
        flag=0
        tn=self.tables.currentItem().text()
        result=''
        q='ALTER TABLE '+tn+' ADD '
        for i in range(self.strows,self.rowcount):
            if self.tabledetails.item(i,0)!=None and self.tabledetails.item(i,1)!=None and self.tabledetails.item(i,2)!=None:
                q=q+self.tabledetails.item(i,0).text()+' '+self.tabledetails.item(i,1).text()+'('+self.tabledetails.item(i,2).text()+'); '
                query=query+q
                q='ALTER TABLE '+tn+' ADD '
            else:
                f=1
        if f==1:
            QMessageBox.about(self, "Alert", "Fill all the required entries")
        elif f==0:
            cn=sqlite3.connect(self.dbname+'.db')
            crob=cn.cursor()
            try:
                crob.execute(query)
                QMessageBox.about(self, "Query", query)
            except:
                QMessageBox.about(self, "Alert", "Some Error Occured.")
                flag=1
            if flag==0:
                sql="SELECT sql FROM sqlite_master WHERE name='"+tn+"';"
        
                crob.execute(sql)

                result=crob.fetchone()
                for record in result:
                    print(record)
                    cn1=sqlite3.connect('sqlgenerator.db')
                    crob1=cn1.cursor()
                    crob1.execute("UPDATE TName SET query=? WHERE tname=? AND dbname=?",(record,tn,self.dbname))
                    cn1.commit()
                    cn1.close()
                    QMessageBox.about(self, "Message", "Table Altered")
            cn.commit()
            cn.close()
        















    def retranslateUi(self, altertable):
        _translate = QtCore.QCoreApplication.translate
        altertable.setWindowTitle(_translate("altertable", "Alter Table"))
        item = self.tables.verticalHeaderItem(0)
        item.setText(_translate("altertable", "New Row"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("altertable", "Tables"))
        self.select.setText(_translate("altertable", "Select"))
        self.done.setText(_translate("altertable", "DONE"))
        item = self.tabledetails.verticalHeaderItem(0)
        item.setText(_translate("altertable", "New Row"))
        item = self.tabledetails.horizontalHeaderItem(0)
        item.setText(_translate("altertable", "New Column"))
        item = self.tabledetails.horizontalHeaderItem(1)
        item.setText(_translate("altertable", "FIELD"))
        item = self.tabledetails.horizontalHeaderItem(2)
        item.setText(_translate("altertable", "SIZE"))
        self.addrow.setText(_translate("altertable", "Add Row"))
        self.removerow.setText(_translate("altertable", "Remove Row"))
        self.addbutton.setText(_translate("altertable", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    altertable = QtWidgets.QMainWindow()
    ui = Ui_altertable()
    ui.setupUi(altertable)
    altertable.show()
    sys.exit(app.exec_())

