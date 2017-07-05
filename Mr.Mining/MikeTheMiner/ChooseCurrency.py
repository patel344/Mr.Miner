# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseCurrency.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChooseCurrency(object):
    def setupUi(self, ChooseCurrency):
        ChooseCurrency.setObjectName("ChooseCurrency")
        ChooseCurrency.resize(600, 591)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        ChooseCurrency.setFont(font)
        ChooseCurrency.setStyleSheet("background-color: rgb(33, 33, 33)")
        self.ethereum = QtWidgets.QPushButton(ChooseCurrency)
        self.ethereum.setGeometry(QtCore.QRect(76, 230, 90, 90))
        self.ethereum.setStyleSheet("background-color:rgb(105, 105, 105);\n"
"\n"
"")
        self.ethereum.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ChooseCurrency/eth-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ethereum.setIcon(icon)
        self.ethereum.setIconSize(QtCore.QSize(90, 80))
        self.ethereum.setObjectName("ethereum")
        self.ethereum_classic = QtWidgets.QPushButton(ChooseCurrency)
        self.ethereum_classic.setGeometry(QtCore.QRect(257, 230, 90, 90))
        self.ethereum_classic.setStyleSheet("background-color:rgb(105, 105, 105);")
        self.ethereum_classic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ChooseCurrency/etc-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ethereum_classic.setIcon(icon1)
        self.ethereum_classic.setIconSize(QtCore.QSize(90, 80))
        self.ethereum_classic.setObjectName("ethereum_classic")
        self.zcash = QtWidgets.QPushButton(ChooseCurrency)
        self.zcash.setGeometry(QtCore.QRect(436, 230, 90, 90))
        self.zcash.setStyleSheet("background-color:rgb(105, 105, 105);")
        self.zcash.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ChooseCurrency/zec-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zcash.setIcon(icon2)
        self.zcash.setIconSize(QtCore.QSize(90, 80))
        self.zcash.setObjectName("zcash")
        self.pascal = QtWidgets.QPushButton(ChooseCurrency)
        self.pascal.setEnabled(False)
        self.pascal.setGeometry(QtCore.QRect(76, 370, 90, 90))
        self.pascal.setStyleSheet("background-color:rgb(105, 105, 105);")
        self.pascal.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ChooseCurrency/xmr-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pascal.setIcon(icon3)
        self.pascal.setIconSize(QtCore.QSize(90, 80))
        self.pascal.setObjectName("pascal")
        self.sia = QtWidgets.QPushButton(ChooseCurrency)
        self.sia.setGeometry(QtCore.QRect(257, 370, 90, 90))
        self.sia.setStyleSheet("background-color:rgb(105, 105, 105);")
        self.sia.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ChooseCurrency/sia-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sia.setIcon(icon4)
        self.sia.setIconSize(QtCore.QSize(90, 80))
        self.sia.setObjectName("sia")
        self.monero = QtWidgets.QPushButton(ChooseCurrency)
        self.monero.setEnabled(False)
        self.monero.setGeometry(QtCore.QRect(436, 370, 90, 90))
        self.monero.setStyleSheet("background-color:rgb(105, 105, 105);")
        self.monero.setText("")
        self.monero.setIcon(icon3)
        self.monero.setIconSize(QtCore.QSize(90, 80))
        self.monero.setObjectName("monero")
        self.label_2 = QtWidgets.QLabel(ChooseCurrency)
        self.label_2.setGeometry(QtCore.QRect(92, 330, 61, 16))
        self.label_2.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ChooseCurrency)
        self.label_3.setGeometry(QtCore.QRect(248, 330, 111, 16))
        self.label_3.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ChooseCurrency)
        self.label_4.setGeometry(QtCore.QRect(464, 330, 41, 16))
        self.label_4.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ChooseCurrency)
        self.label_5.setGeometry(QtCore.QRect(90, 470, 61, 20))
        self.label_5.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ChooseCurrency)
        self.label_6.setGeometry(QtCore.QRect(292, 470, 21, 16))
        self.label_6.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ChooseCurrency)
        self.label_7.setGeometry(QtCore.QRect(450, 470, 61, 16))
        self.label_7.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(ChooseCurrency)
        self.label.setGeometry(QtCore.QRect(40, 90, 518, 78))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Mining_back = QtWidgets.QPushButton(ChooseCurrency)
        self.Mining_back.setGeometry(QtCore.QRect(13, 20, 113, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mining_back.sizePolicy().hasHeightForWidth())
        self.Mining_back.setSizePolicy(sizePolicy)
        self.Mining_back.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.Mining_back.setObjectName("Mining_back")
        self.igalmelapela = QtWidgets.QPushButton(ChooseCurrency)
        self.igalmelapela.setEnabled(True)
        self.igalmelapela.setGeometry(QtCore.QRect(540, 10, 51, 61))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ChooseCurrency/Logo_green-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.igalmelapela.setIcon(icon5)
        self.igalmelapela.setIconSize(QtCore.QSize(60, 60))
        self.igalmelapela.setFlat(True)
        self.igalmelapela.setObjectName("igalmelapela")
        self.label_8 = QtWidgets.QLabel(ChooseCurrency)
        self.label_8.setGeometry(QtCore.QRect(450, 410, 61, 20))
        self.label_8.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(ChooseCurrency)
        self.label_9.setGeometry(QtCore.QRect(90, 410, 61, 20))
        self.label_9.setStyleSheet("color:rgb(0, 255, 0)")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(ChooseCurrency)
        QtCore.QMetaObject.connectSlotsByName(ChooseCurrency)

    def retranslateUi(self, ChooseCurrency):
        _translate = QtCore.QCoreApplication.translate
        ChooseCurrency.setWindowTitle(_translate("ChooseCurrency", "Mr.Miner"))
        self.label_2.setText(_translate("ChooseCurrency", "Ethereum"))
        self.label_3.setText(_translate("ChooseCurrency", "Ethereum Classic"))
        self.label_4.setText(_translate("ChooseCurrency", "Zcash"))
        self.label_5.setText(_translate("ChooseCurrency", "Monero CPU"))
        self.label_6.setText(_translate("ChooseCurrency", "Sia"))
        self.label_7.setText(_translate("ChooseCurrency", "Monero GPU"))
        self.label.setText(_translate("ChooseCurrency", "<html><head/><body><p><span style=\" color:#ffffff;\">Choose Cryptocurrency To Mine</span></p></body></html>"))
        self.Mining_back.setText(_translate("ChooseCurrency", "Settings"))
        self.label_8.setText(_translate("ChooseCurrency", "Coming soon"))
        self.label_9.setText(_translate("ChooseCurrency", "Coming soon"))

import ChooseCurrency_rc
