# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MiningWallet.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MiningWallet(object):
    def setupUi(self, MiningWallet):
        MiningWallet.setObjectName("MiningWallet")
        MiningWallet.resize(600, 600)
        MiningWallet.setStyleSheet("background-color:rgb(33, 33, 33);\n"
"")
        self.label = QtWidgets.QLabel(MiningWallet)
        self.label.setGeometry(QtCore.QRect(70, 50, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.create_wallet_pb = QtWidgets.QPushButton(MiningWallet)
        self.create_wallet_pb.setGeometry(QtCore.QRect(170, 170, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.create_wallet_pb.setFont(font)
        self.create_wallet_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.create_wallet_pb.setObjectName("create_wallet_pb")
        self.label_2 = QtWidgets.QLabel(MiningWallet)
        self.label_2.setGeometry(QtCore.QRect(260, 280, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_wallet_no = QtWidgets.QLineEdit(MiningWallet)
        self.lineEdit_wallet_no.setGeometry(QtCore.QRect(170, 423, 271, 30))
        self.lineEdit_wallet_no.setStyleSheet("background-color:rgb(105, 105, 105);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lineEdit_wallet_no.setObjectName("lineEdit_wallet_no")
        self.label_3 = QtWidgets.QLabel(MiningWallet)
        self.label_3.setGeometry(QtCore.QRect(10, 413, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.add_wallet_pb = QtWidgets.QPushButton(MiningWallet)
        self.add_wallet_pb.setGeometry(QtCore.QRect(450, 420, 131, 41))
        self.add_wallet_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.add_wallet_pb.setObjectName("add_wallet_pb")
        self.label_4 = QtWidgets.QLabel(MiningWallet)
        self.label_4.setGeometry(QtCore.QRect(70, 340, 431, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.miningwallet_back = QtWidgets.QPushButton(MiningWallet)
        self.miningwallet_back.setGeometry(QtCore.QRect(20, 11, 113, 41))
        self.miningwallet_back.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.miningwallet_back.setObjectName("miningwallet_back")

        self.retranslateUi(MiningWallet)
        QtCore.QMetaObject.connectSlotsByName(MiningWallet)

    def retranslateUi(self, MiningWallet):
        _translate = QtCore.QCoreApplication.translate
        MiningWallet.setWindowTitle(_translate("MiningWallet", "Form"))
        self.label.setText(_translate("MiningWallet", "Mining Wallet"))
        self.create_wallet_pb.setText(_translate("MiningWallet", "Create New Wallet"))
        self.label_2.setText(_translate("MiningWallet", "OR"))
        self.label_3.setText(_translate("MiningWallet", "Enter Wallet Number:"))
        self.add_wallet_pb.setText(_translate("MiningWallet", "Add Wallet"))
        self.label_4.setText(_translate("MiningWallet", "<html><head/><body><p><span style=\" color:#ffffff;\">If you already have a wallet for the selected currency, enter it below. Note that if you enter an incorrect wallet number you may not receive funds.</span></p></body></html>"))
        self.miningwallet_back.setText(_translate("MiningWallet", "Back"))

