# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountInfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountInfo(object):
    def setupUi(self, AccountInfo):
        AccountInfo.setObjectName("AccountInfo")
        AccountInfo.resize(600, 600)
        AccountInfo.setStyleSheet("background-color:rgb(33, 33, 33);\n"
"\n"
"")
        self.label = QtWidgets.QLabel(AccountInfo)
        self.label.setGeometry(QtCore.QRect(70, 60, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.accntinfo_back = QtWidgets.QPushButton(AccountInfo)
        self.accntinfo_back.setGeometry(QtCore.QRect(10, 10, 113, 41))
        self.accntinfo_back.setStyleSheet("background-color:rgb(39, 255, 36);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.accntinfo_back.setObjectName("accntinfo_back")
        self.accntinfo_continue = QtWidgets.QPushButton(AccountInfo)
        self.accntinfo_continue.setGeometry(QtCore.QRect(460, 540, 113, 41))
        self.accntinfo_continue.setStyleSheet("background-color:rgb(39, 255, 36);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.accntinfo_continue.setObjectName("accntinfo_continue")
        self.label_2 = QtWidgets.QLabel(AccountInfo)
        self.label_2.setGeometry(QtCore.QRect(40, 450, 391, 71))
        self.label_2.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(AccountInfo)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(AccountInfo)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(AccountInfo)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_5.setObjectName("label_5")
        self.address_label = QtWidgets.QLabel(AccountInfo)
        self.address_label.setGeometry(QtCore.QRect(50, 170, 461, 31))
        self.address_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.address_label.setText("")
        self.address_label.setObjectName("address_label")
        self.urlprogress_label = QtWidgets.QLabel(AccountInfo)
        self.urlprogress_label.setGeometry(QtCore.QRect(50, 290, 461, 31))
        self.urlprogress_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.urlprogress_label.setText("")
        self.urlprogress_label.setObjectName("urlprogress_label")
        self.filepath_label = QtWidgets.QLabel(AccountInfo)
        self.filepath_label.setGeometry(QtCore.QRect(50, 400, 461, 31))
        self.filepath_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.filepath_label.setText("")
        self.filepath_label.setObjectName("filepath_label")

        self.retranslateUi(AccountInfo)
        QtCore.QMetaObject.connectSlotsByName(AccountInfo)

    def retranslateUi(self, AccountInfo):
        _translate = QtCore.QCoreApplication.translate
        AccountInfo.setWindowTitle(_translate("AccountInfo", "Form"))
        self.label.setText(_translate("AccountInfo", "Account Information"))
        self.accntinfo_back.setText(_translate("AccountInfo", "Back"))
        self.accntinfo_continue.setText(_translate("AccountInfo", "Continue"))
        self.label_2.setText(_translate("AccountInfo", "This password will be used to encrypt your account. It is suggested you use a strong, uncommon password. You MUST remember this password. If you do not there is no way to decrypt your account. "))
        self.label_4.setText(_translate("AccountInfo", "Monitor Mining Progress At:"))
        self.label_3.setText(_translate("AccountInfo", "Your Address:"))
        self.label_5.setText(_translate("AccountInfo", "Account Info Saved At: (Do Not Delete File)"))
