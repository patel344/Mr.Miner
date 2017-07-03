# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(600, 600)
        MainPage.setAutoFillBackground(False)
        MainPage.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.label = QtWidgets.QLabel(MainPage)
        self.label.setGeometry(QtCore.QRect(190, 150, 211, 271))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainPage)
        self.label_2.setGeometry(QtCore.QRect(110, 420, 381, 121))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:rgb(0, 255, 0)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Mr.Miner"))
        self.label.setText(_translate("MainPage", "<html><head/><body><p><img src=\":/MainPageMining/MinerLogo.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainPage", "<html><head/><body><p><span style=\" color:#00ff00;\">Welcome To Mister Miner! </span></p></body></html>"))

import MainPageMining_rc
