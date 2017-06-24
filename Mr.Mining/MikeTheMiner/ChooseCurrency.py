# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseCurrency.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setStyleSheet("background-color: rgb(33, 33, 33)")
        self.ethereum = QtWidgets.QPushButton(Form)
        self.ethereum.setGeometry(QtCore.QRect(70, 170, 90, 90))
        self.ethereum.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ChooseCurrency/eth-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ethereum.setIcon(icon)
        self.ethereum.setIconSize(QtCore.QSize(90, 80))
        self.ethereum.setObjectName("ethereum")
        self.ethereum_classic = QtWidgets.QPushButton(Form)
        self.ethereum_classic.setGeometry(QtCore.QRect(260, 170, 90, 90))
        self.ethereum_classic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ChooseCurrency/etc-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ethereum_classic.setIcon(icon1)
        self.ethereum_classic.setIconSize(QtCore.QSize(90, 80))
        self.ethereum_classic.setObjectName("ethereum_classic")
        self.zcash = QtWidgets.QPushButton(Form)
        self.zcash.setGeometry(QtCore.QRect(430, 170, 90, 90))
        self.zcash.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ChooseCurrency/zec-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zcash.setIcon(icon2)
        self.zcash.setIconSize(QtCore.QSize(90, 80))
        self.zcash.setObjectName("zcash")
        self.pascal = QtWidgets.QPushButton(Form)
        self.pascal.setGeometry(QtCore.QRect(70, 310, 90, 90))
        self.pascal.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ChooseCurrency/pasc-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pascal.setIcon(icon3)
        self.pascal.setIconSize(QtCore.QSize(90, 80))
        self.pascal.setObjectName("pascal")
        self.sia = QtWidgets.QPushButton(Form)
        self.sia.setGeometry(QtCore.QRect(260, 310, 90, 90))
        self.sia.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ChooseCurrency/sia-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sia.setIcon(icon4)
        self.sia.setIconSize(QtCore.QSize(90, 80))
        self.sia.setObjectName("sia")
        self.monero = QtWidgets.QPushButton(Form)
        self.monero.setGeometry(QtCore.QRect(430, 310, 90, 90))
        self.monero.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ChooseCurrency/xmr-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.monero.setIcon(icon5)
        self.monero.setIconSize(QtCore.QSize(90, 80))
        self.monero.setObjectName("monero")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 50, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Choose Cryptocurrency To Mine</span></p></body></html>"))

import ChooseCurrency_rc
