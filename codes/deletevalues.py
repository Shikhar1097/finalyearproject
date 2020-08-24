# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletevalues.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_deletevalues(QWidget):
    dbname=''
    tname=''
    deletevalues=None
    def setupUi(self, deletevalues,dn):
        deletevalues.setObjectName("deletevalues")
        deletevalues.resize(781, 556)
        deletevalues.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(deletevalues)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 211, 381))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 409, 121, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.verticalLayout.addWidget(self.select)
        self.done = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.done.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.done.setObjectName("done")
        self.verticalLayout.addWidget(self.done)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 10, 20, 531))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.openedtable = QtWidgets.QTableWidget(self.centralwidget)
        self.openedtable.setGeometry(QtCore.QRect(260, 10, 511, 381))
        self.openedtable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.openedtable.setObjectName("openedtable")
        self.openedtable.setColumnCount(0)
        self.openedtable.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(259, 420, 511, 71))
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
        deletevalues.setCentralWidget(self.centralwidget)

        self.retranslateUi(deletevalues)
        QtCore.QMetaObject.connectSlotsByName(deletevalues)
        deletevalues.setFixedSize(781,556)








        self.dbname=dn
        self.deletevalues=deletevalues
        self.select.clicked.connect(self.selectevent)
        self.done.clicked.connect(self.doneevent)
        self.cancel.clicked.connect(self.doneevent)
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





    def selectevent(self):
        i=1
        tn=self.tables.currentItem().text()
        self.tname=tn
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



    def doneevent(self):
        self.deletevalues.close()


    def deleteevent(self):
        f=0
        item=self.openedtable.currentItem().text()
        r=self.openedtable.currentRow()
        c=self.openedtable.currentColumn()
        entry=self.openedtable.horizontalHeaderItem(c).text()
        if item.isdigit():
            fl=1
        elif item.isalpha():
            fl=0
        else:
            fl=1
        if fl==1:
            query="DELETE FROM "+self.tname+" WHERE "+entry+"="+item+";"
        else:
            query="DELETE FROM "+self.tname+" WHERE "+entry+"='"+item+"';"
            
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        try:
            crob.execute(query)
        except:
            QMessageBox.about(self, "Alert", "Some Error Occured.")
            f=1
        if f==0:
            QMessageBox.about(self, "Query", query)
            QMessageBox.about(self, "Message", "Deletion Done")
        cn.commit()
        cn.close()
        











    def retranslateUi(self, deletevalues):
        _translate = QtCore.QCoreApplication.translate
        deletevalues.setWindowTitle(_translate("deletevalues", "Delete Values"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("deletevalues", "Tables"))
        self.select.setText(_translate("deletevalues", "Select"))
        self.done.setText(_translate("deletevalues", "Done"))
        self.deletebutton.setText(_translate("deletevalues", "Delete"))
        self.cancel.setText(_translate("deletevalues", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deletevalues = QtWidgets.QMainWindow()
    ui = Ui_deletevalues()
    ui.setupUi(deletevalues)
    deletevalues.show()
    sys.exit(app.exec_())

