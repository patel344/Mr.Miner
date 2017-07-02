# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewWallet.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateNewWallet(object):
    def setupUi(self, CreateNewWallet):
        CreateNewWallet.setObjectName("CreateNewWallet")
        CreateNewWallet.resize(600, 600)
        CreateNewWallet.setStyleSheet("background-color:rgb(33,33,33);")
        self.newWallet_back = QtWidgets.QPushButton(CreateNewWallet)
        self.newWallet_back.setGeometry(QtCore.QRect(20, 20, 113, 41))
        self.newWallet_back.setStyleSheet("background-color:rgb(39, 255, 36);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.newWallet_back.setObjectName("newWallet_back")
        self.newWallet_continue = QtWidgets.QPushButton(CreateNewWallet)
        self.newWallet_continue.setGeometry(QtCore.QRect(450, 530, 113, 41))
        self.newWallet_continue.setStyleSheet("background-color:rgb(39, 255, 36);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.newWallet_continue.setObjectName("newWallet_continue")
        self.label = QtWidgets.QLabel(CreateNewWallet)
        self.label.setGeometry(QtCore.QRect(80, 60, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(CreateNewWallet)
        self.label_4.setGeometry(QtCore.QRect(40, 265, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255,255,255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_password = QtWidgets.QLineEdit(CreateNewWallet)
        self.lineEdit_password.setGeometry(QtCore.QRect(40, 205, 341, 31))
        self.lineEdit_password.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_passwordconfirm = QtWidgets.QLineEdit(CreateNewWallet)
        self.lineEdit_passwordconfirm.setGeometry(QtCore.QRect(40, 335, 341, 31))
        self.lineEdit_passwordconfirm.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.lineEdit_passwordconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwordconfirm.setObjectName("lineEdit_passwordconfirm")
        self.label_3 = QtWidgets.QLabel(CreateNewWallet)
        self.label_3.setGeometry(QtCore.QRect(40, 145, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(CreateNewWallet)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 541, 71))
        self.label_2.setStyleSheet("color:rgb(255,255,255);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CreateNewWallet)
        QtCore.QMetaObject.connectSlotsByName(CreateNewWallet)

    def retranslateUi(self, CreateNewWallet):
        _translate = QtCore.QCoreApplication.translate
        CreateNewWallet.setWindowTitle(_translate("CreateNewWallet", "Form"))
        self.newWallet_back.setText(_translate("CreateNewWallet", "Back"))
        self.newWallet_continue.setText(_translate("CreateNewWallet", "Continue"))
        self.label.setText(_translate("CreateNewWallet", "Create New Wallet"))
        self.label_4.setText(_translate("CreateNewWallet", "Confirm Password:"))
        self.label_3.setText(_translate("CreateNewWallet", "Choose Password: (min 8 characters)"))
        self.label_2.setText(_translate("CreateNewWallet", "This password will be used to encrypt your account. It is suggested you use a strong, uncommon password. You MUST remember this password. If you do not there is no way to decrypt your account. "))

