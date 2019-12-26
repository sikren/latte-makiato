# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(26, 50, 711, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(706, 10, 31, 31))
        self.Add.setObjectName("Add")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(646, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(116, 20, 113, 20))
        self.Search.setObjectName("Search")
        self.Start_search = QtWidgets.QPushButton(self.centralwidget)
        self.Start_search.setGeometry(QtCore.QRect(246, 20, 75, 23))
        self.Start_search.setObjectName("Start_search")
        self.Confirm = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm.setGeometry(QtCore.QRect(610, 150, 121, 23))
        self.Confirm.setObjectName("Confirm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Add.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Add Coffee"))
        self.label_2.setText(_translate("MainWindow", "Search for edit"))
        self.Start_search.setText(_translate("MainWindow", "Search"))
        self.Confirm.setText(_translate("MainWindow", "Confirm"))
