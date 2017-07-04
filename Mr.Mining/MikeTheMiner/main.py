from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from subprocess import Popen, PIPE, STDOUT
import sys, os
import time
import subprocess
import pexpect
from pexpect import popen_spawn

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
        if self.nvidia_rb.isChecked() or self.amd_rb.isChecked():
            with open('Mining_Settings.txt', 'a') as f:
                f.write(graphic_card)
                f.write('\n')
                f.write(num_gpus)
                f.write('\n')
                f.write(email)
                f.write('\n')
                f.write(rig_name)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select the graphic card you are using.")
            msg.setWindowTitle("Mr.Miner Missing Information")
            msg.setStandardButtons(QMessageBox.Ok)

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
        if len(self.lineEdit_password.text()) >= 8:
            if self.lineEdit_password.text() == self.lineEdit_passwordconfirm.text():
                password = self.lineEdit_password.text()
                if currency_caller == 'Ethereum':
                    child = pexpect.popen_spawn.PopenSpawn('geth account new')
                    child.delaybeforesend = None
                    child.expect('.*')
                    child.sendline(self.lineEdit_password.text())
                    child.expect('.*')
                    child.sendline(self.lineEdit_password.text())
                    child.expect(pexpect.EOF, timeout=None)
                    cmd_show_data = child.before
                    cmd_output = cmd_show_data.decode('utf-8').split()
                    account = cmd_output[-1][1:-1]
                    with open('Ethereum_Wallet/Ethereum_Settings.txt', 'w') as f:
                        f.write(account)

                elif currency_caller == 'Ethereum_Classic':
                    child = pexpect.popen_spawn.PopenSpawn('geth account new')
                    child.delaybeforesend = None
                    child.expect('.*')
                    child.sendline(self.lineEdit_password.text())
                    child.expect('.*')
                    child.sendline(self.lineEdit_password.text())
                    child.expect(pexpect.EOF, timeout=None)
                    cmd_show_data = child.before
                    cmd_output = cmd_show_data.decode('utf-8').split()
                    account = cmd_output[-1][1:-1]
                    with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt', 'w') as f:
                        f.write(account)

                elif currency_caller == 'Zcash':
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
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Passwords do not match.")
                msg.setWindowTitle("Mr.Miner Error Occurred")
                msg.setStandardButtons(QMessageBox.Ok)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Password must be at least 8 Characters.")
            msg.InformativeText("Having a strong password is integral to maintaining your wallet's security.")
            msg.setWindowTitle("Mr.Miner Error Occurred")
            msg.setStandardButtons(QMessageBox.Ok)

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
        global account
        if self.sender() == self.ethereum:
            if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
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
            if os.path.isfile('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt', 'r') as f:
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
            if os.path.isfile('Zcash_Wallet/Zcash_Settings.txt'):
                with open('Zcash_Wallet/Zcash_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'Zcash'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'Zcash'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
        elif self.sender() == self.pascal:
            if os.path.isfile('Pascal_Wallet/Pascal_Settings.txt'):
                with open('Pascal_Wallet/Pascal_Settings.txt', 'r') as f:
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
            if os.path.isfile('Sia_Wallet/Sia_Settings.txt'):
                with open('Sia_Wallet/Sia_Settings.txt', 'r') as f:
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
            if os.path.isfile('Monero_Wallet/Monero_Settings.txt'):
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
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
        ##add calling other programs for other wallets
        global createnewwallet
        createnewwallet = CreateNewWallet()
        createnewwallet.show()
        self.close()

    def add_wallet(self):
        self.entered_wallet_no = self.lineEdit_wallet_no.text()
        if len(self.entered_wallet_no) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("It seems like you haven't entered in a wallet number.")
            msg.setInformativeText("Please enter valid wallet number or create a new one.")
            msg.setWindowTitle("Mr.Miner Missing Information")
            msg.setStandardButtons(QMessageBox.Ok)

        if currency_caller == 'Ethereum':
            with open('Ethereum_Wallet/Ethereum_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Ethereum_Classic':
            with open('Ethereum_Wallet/EthereumClassic_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Zcash':
            with open('Zcash_Wallet/Zcash_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
                f.close()
        elif currency_caller == 'Sia':
            with open('Sia_Wallet/Sia_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Pascal':
            with open('Pascal_Wallet/Pascal_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'Monero':
            with open('Monero_Wallet/Monero_Settings.txt', 'w') as f:
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
        global currency_caller

        if currency_caller == 'Ethereum':
            if os.path.exists('Ethereum_Wallet/Ethereum_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt') as f:
                    account = f.readlines()[0]
            with open('Santas_helpers\etherum_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                batman.write("Santas_helpers\ethminer.exe -I -F http://eth-eu1.nanopool.org:8888/0x" + account + "/" + rig_name + "/" + email)
            subprocess.Popen("Santas_helpers\etherum_Start.bat", shell=True)
            #batman.close()
            #subprocess.call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
            #subprocess.call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
            #subprocess.call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
            #subprocess.call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)

            #output, stderr = subprocess.Popen("Santas_helpers\ethminer.exe -I -F http://eth-eu1.nanopool.org:8888/0x" + account + "/" + rig_name + "/" + email ,
             #    shell=True).communicate()
            #subprocess.call("Santas_helpers\ethminer.exe -I -F http://eth-eu1.nanopool.org:8888/0x" + account + "/" + rig_name + "/" + email ,
             #    shell=True)
        elif currency_caller == 'Ethereum_Classic':
            if os.path.exists('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt') as f:
                    account = f.readlines()[0]
            subprocess.call("setx GPU_FORCE_64BIT_PTR 0", shell=True)
            subprocess.call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
            subprocess.call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
            subprocess.call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
            subprocess.call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)
            subprocess.call("Santas_helpers\ethminer.exe --farm-recheck 200 -I -S etc-eu1.nanopool.org:19999 -O 0x" + account + "." + rig_name + "/" + email,
                            shell=True)
        elif currency_caller == 'Zcash':
            if os.path.exists('Zcash_Wallet/Zcash_Settings.txt'):
                with open('Zcash_Wallet/Zcash_Settings.txt') as f:
                    account = f.readlines()[0]
        elif currency_caller == 'Sia':
            if os.path.exists('Sia_Wallet/Sia_Settings.txt'):
                with open('Sia_Wallet/Sia_Settings.txt') as f:
                    account = f.readlines()[0]
        elif currency_caller == 'Pascal':
            if os.path.exists('Pascal_Wallet/Pascal_Settings.txt'):
                with open('Pascal_Wallet/Pascal_Settings.txt') as f:
                    account = f.readlines()[0]
        elif currency_caller == 'Monero':
            if os.path.exists('Monero_Wallet/Monero_Settings.txt'):
                with open('Monero_Wallet/Monero_Settings.txt') as f:
                    account = f.readlines()[0]
    def Establish_Connections(self):
        global currency_caller
        self.coinName_label.setText(currency_caller)
        self.address_label.setText('0x'+account)
        self.stop_pb.clicked.connect(self.stop)
        self.startOver_pb.clicked.connect(self.startOver)
        self.Mining_back.clicked.connect(self.back_pressed)
        self.auto_cb.stateChanged.connect(self.auto_mine)
        self.coinName_cb.setText(currency_caller)

    def auto_mine(self):
        if self.auto_cb.isChecked():
            with open('AutoMine_Settings.txt', 'w') as f:
                f.write(currency_caller)
        else:
            if os.path.exists('AutoMine_Settings.txt'):
                os.remove('AutoMine_Settings.txt')

    def stop(self):
        "Quit mining application"
        if currency_caller == 'Ethereum':
            os.system("taskkill /f /im  ethminer.exe")
        global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

    def startOver(self):
        if currency_caller == 'Ethereum':
            if os.path.exists('Ethereum_Wallet/Ethereum_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt') as f:
                    account = f.readlines()[0]

                subprocess.call("setx GPU_FORCE_64BIT_PTR 0", shell=True)
                subprocess.call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
                subprocess.call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
                subprocess.call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
                subprocess.call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)
                subprocess.call("echo ethminer.exe -F http://eth-eu1.nanopool.org:8888/0x" + account + "/" + rig_name + "/" + email + " -I",
                 shell=True)

        elif currency_caller == 'Ethereum_Classic':
            if os.path.exists('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt') as f:
                    account = f.readlines()[0]

                subprocess.call("setx GPU_FORCE_64BIT_PTR 0", shell=True)
                subprocess.call("setx GPU_MAX_HEAP_SIZE 100", shell=True)
                subprocess.call("setx GPU_USE_SYNC_OBJECTS 1", shell=True)
                subprocess.call("setx GPU_SINGLE_ALLOC_PERCENT 100", shell=True)
                subprocess.call("setx GPU_MAX_ALLOC_PERCENT 100", shell=True)
                subprocess.call("ethminer.exe --farm-recheck 200 -I -S etc-eu1.nanopool.org:19999 -O 0x" + account + "." + rig_name + "/" + email,
                            shell=True)


    def back_pressed(self):
        global setuppage
        setuppage = SetupPage()
        setuppage.show()

def load_info():
    global email
    global rig_name
    global num_gpus
    global graphic_card
    global settings_exist
    global currency_caller
    global automine_bool

    automine_bool = False
    settings_exist = False

    if not os.path.exists('Ethereum_Wallet'):
        os.makedirs('Ethereum_Wallet')
    if not os.path.exists('EthereumClassic_Wallet'):
        os.makedirs('EthereumClassic_Wallet')
    if not os.path.exists('Pascal_Wallet'):
        os.makedirs('Pascal_Wallet')
    if not os.path.exists('Sia_Wallet'):
        os.makedirs('Sia_Wallet')
    if not os.path.exists('Monero_Wallet'):
        os.makedirs('Monero_Wallet')
    if not os.path.exists('Zcash_Wallet'):
        os.makedirs('Zcash_Wallet')

    if os.path.isfile('AutoMine_Settings.txt'):
        with open('AutoMine_Settings.txt') as f:
            currency_caller = f.readlines()[0]
        automine_bool = True

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
        if automine_bool:
            global nowmining
            nowmining = NowMining()
            nowmining.auto_cb.setChecked(True)
            nowmining.show()
        else:
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