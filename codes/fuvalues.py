# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuvalues.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_fuvalues(QWidget):
    dbname=''
    fuvalues=None
    tname=''
    def setupUi(self, fuvalues,dn):
        fuvalues.setObjectName("fuvalues")
        fuvalues.resize(799, 550)
        fuvalues.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(fuvalues)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tables.setGeometry(QtCore.QRect(10, 10, 201, 381))
        self.tables.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.tables.setObjectName("tables")
        self.tables.setColumnCount(1)
        self.tables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tables.setHorizontalHeaderItem(0, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 400, 131, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.find.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.find.setObjectName("find")
        self.verticalLayout.addWidget(self.find)
        self.update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.update.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font:10pt \"Comic Sans MS\";")
        self.update.setObjectName("update")
        self.verticalLayout.addWidget(self.update)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 10, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.values = QtWidgets.QTableWidget(self.centralwidget)
        self.values.setGeometry(QtCore.QRect(250, 10, 531, 381))
        self.values.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.values.setObjectName("values")
        self.values.setColumnCount(0)
        self.values.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 410, 531, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.updatefinal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.updatefinal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.updatefinal.setObjectName("updatefinal")
        self.horizontalLayout.addWidget(self.updatefinal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.done = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.done.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.done.setObjectName("done")
        self.horizontalLayout.addWidget(self.done)
        fuvalues.setCentralWidget(self.centralwidget)

        self.retranslateUi(fuvalues)
        QtCore.QMetaObject.connectSlotsByName(fuvalues)






        self.dbname=dn
        self.fuvalues=fuvalues
        fuvalues.setFixedSize(799,550)
        self.done.clicked.connect(self.doneevent)
        self.update.clicked.connect(self.updateevent)
        self.updatefinal.clicked.connect(self.updatefinalevent)
        self.find.clicked.connect(self.findevent)
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
        self.fuvalues.close()


    def updateevent(self):
        i=1
        tn=self.tables.currentItem().text()
        self.tname=tn
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        crob.execute('PRAGMA TABLE_INFO('+tn+')')
        titles = [tup[1] for tup in crob.fetchall()]
        for ch in titles:
            self.values.setColumnCount(i)
            item = QtWidgets.QTableWidgetItem()
            item.setText(ch)
            self.values.setHorizontalHeaderItem((i-1), item)
            i+=1
        crob.execute("SELECT * FROM "+tn)
        record=crob.fetchall()
        rc=1
        for entry in record:
            self.values.setRowCount(rc)
            cc=0
            for i in entry:
                item=QTableWidgetItem(str(i))
                self.values.setItem((rc-1), cc, item)
                cc+=1
            rc+=1
        cn.commit()
        cn.close()



    def updatefinalevent(self):
        f=0
        item=self.values.currentItem().text()
        r=self.values.currentRow()
        c=self.values.currentColumn()
        if c==0:
            d=1
        else:
            d=0
        if c!=-1:
            entry=self.values.horizontalHeaderItem(c).text()
            wc=self.values.horizontalHeaderItem(d).text()
            wce=self.values.item(r,d).text()
            if item.isalpha() and wce.isalpha():
                query="UPDATE "+self.tname+" SET "+entry+"='"+item+"' WHERE "+wc+"="+"'"+wce+"';"
            elif item.isalpha():
                query="UPDATE "+self.tname+" SET "+entry+"='"+item+"' WHERE "+wc+"="+wce+";"
            elif wce.isalpha():
                query="UPDATE "+self.tname+" SET "+entry+"="+item+" WHERE "+wc+"="+"'"+wce+"';"
            else:
                query="UPDATE "+self.tname+" SET "+entry+"="+item+" WHERE "+wc+"="+wce+";"
            cn=sqlite3.connect(self.dbname+'.db')
            crob=cn.cursor()
            try:
                crob.execute(query)
            except:
                QMessageBox.about(self, "Alert", "Some Error Occured.")
                f=1
            if f==0:
                QMessageBox.about(self, "Query", query)
                QMessageBox.about(self, "Message", "Updation done.")
            cn.commit()
            cn.close()
        else:
           QMessageBox.about(self, "Alert", "Update Not Possible.")



    def findevent(self):
        f=0
        tn=self.tables.currentItem().text()
        text,ok = QInputDialog.getText(self, 'Find Entry', 'Entry :')
        txt=str(text)
        if txt=='':
            QMessageBox.about(self, "Alert", "Textbox Empty.")
        else:
            if ok:
                cn=sqlite3.connect(self.dbname+'.db')
                crob=cn.cursor()
                crob.execute("SELECT * FROM "+tn+";")
                record=crob.fetchall()
                cn.commit()
                cn.close()
                for result in record:
                    for entry in result:
                        if str(entry)==txt:
                            f+=1
                            break
                if f>0:
                    QMessageBox.about(self, "Message", "Entry present.")
                    i=1
                    tn=self.tables.currentItem().text()
                    cn=sqlite3.connect(self.dbname+'.db')
                    crob=cn.cursor()
                    crob.execute('PRAGMA TABLE_INFO('+tn+')')
                    titles = [tup[1] for tup in crob.fetchall()]
                    for ch in titles:
                        self.values.setColumnCount(i)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(ch)
                        self.values.setHorizontalHeaderItem((i-1), item)
                        i+=1
                    crob.execute("SELECT * FROM "+tn)
                    record=crob.fetchall()
                    rc=1
                    for entry in record:
                        self.values.setRowCount(rc)
                        cc=0
                        for i in entry:
                            item=QTableWidgetItem(str(i))
                            self.values.setItem((rc-1), cc, item)
                            cc+=1
                        rc+=1
                    cn.commit()
                    cn.close()
                    rc-=1
                    print(str(rc)+" "+str(cc))
                    for n in range(0,rc):
                        for m in range(0,cc):
                            if str(self.values.item(n,m).text())==txt:
                                self.values.setRangeSelected(QTableWidgetSelectionRange(n, m, n, m), True)
                             
                                        
                else:
                    QMessageBox.about(self, "Message", "Entry not present in the table.") 
                    i=1
                    tn=self.tables.currentItem().text()
                    cn=sqlite3.connect(self.dbname+'.db')
                    crob=cn.cursor()
                    crob.execute('PRAGMA TABLE_INFO('+tn+')')
                    titles = [tup[1] for tup in crob.fetchall()]
                    for ch in titles:
                        self.values.setColumnCount(i)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(ch)
                        self.values.setHorizontalHeaderItem((i-1), item)
                        i+=1
                    crob.execute("SELECT * FROM "+tn)
                    record=crob.fetchall()
                    rc=1
                    for entry in record:
                        self.values.setRowCount(rc)
                        cc=0
                        for i in entry:
                            item=QTableWidgetItem(str(i))
                            self.values.setItem((rc-1), cc, item)
                            cc+=1
                        rc+=1
                    cn.commit()
                    cn.close()













    def retranslateUi(self, fuvalues):
        _translate = QtCore.QCoreApplication.translate
        fuvalues.setWindowTitle(_translate("fuvalues", "Find/Update Values"))
        item = self.tables.horizontalHeaderItem(0)
        item.setText(_translate("fuvalues", "Tables"))
        self.find.setText(_translate("fuvalues", "Find"))
        self.update.setText(_translate("fuvalues", "Update"))
        self.updatefinal.setText(_translate("fuvalues", "Update"))
        self.done.setText(_translate("fuvalues", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fuvalues = QtWidgets.QMainWindow()
    ui = Ui_fuvalues()
    ui.setupUi(fuvalues)
    fuvalues.show()
    sys.exit(app.exec_())

