# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewWallet.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.newWallet_back = QtWidgets.QPushButton(Form)
        self.newWallet_back.setGeometry(QtCore.QRect(20, 20, 113, 41))
        self.newWallet_back.setObjectName("newWallet_back")
        self.newWallet_continue = QtWidgets.QPushButton(Form)
        self.newWallet_continue.setGeometry(QtCore.QRect(450, 530, 113, 41))
        self.newWallet_continue.setObjectName("newWallet_continue")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 60, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 265, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(40, 205, 341, 31))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_passwordconfirm = QtWidgets.QLineEdit(Form)
        self.lineEdit_passwordconfirm.setGeometry(QtCore.QRect(40, 335, 341, 31))
        self.lineEdit_passwordconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwordconfirm.setObjectName("lineEdit_passwordconfirm")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 145, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 541, 71))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.newWallet_back.setText(_translate("Form", "Back"))
        self.newWallet_continue.setText(_translate("Form", "Continue"))
        self.label.setText(_translate("Form", "Create New Wallet"))
        self.label_4.setText(_translate("Form", "Confirm Password:"))
        self.label_3.setText(_translate("Form", "Choose Password: (min 8 characters)"))
        self.label_2.setText(_translate("Form", "This password will be used to encrypt your account. It is suggested you use a strong, uncommon password. You MUST remember this password. If you do not there is no way to decrypt your account. "))

