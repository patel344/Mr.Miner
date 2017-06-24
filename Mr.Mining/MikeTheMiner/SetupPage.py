# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 440, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.nvidia_rb = QtWidgets.QRadioButton(Form)
        self.nvidia_rb.setGeometry(QtCore.QRect(100, 160, 102, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nvidia_rb.setFont(font)
        self.nvidia_rb.setObjectName("nvidia_rb")
        self.amd_rb = QtWidgets.QRadioButton(Form)
        self.amd_rb.setGeometry(QtCore.QRect(100, 200, 102, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.amd_rb.setFont(font)
        self.amd_rb.setObjectName("amd_rb")
        self.gpu_reqs = QtWidgets.QLabel(Form)
        self.gpu_reqs.setGeometry(QtCore.QRect(110, 240, 421, 61))
        self.gpu_reqs.setText("")
        self.gpu_reqs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gpu_reqs.setWordWrap(True)
        self.gpu_reqs.setObjectName("gpu_reqs")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(70, 380, 341, 31))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_rigName = QtWidgets.QLineEdit(Form)
        self.lineEdit_rigName.setGeometry(QtCore.QRect(70, 510, 341, 31))
        self.lineEdit_rigName.setObjectName("lineEdit_rigName")
        self.setup_next_pb = QtWidgets.QPushButton(Form)
        self.setup_next_pb.setGeometry(QtCore.QRect(462, 551, 121, 41))
        self.setup_next_pb.setObjectName("setup_next_pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Setup Your Account"))
        self.label_2.setText(_translate("Form", "Select Graphic Card:"))
        self.label_3.setText(_translate("Form", "Enter Email:"))
        self.label_4.setText(_translate("Form", "Name Your Mining Rig:"))
        self.nvidia_rb.setText(_translate("Form", "NVIDIA"))
        self.amd_rb.setText(_translate("Form", "AMD"))
        self.setup_next_pb.setText(_translate("Form", "Continue"))

