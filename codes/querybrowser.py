# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querybrowser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from display import Ui_display
import sqlite3

class Ui_querybrowser(QWidget):
    dbname=''
    querybrowser=None
    def setupUi(self, querybrowser,dn):
        querybrowser.setObjectName("querybrowser")
        querybrowser.resize(536, 282)
        querybrowser.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"")
        self.centralwidget = QtWidgets.QWidget(querybrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.query = QtWidgets.QTextEdit(self.centralwidget)
        self.query.setGeometry(QtCore.QRect(20, 50, 491, 151))
        self.query.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.query.setObjectName("query")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 220, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exec = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exec.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.exec.setObjectName("exec")
        self.horizontalLayout.addWidget(self.exec)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        querybrowser.setCentralWidget(self.centralwidget)

        self.retranslateUi(querybrowser)
        QtCore.QMetaObject.connectSlotsByName(querybrowser)






        self.dbname=dn
        self.querybrowser=querybrowser
        querybrowser.setFixedSize(536,282)
        self.reset.clicked.connect(self.resetevent)
        self.exec.clicked.connect(self.execevent)
        QMessageBox.about(self, "Message", "Only provide actions supported by the GUI to avoid errors.")





    def resetevent(self):
        self.query.setText("")
        self.query.setFocus()





    def execevent(self):
        sw=''
        fw=''
        query=str(self.query.toPlainText())
        query=query.strip()
        query1=query.lower()
        f=0
        q=''
        count=0
        cn=sqlite3.connect(self.dbname+'.db')
        crob=cn.cursor()
        try:
            crob.execute(query)
        except:
            f=1
            QMessageBox.about(self, "Alert", "Some Error Occured.")
        cn.commit()
        cn.close()
        if f==0:
            QMessageBox.about(self, "Message", "Database Action Successfully Executed.")
            self.query.setText("")
            self.query.setFocus()
            for ch in query1:
                if ch!=' ':
                    q=q+ch
                else:
                    count+=1
                    if count==1:
                        fw=q
                        q=q+' '
                    if count==2:
                        sw=q
                        break


            if sw=='create table':
                cn=sqlite3.connect('sqlgenerator.db')
                crob=cn.cursor()
                start=query1.index('table')+6
                end=query1.index('(')
                tn=query[start:end]
                crob.execute("INSERT INTO TName(tname,dbname,query)VALUES(?,?,?);",(tn,self.dbname,query))
                cn.commit()
                cn.close()


            elif sw=='drop table':
                cn=sqlite3.connect('sqlgenerator.db')
                crob=cn.cursor()
                start=query1.index('table')+6
                tn=query[start:]
                crob.execute("DELETE FROM TName WHERE tname=? AND dbname=?;",(tn,self.dbname))
                cn.commit()
                cn.close()


            elif sw=='create view':
                cn=sqlite3.connect('sqlgenerator.db')
                crob=cn.cursor()
                start=query1.index('view')+5
                end=query1.index('as')-1
                tn=query[start:end]
                crob.execute("INSERT INTO VName(vname,dbname)VALUES(?,?);",(tn,self.dbname))
                cn.commit()
                cn.close()


            elif sw=='drop view':
                cn=sqlite3.connect('sqlgenerator.db')
                crob=cn.cursor()
                start=query1.index('view')+5
                tn=query[start:]
                crob.execute("DELETE FROM VName WHERE vname=? AND dbname=?;",(tn,self.dbname))
                cn.commit()
                cn.close()


            elif sw=='alter table':
                if query1.find('rename')>-1:
                    start=query1.index('table')+6
                    end=query1.index('rename')-1
                    tn=query[start:end]
                    start=query1.index('to')+3
                    ntn=query[start:]
                    cn=sqlite3.connect('sqlgenerator.db')
                    crob=cn.cursor()
                    crob.execute("SELECT * FROM TName")
                    record=crob.fetchall()
                    for entry in record:
                        tname=str(entry[0])
                        dbn=str(entry[1])
                        if tname==tn and dbn==self.dbname:
                            q=str(entry[2])
                    crob.execute("UPDATE TName SET tname=? WHERE dbname=? AND query=?;",(ntn,self.dbname,q))
                    cn.commit()
                    cn.close()
                    start=q.index('(')
                    qu=q[start:]
                    q="CREATE TABLE "+ntn+qu
                    cn=sqlite3.connect('sqlgenerator.db')
                    crob=cn.cursor()
                    crob.execute("UPDATE TName SET query=? WHERE tname=? AND dbname=?;",(q,ntn,self.dbname))
                    cn.commit()
                    cn.close()

                if  query1.find('add')>-1:
                    start=query1.index('table')+6
                    end=query1.index('add')-1
                    tn=query[start:end]
                    cn=sqlite3.connect(self.dbname+'.db')
                    crob=cn.cursor()
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
                    cn.commit()
                    cn.close()

            elif fw=='select':
                cn=sqlite3.connect(self.dbname+'.db')
                crob=cn.cursor()
                crob.execute(query)
                result=crob.fetchall()
                cn.commit()
                cn.close()
                
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_display()
                self.ui.setupUi(self.window,result)
                self.window.show()
                self.querybrowser.close()


            elif fw=='insert' or fw=='delete' or fw=='update':
                f=0


            else:
                QMessageBox.about(self, "Alert", "Action NOT supported by the Application. \nThis modification may not be seen in the application.")

                    
                    


            

            
                    
                
                
                
            
        
        
        
                     
                     
                
                














    def retranslateUi(self, querybrowser):
        _translate = QtCore.QCoreApplication.translate
        querybrowser.setWindowTitle(_translate("querybrowser", "Query Execution"))
        self.label.setText(_translate("querybrowser", " SQL Query:"))
        self.exec.setText(_translate("querybrowser", "Execute"))
        self.reset.setText(_translate("querybrowser", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    querybrowser = QtWidgets.QMainWindow()
    ui = Ui_querybrowser()
    ui.setupUi(querybrowser)
    querybrowser.show()
    sys.exit(app.exec_())

