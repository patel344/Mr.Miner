from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, os
import time
import subprocess
import pexpect

from MainPage import Ui_MainPage
from SetupPage import Ui_SetupPage
from CreateNewWallet import Ui_CreateNewWallet
from ChooseCurrency import Ui_ChooseCurrency
from MiningWallet import Ui_MiningWallet
from NowMining import Ui_NowMining
from AccountInfo import Ui_AccountInfo

global email
global rig_name
global num_gpus
global graphic_card
global settings_exist
global currency_caller # Used to see which currency led to the mining wallet page

class MainPage(QWidget, Ui_MainPage):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #time.sleep(30)
        #self.close()
        self.showSplash()
        #self.close()

    def showSplash(self):
        #time.sleep(15)
        global setuppage
        setuppage = SetupPage()
        setuppage.show()
        self.close()

class SetupPage(QDialog, Ui_SetupPage):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()

    def Establish_Connections(self):
        self.setup_next_pb.clicked.connect(self.handle_button)
        self.nvidia_rb.toggled.connect(self.nvidia_chosen)
        self.amd_rb.toggled.connect(self.amd_chosen)
        self.setup_next_pb.clicked.connect(self.save_options)

    def handle_button(self):
        global choosecurrency
        global email
        global rig_name
        global num_gpus

        # Check if email is valid
        email = self.lineEdit_email.text()
        rig_name = self.lineEdit_rigName.text()
        num_gpus = self.lineEdit_no_gpus.text()

        # Going To Next Stage
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

    def nvidia_chosen(self):
        global graphic_card
        graphic_card = 'nvidia'
        self.gpu_reqs.setText('NVIDIA REQS')

    def amd_chosen(self):
        global graphic_card
        graphic_card = 'amd'
        self.gpu_reqs.setText('AMD REQS')

    def save_options(self):
        with open('Mining_Settings.txt', 'a') as f:
            f.write(graphic_card)
            f.write('\n')
            f.write(num_gpus)
            f.write('\n')
            f.write(email)
            f.write('\n')
            f.write(rig_name)

class CreateNewWallet(QDialog, Ui_CreateNewWallet):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()

    def Establish_Connections(self):
        self.newWallet_continue.clicked.connect(self.handle_next)

    def handle_next(self):
        global accountinfo
        global account
        global currency_caller

        if self.lineEdit_password.text() == self.lineEdit_passwordconfirm.text():
            password = self.lineEdit_password.text()
            if currency_caller == 'Ethereum':
                child = pexpect.spawn('geth account new')
                child.delaybeforesend = None
                child.expect('.*')
                child.sendline(self.lineEdit_password.text())
                child.expect('.*')
                child.sendline(self.lineEdit_password.text())
                child.expect(pexpect.EOF, timeout=None)
                cmd_show_data = child.before
                cmd_output = cmd_show_data.decode('utf-8').split()
                account = cmd_output[-1][1:-1]

                with open('Ethereum_Settings.txt', 'w') as f:
                    f.write(account)
            elif currency_caller == 'Ethereum_Classic':
                with open('EthereumClassic_Settings.txt', 'w') as f:
                    f.write('Write generated address here.')
            elif currency_caller == 'ZCash':
                with open('Zcash_Settings.txt', 'w') as f:
                    f.write('Write generated address here.')
            elif currency_caller == 'Sia':
                with open('Sia_Settings.txt', 'w') as f:
                    f.write('Write generated address here.')
            elif currency_caller == 'Pascal':
                with open('Pascal_Settings.txt', 'w') as f:
                    f.write('Write generated address here.')
            elif currency_caller == 'Monero':
                with open('Monero_Settings.txt', 'w') as f:
                    f.write('Write generated address here.')
            accountinfo = AccountInfo()
            accountinfo.show()
            self.close()

class ChooseCurrency(QDialog, Ui_ChooseCurrency):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()

    def Establish_Connections(self):
        self.ethereum.clicked.connect(self.handle_currency)
        self.ethereum_classic.clicked.connect(self.handle_currency)
        self.zcash.clicked.connect(self.handle_currency)
        self.sia.clicked.connect(self.handle_currency)
        self.monero.clicked.connect(self.handle_currency)
        self.pascal.clicked.connect(self.handle_currency)

    def handle_currency(self):
        global nowmining
        global miningwallet
        global currency_caller
        if self.sender() == self.ethereum:
            if os.path.isfile('Ethereum_Settings.txt'):
                with open('Ethereum_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                currency_caller = 'Ethereum'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Ethereum'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.ethereum_classic:
            if os.path.isfile('EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'Ethereum_Classic'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Ethereum_Classic'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.zcash:
            if os.path.isfile('ZCash_Settings.txt'):
                with open('ZCash_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'ZCash'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'ZCash'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.pascal:
            if os.path.isfile('Pascal_Settings.txt'):
                with open('Pascal_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'Pascal'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Pascal'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.sia:
            if os.path.isfile('Sia_Settings.txt'):
                with open('Sia_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'Sia'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Sia'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.monero:
            if os.path.isfile('Monero_Settings.txt'):
                with open('Monero_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'Monero'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Monero'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()

class AccountInfo(QDialog, Ui_AccountInfo):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()
        self.fill_info()

    def fill_info(self):
        global account
        #global currency_caller
        self.address_label.setText(account)
        self.urlprogress_label.setText('www.nanopool.com/0x'+account)
        self.filepath_label.setText(currency_caller+'_Settings.txt')

    def Establish_Connections(self):
        self.accntinfo_continue.clicked.connect(self.next_pressed)
        self.accntinfo_back.clicked.connect(self.back_pressed)

    def next_pressed(self):
        global nowmining
        nowmining = NowMining()
        nowmining.show()
        self.close()

    def back_pressed(self):
        global setuppage
        setuppage = SetupPage()
        setuppage.show()

class MiningWallet(QDialog, Ui_MiningWallet):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()

    def Establish_Connections(self):
        self.create_wallet_pb.clicked.connect(self.create_new_wallet)
        self.add_wallet_pb.clicked.connect(self.add_wallet)
        self.miningwallet_back.clicked.connect(self.back_clicked)

    def create_new_wallet(self):
        global createnewwallet
        createnewwallet = CreateNewWallet()
        createnewwallet.show()
        self.close()

    def add_wallet(self):
        self.entered_wallet_no = self.lineEdit_wallet_no.text()
        if currency_caller == 'Ethereum':
            with open('Ethereum_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Ethereum_Classic':
            with open('EthereumClassic_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'ZCash':
            with open('Zcash_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Sia':
            with open('Sia_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Pascal':
            with open('Pascal_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Monero':
            with open('Monero_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        #global nowmining
        nowmining = NowMining()
        nowmining.show()
        self.close()

    def back_clicked(self):
        #global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

class NowMining(QDialog, Ui_NowMining):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.start_mining()
        self.Establish_Connections()

    def start_mining(self):
        global account
        global rig_name
        global email

        if os.path.exists('Ethereum_Settings.txt'):
            with open('Ethereum_Settings.txt') as f:
                account = f.readlines()[0]

        subprocess.call("setx GPU_FORCE_64BIT_PTR 0", shell=True)
        subprocess.call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
        subprocess.call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
        subprocess.call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
        subprocess.call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)
        subprocess.call("echo http://eth-eu1.nanopool.org:8888/0x" + account + "/" + rig_name + "/" + email + " -I",
             shell=True)

    def Establish_Connections(self):
        global currency_caller
        self.coinName_label.setText(currency_caller)
        self.address_label.setText('0x'+account)
        self.stop_pb.clicked.connect(self.stop)
        self.startOver_pb.clicked.connect(self.startOver)
        self.Mining_back.clicked.connect(self.back_pressed)

    def stop(self):
        "Quit mining application"
        global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

    def startOver(self):
        "Restarts Mining of Same currency"

    def back_pressed(self):
        "Settings Page"

def load_info():
    global email
    global rig_name
    global num_gpus
    global graphic_card
    global settings_exist

    settings_exist = False

    if os.path.isfile('Mining_Settings.txt'):
        with open('Mining_Settings.txt', 'r') as f:
            settings = f.readlines()
        """
            settings format:

                Line 0: Graphic Card
                Line 1: Number of GPUs
                Line 2: Email
                Line 3: Mining Rig Name
        """
        if len(settings) == 4:
            settings_exist = True
            graphic_card, num_gpus, email, rig_name = settings[0], settings[1], settings[2], settings[3]

            return True
    return False

def main():
    app = QApplication(sys.argv)

    """# Create and display the splash screen
    splash_pix = QPixmap('MinerLogog.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(3)


    global mainpage
    mainpage = MainPage()
    mainpage.show()
    app.exec()
    """

    # If setup info has already been entered go directly to currency page
    if load_info():
        global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
    else:
        global setuppage
        setuppage = SetupPage()
        setuppage.show()
    app.exec()
if __name__ == '__main__':
    main()