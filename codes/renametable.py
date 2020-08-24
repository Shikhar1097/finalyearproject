# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renametable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_renametable(QWidget):
    dbname=''
    renametable=None
    def setupUi(self, renametable,dn):
        renametable.setObjectName("renametable")
        renametable.resize(297, 441)
        renametable.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(renametable)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 271, 361))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.rename = QtWidgets.QPushButton(self.centralwidget)
        self.rename.setGeometry(QtCore.QRect(90, 390, 101, 23))
        self.rename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";")
        self.rename.setObjectName("rename")
        renametable.setCentralWidget(self.centralwidget)

        self.retranslateUi(renametable)
        QtCore.QMetaObject.connectSlotsByName(renametable)







        self.dbname=dn
        self.renametable=renametable
        renametable.setFixedSize(297,441)
        self.tables.verticalHeader().setVisible(False)
        self.rename.clicked.connect(self.renameevent)
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



    def renameevent(self):
        query=''
        tn=self.tables.currentItem().text()
        cn1=sqlite3.connect('sqlgenerator.db')
        crob1=cn1.cursor()
        crob1.execute("SELECT * FROM TName")
        record=crob1.fetchall()
        for entry in record:
            tname=str(entry[0])
            dbn=str(entry[1])
            if tname==tn and dbn==self.dbname:
                query=str(entry[2])
                      
        
        text,ok = QInputDialog.getText(self, 'Rename Table', 'Enter New Name:')
        txt=str(text)
        if txt=='':
            QMessageBox.about(self, "Alert", "Enter a valid table-name.")
        else:
            if ok:
                st="ALTER TABLE "+tn+" RENAME TO "+txt
                cn=sqlite3.connect(self.dbname+'.db')
                crob=cn.cursor()
                crob.execute(st)
                QMessageBox.about(self, "Query", st)
                
                crob1.execute("UPDATE TName SET tname=? WHERE dbname=? AND query=?;",(txt,self.dbname,query))
                sql="SELECT sql FROM sqlite_master WHERE name='"+txt+"';"
                crob.execute(sql)
                result=crob.fetchone()
                cn.commit()
                cn.close()
                for record in result:
                    print(record)
                    crob1.execute("UPDATE TName SET query=? WHERE tname=? AND dbname=?",(record,txt,self.dbname))
                cn1.commit()
                cn1.close()
                QMessageBox.about(self, "Message", "Table Renamed.")
                self.renametable.close()
            











    def retranslateUi(self, renametable):
        _translate = QtCore.QCoreApplication.translate
        renametable.setWindowTitle(_translate("renametable", "Rename Table"))
        item = self.tables.verticalHeaderItem(0)
        item.setText(_translate("renametable", "New Row"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("renametable", "Tables"))
        self.rename.setText(_translate("renametable", "Rename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    renametable = QtWidgets.QMainWindow()
    ui = Ui_renametable()
    ui.setupUi(renametable)
    renametable.show()
    sys.exit(app.exec_())

