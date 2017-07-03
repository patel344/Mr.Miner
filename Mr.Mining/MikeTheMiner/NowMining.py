# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NowMining.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NowMining(object):
    def setupUi(self, NowMining):
        NowMining.setObjectName("NowMining")
        NowMining.resize(600, 600)
        NowMining.setStyleSheet("background-color:rgb(33, 33, 33);\n"
"\n"
"")
        self.hashrate_label = QtWidgets.QLabel(NowMining)
        self.hashrate_label.setGeometry(QtCore.QRect(220, 180, 301, 24))
        self.hashrate_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.hashrate_label.setObjectName("hashrate_label")
        self.filepath_label = QtWidgets.QLabel(NowMining)
        self.filepath_label.setGeometry(QtCore.QRect(50, 400, 461, 31))
        self.filepath_label.setText("")
        self.filepath_label.setObjectName("filepath_label")
        self.label = QtWidgets.QLabel(NowMining)
        self.label.setGeometry(QtCore.QRect(150, 50, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(NowMining)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(NowMining)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.address_label = QtWidgets.QLabel(NowMining)
        self.address_label.setGeometry(QtCore.QRect(120, 110, 461, 25))
        self.address_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.address_label.setText("")
        self.address_label.setObjectName("address_label")
        self.Mining_back = QtWidgets.QPushButton(NowMining)
        self.Mining_back.setGeometry(QtCore.QRect(10, 10, 113, 41))
        self.Mining_back.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.Mining_back.setObjectName("Mining_back")
        self.label_3 = QtWidgets.QLabel(NowMining)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.coinName_label = QtWidgets.QLabel(NowMining)
        self.coinName_label.setGeometry(QtCore.QRect(270, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.coinName_label.setFont(font)
        self.coinName_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.coinName_label.setText("")
        self.coinName_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.coinName_label.setObjectName("coinName_label")
        self.estCoin_label = QtWidgets.QLabel(NowMining)
        self.estCoin_label.setGeometry(QtCore.QRect(220, 240, 301, 24))
        self.estCoin_label.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.estCoin_label.setObjectName("estCoin_label")
        self.stop_pb = QtWidgets.QPushButton(NowMining)
        self.stop_pb.setGeometry(QtCore.QRect(100, 340, 171, 61))
        self.stop_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.stop_pb.setObjectName("stop_pb")
        self.startOver_pb = QtWidgets.QPushButton(NowMining)
        self.startOver_pb.setGeometry(QtCore.QRect(320, 340, 171, 61))
        self.startOver_pb.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"color:rgb(255, 255, 255)")
        self.startOver_pb.setObjectName("startOver_pb")
        self.auto_cb = QtWidgets.QCheckBox(NowMining)
        self.auto_cb.setGeometry(QtCore.QRect(50, 430, 151, 51))
        self.auto_cb.setStyleSheet("color:rgb(255, 255, 255)\n"
"")
        self.auto_cb.setObjectName("auto_cb")
        self.coinName_cb = QtWidgets.QLabel(NowMining)
        self.coinName_cb.setGeometry(QtCore.QRect(195, 448, 61, 16))
        self.coinName_cb.setObjectName("coinName_cb")
        self.coinName_cb_2 = QtWidgets.QLabel(NowMining)
        self.coinName_cb_2.setGeometry(QtCore.QRect(260, 448, 191, 16))
        self.coinName_cb_2.setObjectName("coinName_cb_2")

        self.retranslateUi(NowMining)
        QtCore.QMetaObject.connectSlotsByName(NowMining)

    def retranslateUi(self, NowMining):
        _translate = QtCore.QCoreApplication.translate
        NowMining.setWindowTitle(_translate("NowMining", "Form"))
        self.hashrate_label.setText(_translate("NowMining", "123"))
        self.label.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">Mining</span></p></body></html>"))
        self.label_4.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">Hash Rate:</span></p></body></html>"))
        self.label_5.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">Estimated Coin:</span></p></body></html>"))
        self.Mining_back.setText(_translate("NowMining", "Settings"))
        self.label_3.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">Address:</span></p></body></html>"))
        self.estCoin_label.setText(_translate("NowMining", "123"))
        self.stop_pb.setText(_translate("NowMining", "Stop Mining"))
        self.startOver_pb.setText(_translate("NowMining", "Start Over"))
        self.auto_cb.setText(_translate("NowMining", "Automatically mine "))
        self.coinName_cb.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">Ethereum</span></p></body></html>"))
        self.coinName_cb_2.setText(_translate("NowMining", "<html><head/><body><p><span style=\" color:#ffffff;\">next time Mr. Miner starts</span></p></body></html>"))

