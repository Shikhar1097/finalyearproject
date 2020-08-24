# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from createtable import Ui_createtable
from createusinganother import Ui_createusinganother
from opentable import Ui_opentable
from altertable import Ui_altertable
from renametable import Ui_renametable
from deletetable import Ui_deletetable
from createuser import Ui_createuser
from deleteuser import Ui_deleteuser
from insertvalues import Ui_insertvalues
from deletevalues import Ui_deletevalues
from fuvalues import Ui_fuvalues
from createview import Ui_createview
from deleteview import Ui_deleteview
from printmenu import Ui_printmenu
from dswindow import Ui_dswindow
from querybrowser import Ui_querybrowser
from helptopics import Ui_helptopics
from selectionwindow import Ui_selectionwindow
import sys





class Ui_mainwindow(QWidget):
    dbname=""
    un=""
    def setupUi(self, mainwindow,dn,uname):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(599, 418)
        mainwindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        self.menuTable = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuTable.setFont(font)
        self.menuTable.setObjectName("menuTable")

        
            
        self.menuDBA_Utilities = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuDBA_Utilities.setFont(font)
        self.menuDBA_Utilities.setObjectName("menuDBA_Utilities")
        self.menuManipulate = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuManipulate.setFont(font)
        self.menuManipulate.setObjectName("menuManipulate")
        self.menuView = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuView.setFont(font)
        self.menuView.setObjectName("menuView")
        self.menuAdvanced = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuAdvanced.setFont(font)
        self.menuAdvanced.setObjectName("menuAdvanced")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        mainwindow.setMenuBar(self.menubar)

        
        
        self.actionCreate_Table = QtWidgets.QAction(mainwindow)
        self.actionCreate_Table.setShortcut("")
        self.actionCreate_Table.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionCreate_Table.setObjectName("actionCreate_Table")
        self.actionCreate_Using_Another = QtWidgets.QAction(mainwindow)
        self.actionCreate_Using_Another.setObjectName("actionCreate_Using_Another")
        self.actionOpen_Table = QtWidgets.QAction(mainwindow)
        self.actionOpen_Table.setObjectName("actionOpen_Table")
        self.actionAlter_Table = QtWidgets.QAction(mainwindow)
        self.actionAlter_Table.setObjectName("actionAlter_Table")
        self.actionRename_Table = QtWidgets.QAction(mainwindow)
        self.actionRename_Table.setObjectName("actionRename_Table")
        self.actionDelete_Table = QtWidgets.QAction(mainwindow)
        self.actionDelete_Table.setObjectName("actionDelete_Table")





        self.actionCreate_New_User = QtWidgets.QAction(mainwindow)
        self.actionCreate_New_User.setObjectName("actionCreate_New_User")
        self.actionDelete_User = QtWidgets.QAction(mainwindow)
        self.actionDelete_User.setObjectName("actionDelete_User")
        self.actionInsert = QtWidgets.QAction(mainwindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionDelete = QtWidgets.QAction(mainwindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFind_Update = QtWidgets.QAction(mainwindow)
        self.actionFind_Update.setObjectName("actionFind_Update")
        self.actionCreate_View = QtWidgets.QAction(mainwindow)
        self.actionCreate_View.setObjectName("actionCreate_View")
        self.actionDelete_View = QtWidgets.QAction(mainwindow)
        self.actionDelete_View.setObjectName("actionDelete_View")


        


        self.actionPrint = QtWidgets.QAction(mainwindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionData_Structure = QtWidgets.QAction(mainwindow)
        self.actionData_Structure.setObjectName("actionData_Structure")
        self.actionQuery_Browser = QtWidgets.QAction(mainwindow)
        self.actionQuery_Browser.setObjectName("actionQuery_Browser")
        self.actionHelp_Topics = QtWidgets.QAction(mainwindow)
        self.actionHelp_Topics.setObjectName("actionHelp_Topics")
        self.menuTable.addAction(self.actionCreate_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionCreate_Using_Another)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionOpen_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionAlter_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionRename_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionDelete_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction("Conditional Selection")

        
        self.menuDBA_Utilities.addAction(self.actionCreate_New_User)
        self.menuDBA_Utilities.addSeparator()
        self.menuDBA_Utilities.addAction(self.actionDelete_User)
        self.menuManipulate.addAction(self.actionInsert)
        self.menuManipulate.addSeparator()
        self.menuManipulate.addAction(self.actionDelete)
        self.menuManipulate.addSeparator()
        self.menuManipulate.addAction(self.actionFind_Update)
        self.menuView.addAction(self.actionCreate_View)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDelete_View)


        
        
         
        self.menuAdvanced.addAction(self.actionPrint)
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.actionData_Structure)
        self.menuHelp.addAction(self.actionQuery_Browser)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelp_Topics)
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menuDBA_Utilities.menuAction())
        self.menubar.addAction(self.menuManipulate.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        self.dbname=dn
        self.un=uname
        





        

        self.menuTable.triggered[QtWidgets.QAction].connect(self.menufunctionTable)
        self.menuDBA_Utilities.triggered[QtWidgets.QAction].connect(self.menufunctionDBA)
        self.menuManipulate.triggered[QtWidgets.QAction].connect(self.menufunctionManipulate)
        self.menuView.triggered[QtWidgets.QAction].connect(self.menufunctionView)
        self.menuAdvanced.triggered[QtWidgets.QAction].connect(self.menufunctionAdvanced)
        self.menuHelp.triggered[QtWidgets.QAction].connect(self.menufunctionHelp)
        
               


    



    


    

    def menufunctionTable(self, action):
        txt= (action.text())
        if txt=='Create Table':
            self.createtablewindow()
        elif txt=='Create Using Another':
            self.createanotherwindow()
        elif txt=='Open Table':
            self.opentablewindow()
        elif txt=='Alter Table':
            self.altertablewindow()
        elif txt=='Rename Table':
            self.renametablewindow()
        elif txt=='Delete Table':
            self.deletetablewindow()
        elif txt=='Conditional Selection':
            self.spselectionwindow()


    def createtablewindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_createtable()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def createanotherwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_createusinganother()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def opentablewindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_opentable()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def altertablewindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_altertable()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def renametablewindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_renametable()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def deletetablewindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deletetable()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def spselectionwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_selectionwindow()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()




        
        
        

    def menufunctionDBA(self, action):
        txt= (action.text())
        if txt=='Create New User':
            self.createuserwindow()
        if txt=='Delete User':
            self.deleteuserwindow()
            


    def createuserwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_createuser()
        self.ui.setupUi(self.window,self.dbname)
        self.window.show()


    def deleteuserwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deleteuser()
        self.ui.setupUi(self.window,self.dbname,self.un)
        self.window.show()

    






    def menufunctionManipulate(self, action):
        txt= (action.text())
        if txt=='Insert':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_insertvalues()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()

        if txt=='Delete':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_deletevalues()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()

        if txt=='Find/Update':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_fuvalues()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()





        






    def menufunctionView(self,action):
        txt=(action.text())
        if txt=='Create View':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_createview()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()


        if txt=='Delete View':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_deleteview()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()






    def menufunctionAdvanced(self,action):
        txt=(action.text())
        if txt=='Print':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_printmenu()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()

        if txt=='Data Structure':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_dswindow()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()










    def menufunctionHelp(self,action):
        txt=(action.text())
        if txt=='Query Browser':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_querybrowser()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()

        if txt=='Help Topics':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_helptopics()
            self.ui.setupUi(self.window,self.dbname)
            self.window.show()







            

        






        

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "SQL Generator"))
        self.menuTable.setTitle(_translate("mainwindow", "Table"))
        self.menuDBA_Utilities.setTitle(_translate("mainwindow", "DBA Utilities"))
        self.menuManipulate.setTitle(_translate("mainwindow", "Manipulate"))
        self.menuView.setTitle(_translate("mainwindow", "View"))
        self.menuAdvanced.setTitle(_translate("mainwindow", "Advanced"))
        self.menuHelp.setTitle(_translate("mainwindow", "Help"))
        self.actionCreate_Table.setText(_translate("mainwindow", "Create Table"))
        self.actionCreate_Using_Another.setText(_translate("mainwindow", "Create Using Another"))
        self.actionOpen_Table.setText(_translate("mainwindow", "Open Table"))
        self.actionAlter_Table.setText(_translate("mainwindow", "Alter Table"))
        self.actionRename_Table.setText(_translate("mainwindow", "Rename Table"))
        self.actionDelete_Table.setText(_translate("mainwindow", "Delete Table"))
        self.actionCreate_New_User.setText(_translate("mainwindow", "Create New User"))
        self.actionDelete_User.setText(_translate("mainwindow", "Delete User"))
        self.actionInsert.setText(_translate("mainwindow", "Insert"))
        self.actionDelete.setText(_translate("mainwindow", "Delete"))
        self.actionFind_Update.setText(_translate("mainwindow", "Find/Update"))
        self.actionCreate_View.setText(_translate("mainwindow", "Create View"))
        self.actionDelete_View.setText(_translate("mainwindow", "Delete View"))
        self.actionPrint.setText(_translate("mainwindow", "Print"))
        self.actionData_Structure.setText(_translate("mainwindow", "Data Structure"))
        self.actionQuery_Browser.setText(_translate("mainwindow", "Query Browser"))
        self.actionHelp_Topics.setText(_translate("mainwindow", "Help Topics"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    mainwindow.showMaximized()
    sys.exit(app.exec_())


    
