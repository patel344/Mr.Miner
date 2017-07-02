# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupPage(object):
    def setupUi(self, SetupPage):
        SetupPage.setObjectName("SetupPage")
        SetupPage.resize(600, 600)
        SetupPage.setStyleSheet("background-color:rgb(33, 33, 33)")
        self.label = QtWidgets.QLabel(SetupPage)
        self.label.setGeometry(QtCore.QRect(70, 40, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SetupPage)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SetupPage)
        self.label_3.setGeometry(QtCore.QRect(70, 380, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SetupPage)
        self.label_4.setGeometry(QtCore.QRect(70, 470, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_4.setObjectName("label_4")
        self.nvidia_rb = QtWidgets.QRadioButton(SetupPage)
        self.nvidia_rb.setGeometry(QtCore.QRect(100, 160, 102, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nvidia_rb.setFont(font)
        self.nvidia_rb.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.nvidia_rb.setObjectName("nvidia_rb")
        self.amd_rb = QtWidgets.QRadioButton(SetupPage)
        self.amd_rb.setGeometry(QtCore.QRect(100, 200, 102, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.amd_rb.setFont(font)
        self.amd_rb.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.amd_rb.setObjectName("amd_rb")
        self.gpu_reqs = QtWidgets.QLabel(SetupPage)
        self.gpu_reqs.setGeometry(QtCore.QRect(110, 240, 421, 61))
        self.gpu_reqs.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.gpu_reqs.setText("")
        self.gpu_reqs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gpu_reqs.setWordWrap(True)
        self.gpu_reqs.setObjectName("gpu_reqs")
        self.lineEdit_email = QtWidgets.QLineEdit(SetupPage)
        self.lineEdit_email.setGeometry(QtCore.QRect(70, 430, 341, 31))
        self.lineEdit_email.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_rigName = QtWidgets.QLineEdit(SetupPage)
        self.lineEdit_rigName.setGeometry(QtCore.QRect(70, 510, 341, 31))
        self.lineEdit_rigName.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lineEdit_rigName.setObjectName("lineEdit_rigName")
        self.setup_next_pb = QtWidgets.QPushButton(SetupPage)
        self.setup_next_pb.setGeometry(QtCore.QRect(462, 551, 121, 41))
        self.setup_next_pb.setStyleSheet("background-color:rgb(39, 255, 36);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.setup_next_pb.setObjectName("setup_next_pb")
        self.label_5 = QtWidgets.QLabel(SetupPage)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_no_gpus = QtWidgets.QLineEdit(SetupPage)
        self.lineEdit_no_gpus.setGeometry(QtCore.QRect(70, 350, 41, 31))
        self.lineEdit_no_gpus.setStyleSheet("\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lineEdit_no_gpus.setObjectName("lineEdit_no_gpus")

        self.retranslateUi(SetupPage)
        QtCore.QMetaObject.connectSlotsByName(SetupPage)

    def retranslateUi(self, SetupPage):
        _translate = QtCore.QCoreApplication.translate
        SetupPage.setWindowTitle(_translate("SetupPage", "Form"))
        self.label.setText(_translate("SetupPage", "<html><head/><body><p><span style=\" color:#ffffff;\">Select Graphic Card:</span></p></body></html>"))
        self.label_2.setText(_translate("SetupPage", "<html><head/><body><p><span style=\" color:#ffffff;\">Select Graphic Card:</span></p></body></html>"))
        self.label_3.setText(_translate("SetupPage", "Enter Email:"))
        self.label_4.setText(_translate("SetupPage", "Name Your Mining Rig:"))
        self.nvidia_rb.setText(_translate("SetupPage", "NVIDIA"))
        self.amd_rb.setText(_translate("SetupPage", "AMD"))
        self.setup_next_pb.setText(_translate("SetupPage", "Continue"))
        self.label_5.setText(_translate("SetupPage", "Number Of GPUs Installed:"))

