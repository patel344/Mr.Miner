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
        MiningWallet.resize(632, 600)
        MiningWallet.setStyleSheet("background-color:rgb(33, 33, 33);\n"
"")
        self.label = QtWidgets.QLabel(MiningWallet)
        self.label.setGeometry(QtCore.QRect(100, 80, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.create_wallet_pb = QtWidgets.QPushButton(MiningWallet)
        self.create_wallet_pb.setGeometry(QtCore.QRect(210, 210, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.create_wallet_pb.setFont(font)
        self.create_wallet_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.create_wallet_pb.setObjectName("create_wallet_pb")
        self.label_2 = QtWidgets.QLabel(MiningWallet)
        self.label_2.setGeometry(QtCore.QRect(300, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_wallet_no = QtWidgets.QLineEdit(MiningWallet)
        self.lineEdit_wallet_no.setGeometry(QtCore.QRect(200, 460, 271, 30))
        self.lineEdit_wallet_no.setStyleSheet("background-color:rgb(105, 105, 105);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lineEdit_wallet_no.setObjectName("lineEdit_wallet_no")
        self.label_3 = QtWidgets.QLabel(MiningWallet)
        self.label_3.setGeometry(QtCore.QRect(10, 453, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.add_wallet_pb = QtWidgets.QPushButton(MiningWallet)
        self.add_wallet_pb.setGeometry(QtCore.QRect(479, 455, 131, 40))
        self.add_wallet_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.add_wallet_pb.setObjectName("add_wallet_pb")
        self.label_4 = QtWidgets.QLabel(MiningWallet)
        self.label_4.setGeometry(QtCore.QRect(100, 380, 431, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.miningwallet_back = QtWidgets.QPushButton(MiningWallet)
        self.miningwallet_back.setGeometry(QtCore.QRect(20, 13, 113, 41))
        self.miningwallet_back.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.miningwallet_back.setObjectName("miningwallet_back")
        self.igalmelapela = QtWidgets.QPushButton(MiningWallet)
        self.igalmelapela.setEnabled(True)
        self.igalmelapela.setGeometry(QtCore.QRect(570, 10, 51, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.igalmelapela.setPalette(palette)
        self.igalmelapela.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ChooseCurrency/Logo_green-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.igalmelapela.setIcon(icon)
        self.igalmelapela.setIconSize(QtCore.QSize(60, 60))
        self.igalmelapela.setFlat(True)
        self.igalmelapela.setObjectName("igalmelapela")
        self.label_5 = QtWidgets.QLabel(MiningWallet)
        self.label_5.setGeometry(QtCore.QRect(100, 160, 431, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(MiningWallet)
        QtCore.QMetaObject.connectSlotsByName(MiningWallet)

    def retranslateUi(self, MiningWallet):
        _translate = QtCore.QCoreApplication.translate
        MiningWallet.setWindowTitle(_translate("MiningWallet", "Mr.Miner"))
        self.label.setText(_translate("MiningWallet", "Mining Wallet"))
        self.create_wallet_pb.setText(_translate("MiningWallet", "Create New Wallet"))
        self.label_2.setText(_translate("MiningWallet", "OR"))
        self.label_3.setText(_translate("MiningWallet", "Enter Wallet Number:"))
        self.add_wallet_pb.setText(_translate("MiningWallet", "Add Wallet"))
        self.label_4.setText(_translate("MiningWallet", "<html><head/><body><p><span style=\" color:#ffffff;\">If you already have a wallet for the selected currency, enter it below. Note that if you enter an incorrect wallet number you may not receive funds.</span></p></body></html>"))
        self.miningwallet_back.setText(_translate("MiningWallet", "Back"))
        self.label_5.setText(_translate("MiningWallet", "<html><head/><body><p><span style=\" color:#ffffff;\">We use external wallet software.Therfore you might have to install and run the software and then manually enter the Wallet number in the box bellow.</span></p></body></html>"))

import ChooseCurrency_rc
