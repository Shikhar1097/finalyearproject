# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sqlite3

class Ui_printmenu(QWidget):
    dbname=''
    printmenu=None
    def setupUi(self, printmenu,dn):
        printmenu.setObjectName("printmenu")
        printmenu.resize(844, 543)
        printmenu.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(printmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 211, 411))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(70, 450, 75, 31))
        self.select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.select.setObjectName("select")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(243, 10, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabledetails = QtWidgets.QTableWidget(self.centralwidget)
        self.tabledetails.setGeometry(QtCore.QRect(290, 10, 531, 411))
        self.tabledetails.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.setColumnCount(0)
        self.tabledetails.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(289, 440, 531, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.print = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.print.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.print.setObjectName("print")
        self.horizontalLayout.addWidget(self.print)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.tables.raise_()
        self.select.raise_()
        self.line.raise_()
        self.tabledetails.raise_()
        self.horizontalLayoutWidget.raise_()
        self.print.raise_()
        printmenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(printmenu)
        QtCore.QMetaObject.connectSlotsByName(printmenu)






        self.dbname=dn
        self.printmenu=printmenu
        printmenu.setFixedSize(844,543)
        self.cancel.clicked.connect(self.cancelevent)
        self.select.clicked.connect(self.selectevent)
        self.print.clicked.connect(self.printevent)
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
        self.printmenu.close()



    def selectevent(self):
        i=1
        tn=self.tables.currentItem().text()
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute('PRAGMA TABLE_INFO('+tn+')')
        titles = [tup[1] for tup in crob.fetchall()]
        for ch in titles:
            self.tabledetails.setColumnCount(i)
            item = QtWidgets.QTableWidgetItem()
            item.setText(ch)
            self.tabledetails.setHorizontalHeaderItem((i-1), item)
            i+=1
        crob.execute("SELECT * FROM "+tn)
        record=crob.fetchall()
        rc=1
        for entry in record:
            self.tabledetails.setRowCount(rc)
            cc=0
            for i in entry:
                item=QTableWidgetItem(str(i))
                self.tabledetails.setItem((rc-1), cc, item)
                cc+=1
            rc+=1
        cn.commit()
        cn.close()




    def printevent(self):
        if self.tabledetails.columnCount()==0:
            QMessageBox.about(self, "Alert", "No Table Selected")
        else:
            printer = QtPrintSupport.QPrinter()
            painter = QtGui.QPainter()
            painter.begin(printer)
            screen = self.tabledetails.grab()
            painter.drawPixmap(100, 100, screen)
            painter.end()
            QMessageBox.about(self, "Message", "Saved")
            self.printmenu.close()
















    def retranslateUi(self, printmenu):
        _translate = QtCore.QCoreApplication.translate
        printmenu.setWindowTitle(_translate("printmenu", "Print"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("printmenu", "Tables"))
        self.select.setText(_translate("printmenu", "Select"))
        self.print.setText(_translate("printmenu", "Print"))
        self.cancel.setText(_translate("printmenu", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    printmenu = QtWidgets.QMainWindow()
    ui = Ui_printmenu()
    ui.setupUi(printmenu)
    printmenu.show()
    sys.exit(app.exec_())

