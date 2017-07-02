from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class SetupPage(QWidget):
    def __init__(self, parent = None):
        loadUi("SetupPage.ui", self)
        self.setup_next_pb(self.)
