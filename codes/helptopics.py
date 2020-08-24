# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helptopics.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_helptopics(QWidget):
    helptopics=None
    dbname=''
    def setupUi(self, helptopics,dn):
        helptopics.setObjectName("helptopics")
        helptopics.resize(788, 433)
        helptopics.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(helptopics)
        self.centralwidget.setObjectName("centralwidget")
        self.modules = QtWidgets.QListWidget(self.centralwidget)
        self.modules.setGeometry(QtCore.QRect(10, 10, 201, 361))
        self.modules.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.modules.setObjectName("modules")
        self.details = QtWidgets.QTextEdit(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(260, 10, 521, 361))
        self.details.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Comic Sans MS\";")
        self.details.setObjectName("details")
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(340, 390, 101, 31))
        self.done.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.done.setObjectName("done")
        helptopics.setCentralWidget(self.centralwidget)

        self.retranslateUi(helptopics)
        QtCore.QMetaObject.connectSlotsByName(helptopics)







        self.details.setText("Double Click on module to know about it.")
        self.dbname=dn
        self.helptopics=helptopics
        self.done.clicked.connect(self.closeWindow)
        modulesentry = ["Create Table","Create Using Another","Open Table","Alter Table","Rename Table","Delete Table","Conditional Selection","Create New User","Delete User","Insert","Delete","Find/Update","Create View","Delete View","Print","Data Structure","Query Browser"]
        for entry in modulesentry:
            self.modules.addItem(entry)

        self.modules.itemDoubleClicked.connect(self.printdetails)
        self.details.setReadOnly(True)




    def printdetails(self,item):
        txt=item.text()
        if txt=='Create Table':
            self.details.setText('''Create Table:

This module provides the user a function to create a table within the currently accessed database. The created table remains accessible throughout the application including the query browser, where the user is required to type the SQL query to carry out any specific SQL task.

Module Details:

The contents included in this module are- table name and table details.
The user is required to enter values in all the fields in order to successfully create a table. Firstly, the user user has to provide a name for the table to be created. Secondly, the details of all the columns to be included in the table are required to be provided. The user has to enter the name of each column, type of data it would be holding, maximun length og the data and any specific constraint for the column if required(constraint is not mandatory).

Module Fucntionality:

The module works as follows-
The user can add a new row to enter details for a new column using ADD ROW button.
The user can delete a row using REMOVE ROW button.
The CREATE button should be clicked in order to finally create the new table. The table is successfully created only if all the mandatory fields are provided with relevant data.''')
        elif txt=='Create Using Another':
            self.details.setText('''Create Using Another:

This module allows the user to create a new table within the current database being accessed by the application. The basic difference between the create table module and this module is that, in this module the tables are created using a pre-existing table within the current database, the user is required only to provide the table name for the new table.

Module Details:

The contents included in this module are- the list of tables available and some event handling buttons.
The user is provided with a list of all the tables present in the currently accessed database. The user may select any table from the given list and just provide the name for the new table. Thus, a new table, with the new name and same description as of the selected table, will be created.

Module Functionality:

The user is provided with a list of all the tables present in the current database. The user is required to select a table and click on the select button. On clicking the select button a prompt box appears asking for the name of the new table, the user has to enter the name for the new table and click on ok. Thus, a new table is created with the new name as provided using the prompt box and the attributes and the details of the attributes are same as the table selected to create a new table.
The user can click on cancel button to close the window.''')
        elif txt=='Open Table':
            self.details.setText('''Open Table:

This module allows the user to select a certain already or previously created table(within the currently accessed database) and view all the contents of that table. The tables in option are all those which are present in the current database, no external table can be accessed.

Module Details:

The contents of this module include- the list of the tables, from which the user may choose any table to view its contents, some event handling buttons for performing operations and an area that displays the contents of the selected table.

Module Functionality:

The user is provided with a list of all the tables present in the current database as he opens this module. An open button is avaialable on the left side of the display box, the user is required to select the table which he wants to view, and clicl on the open button. As the user clicks on the open table button, all the contents of the selected table can be seen in the area on the right of the display box.''')
        elif txt=='Alter Table':
            self.details.setText('''Alter Table:

The Alter Table Module allows the user to alter any pre-existing table within the current database. In other words, if the user desires to alter the table that he has already created, he may use this module to do so. The alter table command in SQLite allows the user to add or remove columns from a pre-existing table.

Module Details:

The contents of this module include-a list of all the pre-existing tables within the current database, one of which is to be altered, a table with three columns that is required to be filled accordingly in order to provide the complete details of the new column that is to added, a select button to select the current table to be altered, a done button to close the window, add row and remove row button to add and remove row from the column details table and the add button to add the columns to the selected table.

Module Functionality:

The module provides the select button to select a table to be altered from the given list of pre-existing tables. The user selects a table that is to be altered, and fills in the details of the column that is to be altered. The user may add a row or remove a row from the column details table on the right to change the number of columns to be added to the selected row. The Add button is pushed by the user to finally add the column/s to the selected table.''')
        elif txt=='Rename Table':
            self.details.setText('''Rename Table:

The Rename Table Window provides the user a feature where the user is allowed to change the name of any pre-existing table of the current database. The rename window is nothing but a list of pre-existing tables in the current database.

Module Details:

The contents of this module include a list of all the pre-existing tables within the current module, a Rename button, which is clicked to rename the selected table.

Module Functionality:

The user can carry out the Rename Table operation by selecting a table from the list of the pre-existing tables, and click on the rename button. As the user clicks on the rename button, a new window pops up asking the new name for the selected table. The user can enter the new name and click OK to rename the table or just click on the Cancel button to abort the operation.''')
        elif txt=='Delete Table':
            self.details.setText('''Delete Table:

The Delete Table Window is a module that allows the user to delete a pre-existing table from the currently accessed database. The window contains a list of all the pre-existing tables present in the current database, from which the user may select a table to delete it permanently from the database.

Module Details:

The contents of this module include a list of all the existing tables within the currently accessed database, a cancel button to cancel or abort the deletion process or in other words, close the delete table window and the delete button to delete the selected table permanently.

Module Functionality:

The module works as; the complete list of all existing tables within the current database is presented to the user. The user is then supposed to select the table which he wants to delete and then click on delete button to permanently delete that table. The user may also click on the cancel button to abort the deletion process and kill the delete table window.''')
        elif txt=='Conditional Selection':
            self.details.setText('''Conditional Selection:

The Conditional Selection is a module that allows the user to perform any specific or conditional selection, i.e. when the user wants to put any extra filters for the data that is to be selected via the SELECT statement. The clauses included for conditional selection procedure are Where, Like, Glob, Limit, Distinct, Order By, Group By and Having.

Module Details:

The contents of the module include a drop down menu to select the clause that the user desires to employ within his conditional selection statement, the clauses that he may select from vary in both, the syntax of the query as well as the effect of the data fetched, the Open button to open the query window on the basis of the selected clause and the cancel button to abort the process or close the window.

Module Functionality:

The Conditional Selection process works as the user is first provided with a list of clauses supported by the software to employ any one of them in his SELECT query. Once the user selects the desired clause and clicks on the Open button, the query window opens up to enter the query for the selection based on the syntax working for the selected clause. After filling the entries of the query window, the user is supposed to click on the execute button. As the execute button is clicked, the generated Select query is executed and the result fetched from the database is presented to the user with the help of the Display window.''')
        elif txt=='Create New User':
            self.details.setText('''Create New User:

The Create User Window is a module that allows a user to add new users to the software, or in other words, it helps a user to give access to other users by authorizing them to login (providing a username and a password). The process can be done by any user be it the admin or just another user, in order to provide limited access to all the users allowing them to enjoy all the features of the software without jeopardising the security of the data of other users.

Module Details:

The contents of the module include several text fields to enter the username of the new user, a password feed and a confirm password feed, a create button to execute the creation of the new user with the entered login credentials and a reset button to reset all the entries, i.e. clear all the entered data and set the cursor to Create Username.

Module Functionality:

This module works as, the user is required to enter the username and desired password for the new user. The confirm password feed requires the password to be re-entered, if it mismatches or any entry is missing corresponding error is prompted by the software. After correctly filling all the entries, the user is supposed to click the Create button to successfully save the details of the user in the software. If the user wants to reset all the entries, he may click on the Reset button.''')
        elif txt=='Delete User':
            self.details.setText('''Delete User:

The Delete User Window is a module that allows a user to delete the details of any other user, i.e. take away the authorization to access the software. The user is first provided with the list of all the users of the software, he can then select the user he wants to delete and delete him. Only the non-admin users can be deleted from the software and not the admin.

Module Details:

The contents of the module include a list of all the users having the authority to access the software along with the their property, a Delete button to carry out the delete user process and the cancel button to close the window and abort the procedure.

Module Functionality:

The module works as follows-
The user is provided with a list of all the users of the software along with their properties. Any user is only allowed to delete a non-admin user, i.e. credentials of the admin of the software cannot be deleted. The user then may select the user he wants to delete and click on the delete button, or just click on the cancel button to close the window.
''')
        elif txt=='Insert':
            self.details.setText('''Insert:

The insert value module is the module that allows the user to store some values within a table of the current database. The process is carried out as the desired value to be stored is passed as input to this module by the user on the basis of the number of columns in the table, keeping in account the special properties of all the columns.

Module Details:

The contents of the module include a list of all the tables present in the current database for the user to select the one in which he wants to enter the values, a table from where the data to be stored in the table is entered on the basis of the column in which it is to be entered, a select button to select a table from the list of tables, a done button to close the window, an add and remove row button to manage the number of entries to be stored in the table and the Insert button to execute the insertion process.

Module Functionality:

The process of inserting values within a table is carried out as; firstly the user is required to select the table in which he wants to enter the value, from the list of tables and click on the select button, then he should enter all the data that is to be entered in the table, using add and remove row button. At last to execute the process the user has to click on the insert button. ''')
        elif txt=='Delete':
            self.details.setText('''Delete:

The Delete Values Window is a module that allows the user to permanently delete some specific row from a table in the current database. The deletion process is done by using some entry present in any column of the row that is required to be deleted. The deletion process in done by taking a value as input and deleting the complete row containing that value.

Module Details:

The contents of the module include a list of all the tables present in the current database for the user to select the desired table, a select button to select the current table, a done button to close the window, a table showing all the data present in the table, a delete button to delete the row of the currently selected data and a cancel button to abort the deletion process.

Module Functionality:

The module works as the user selects the desired table from the list of tables, and then selects any data of the row that he wants to delete. Now as he clicks on the delete button, the complete row of current data gets deleted from the table. ''')
        elif txt=='Find/Update':
            self.details.setText('''Find/Update:

The Find/Update Window is a module that allows the user to check the table for the presence of some specific data, or update some data present in the table, i.e. the user may send a value as input to the module and the module will check the table for the presence of that data and mark the cells in which the data is present, and show a message if no such data is present. The updation is done by editing any cell whose value is to be updated (only one value can be updated at a time).

Module Details:

The contents of the module include a list of the all the tables present in the current database, a find button to initiate the Find operation, a update button to initiate and finalize the Update operation, a space to open the selected table and done button to close the window.

Module Functionality:

The module works in the way that the user selects the desired table from the list of the tables and clicks on the find or update button as per his choice. The Find button opens up a prompt box asking for the value to find within the table, as the user clicks OK, the module marks all the cells that contain that value if present, or displays a ‘not found’ message. While, if the user clicks on the update button, the table opens up and the user is allowed to update any single cell at a time and click on the update button on the right to execute or save the updation. ''')
        elif txt=='Create View':
            self.details.setText('''Create View:

The Create View Window is a module that provides the user a feature to create a view for any table in order to have a specific view for some part of the table. A view is a part of some table that is created by the user and saved distinctly.

Module Details:

The contents of the module include the list of all the tables present in the current database, a select button to select the current table from the list, a table to select the columns from the table that may be the part of the view, a create view button to execute the view creation process and cancel button to close the window.

Module Functionality:

The user is present with the list of all the tables present within the database, and he selects the table for which the view is to be created by clicking on the select button. The user then selects all the columns of the table which he wants to include within the view and clicks on the create view button to finalize the procedure. The user may also click the cancel button to abort the process. ''')
        elif txt=='Delete View':
            self.details.setText('''Delete View:

The Delete View Window is a module that provides the software a feature to delete some previously created view that was created by the user for some specific table. The delete view procedure is carried out by, selecting the desired view from the list of all the views present and then delete it, this way the view gets permanently deleted from the database.

Module Details:

The contents of the module include the list of all the views present within the database for the user to select the desired one and delete it, a delete button to confirm and execute the deletion process and the cancel button to close the window or abort the deletion procedure.

Module Functionality:

The working of this module can be described as, first the user is provided the list of all the views present within the database as he opens the module, then the user is required to click on the desired view that he wants to delete and then click on the delete view button to permanently remove it from the database. The user may also click on the cancel button to close the window.''')
        elif txt=='Print':
            self.details.setText('''Print:

The print window module is one of the most helpful module within the software as it provides the feature to print any table present within the database, or just save the table to some other external file. This is done by exporting the file to a pdf or xps file.

Module Details:

The contents of the module include the list of the tables present within the current database for the user to select the desired table to be printed or externally saved, a space to open the selected table, a select button to select the current table and open it in the given space, a print button to save the file as some external file and cancel button to close the window and abort the process.

Module Functionality:

The working of the module is defined as the user is first provided with the list of all the tables present within the database, and he selects the desired table to save it as an external file. After the table is opened in the given space, the user may click on the print button to open the Save File window to save the table as an external file. There the user is just required to specify the location and name of the file to be saved. The user may also click on cancel button to close the window.''')
        elif txt=='Data Structure':
            self.details.setText('''Data Structure:

The Data Structure Window is a module that allows the user to view the data structure of the selected table. The data structure refers to the structure of the table, i.e. the name of all the columns within the table within their type, size and constraint. The software displays the data structure to the user in form of the table creation query of the selected table.

Module Details:

The contents of the module include a drop down menu to select the desired table from the list of the tables present in the current database, a data structure field to display the structure of the selected table, a select button to select the current table from the list and display the structure of that table in the display field and cancel button to close the window.

Module Functionality:

The user is required to select the desired table from the list of the tables present in the current database to view its structure. After the user selects the table he should click on the Select button to view its structure displayed in the Data Structure field. The user may also click on the cancel button to close the window.''')
        elif txt=='Query Browser':
            self.details.setText('''Query Browser:

The Query Browser is a module that provides an additional feature to the software where the user is allowed to type the SQL Queries and execute them. This feature makes the software flexible and does not bind the user to use only one technique to perform his operations over the database as well as data. 
The software allows only those database operations to be performed by typing SQL queries which are supported or offered by the GUI, and if any other action is executed using the query browser, the user may face ambiguity or errors within the software, as the software may not be able to update itself along with the database. 

Module Details:

The module contents include a text field that may be used by the user to type in the SQL queries, the execute button to execute the queries written in the text field and cancel button to kill the window.

Module Functionality:

The module opens up when the user clicks on the query browser option of the Help drop down menu. The user is required to enter the SQL query, of the operation he intends to perform over the database with the help of the software, in the text field and click on the execute button to execute it. The user may also click on the cancel button to close the window.''')
        


        

    


        




    def closeWindow(self):
        self.helptopics.close()











    def retranslateUi(self, helptopics):
        _translate = QtCore.QCoreApplication.translate
        helptopics.setWindowTitle(_translate("helptopics", "Help"))
        self.done.setText(_translate("helptopics", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    helptopics = QtWidgets.QMainWindow()
    ui = Ui_helptopics()
    ui.setupUi(helptopics)
    helptopics.show()
    sys.exit(app.exec_())

