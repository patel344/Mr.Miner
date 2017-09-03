from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *


import json
import sys, os
import logging
from time import sleep
from urllib.request import Request, urlopen
import re
import subprocess
import pexpect
from pexpect import popen_spawn
from subprocess import Popen as popen

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
        self.nvidia_rb.toggled.connect(self.nvidia_chosen)
        self.amd_rb.toggled.connect(self.amd_chosen)
        self.setup_next_pb.clicked.connect(self.save_options)

    def nvidia_chosen(self):
        global graphic_card
        graphic_card = 'nvidia'
        self.gpu_reqs.setText('*Download and Install your GPU Drivers from:\nhttp://www.nvidia.com/Download/index.aspx\n'
                                '*Download and Install CUDA Drivers from: \n'
                                'https://developer.nvidia.com/cuda-downloads\n'
                                '*Download and Install Microsoft Visual Studio redistributable 2015: \n'
                                'https://www.microsoft.com/en-us/download/details.aspx?id=48145\n'
                                '*Download and Install Microsoft Visual Studio redistributable 2013\n'
                                'https://www.microsoft.com/en-us/download/details.aspx?id=40784\n')

    def amd_chosen(self):
        global graphic_card
        graphic_card = 'amd'
        self.gpu_reqs.setText(
            '*Download and Install your GPU Drivers from:\nhttp://support.amd.com/en-us/download\n'
            '*Download and Install OPENCL Drivers from: \n'
            'http://support.amd.com/en-us/kb-articles/Pages/OpenCL2-Driver.aspx\n'
            '*Download and Install Microsoft Visual Studio redistributable 2015: \n'
            'https://www.microsoft.com/en-us/download/details.aspx?id=48145\n'
            '*Download and Install Microsoft Visual Studio redistributable 2013\n'
            'https://www.microsoft.com/en-us/download/details.aspx?id=40784\n')

    def save_options(self):
        global choosecurrency
        global email
        global rig_name
        global num_gpus

        # Check if email is valid
        email = self.lineEdit_email.text()
        rig_name = self.lineEdit_rigName.text()
        num_gpus = self.lineEdit_no_gpus.text()
        print(num_gpus)
        if self.nvidia_rb.isChecked() or self.amd_rb.isChecked():
            try:
                num_gpus = int(num_gpus)
            except ValueError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Number of GPUs input must be an integer value.")
                msg.setWindowTitle("Mr.Miner Incorrect Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

            with open('Mining_Settings.txt', 'w') as f:
                f.write(graphic_card)
                f.write('\n')
                f.write(str(num_gpus))
                f.write('\n')
                f.write(email)
                f.write('\n')
                f.write(rig_name)

            # Going To Next Stage
            choosecurrency = ChooseCurrency()
            choosecurrency.show()
            self.close()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select the graphic card you are using.")
            msg.setWindowTitle("Mr.Miner Missing Information")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

class CreateNewWallet(QDialog, Ui_CreateNewWallet):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()

    def Establish_Connections(self):
        self.newWallet_continue.clicked.connect(self.handle_next)
        self.newWallet_back.clicked.connect(self.handle_back)

    def handle_back(self):
        global miningwallet
        miningwallet = MiningWallet()
        miningwallet.show()
        self.close()

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
                    #open wallet aplication
                    with open('Zcash_Settings.txt', 'w') as f:
                        f.write('Write generated address here.')
                elif currency_caller == 'Sia':
                    with open('Sia_Settings.txt', 'w') as f:
                        f.write('Write generated address here.')
                elif currency_caller == 'Monero':
                    with open('Monero_Settings.txt', 'w') as f:
                        f.write('Write generated address here.')
                elif currency_caller == 'Pascal':
                    with open('Pascal_Settings.txt', 'w') as f:
                        f.write('Pascal address')

                accountinfo = AccountInfo()
                accountinfo.show()
                self.close()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Passwords do not match.")
                msg.setWindowTitle("Mr.Miner Error Occurred")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Password must be at least 8 Characters.")
            msg.setInformativeText("Having a strong password is integral to maintaining your wallet's security.")
            msg.setWindowTitle("Mr.Miner Error Occurred")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

class ChooseCurrency(QDialog, Ui_ChooseCurrency):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Establish_Connections()
        ##add update
        #subprocess.Popen(r"Santas_helpers\update_miner.bat", shell=True)

    def get_balance(self, url, coin_label):
        if coin_label == 'not_xmr':
            #while True:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            info = json.loads(urlopen(req).read().decode('utf-8'))
            if info['status']:
                # print("working")
                # print(int(info['data']))
                #print(round(float(info['data']), 4))
                #print(coin_label)
                return round(float(info['data']), 4)
            else:
                # print('error')
               # print(coin_label)
                logging.error('Nanopool API:' + info['error'])
                return int(0)
                #sleep(30)
        else:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            info = json.loads(urlopen(req).read().decode('utf-8'))
            if not info['error']:
                # print("working")
                # print(int(info['data']))
                return round(float(info['wallet_balance']), 4)
            else:
                # print('error')
                logging.error('Dwarfpool API:' + info['error'])
                return 0
                # sleep(30)

    def check_balance(self, url):
        count = 0
        #while True:
        if self.get_balance(url) == 0:
            count += 1
            logging.warning('Nanopool API: Balance seems to be zero')
        else:
            count = 0

          #  if count == 2:
          #      popen('taskkill /f /im {}'.format('ethminer.exe'))
          #      sleep(10)
          #      self.start_mining()

                # print("hashrate is 0")
                # Restarts the miner
                # popen('ethminer.exe' + ' )

           # sleep(5)

    def scrape_nanopool(self, coin_label, account):
        #print(coin_label)
        #print(account)
        if coin_label == 'xmr':
            return self.get_balance('http://dwarfpool.com/xmr/api?wallet=' + account + '&email=xmr@example.com', 'xmr')
        else:
            #print(coin_label)
            #self.get_balance('https://api.nanopool.org/v1/eth/balance/0x2fc7723d8623eb414abb4fa6d81395d81b87a8f9', 'not_xmr')
            return self.get_balance('https://api.nanopool.org/v1/' + coin_label + '/balance/' + account, 'not_xmr')


    def Establish_Connections(self):
        self.ethereum.clicked.connect(self.handle_currency)
        self.ethereum_classic.clicked.connect(self.handle_currency)
        self.zcash.clicked.connect(self.handle_currency)
        self.sia.clicked.connect(self.handle_currency)
        self.monero.clicked.connect(self.handle_currency)
        self.pascal.clicked.connect(self.handle_currency)
        self.monero_eth_sia.clicked.connect(self.handle_currency)
        self.monero_gpu.clicked.connect(self.handle_currency)
        self.monero_gpu_cpu.clicked.connect(self.handle_currency)
        self.monero_pasc_monero.clicked.connect(self.handle_currency)
        self.monero_zcash.clicked.connect(self.handle_currency)
        self.Mining_back.clicked.connect(self.handle_back)

        if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt'):
            with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_eth = self.scrape_nanopool('eth', account)
            print(balance_eth)
            self.eth_coin.setText(str(balance_eth) + ' eth')

        if os.path.isfile('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
            with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_etc = self.scrape_nanopool('etc', account)
            self.etc_coin.setText(str(balance_etc) + ' etc')

        if os.path.isfile('Zcash_Wallet/Zcash_Settings.txt'):
            with open('Zcash_Wallet/Zcash_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_zec = self.scrape_nanopool('zec', account)
            self.zec_coin.setText(str(balance_zec) + ' zec')

        if os.path.isfile('Sia_Wallet/Sia_Settings.txt'):
            with open('Sia_Wallet/Sia_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_sia = self.scrape_nanopool('sia', account)
            self.sia_coin.setText(str(balance_sia) + ' sia')

        if os.path.isfile('Monero_Wallet/Monero_Settings.txt'):
            with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_xmr = self.scrape_nanopool('xmr', account)
            self.xmr_coin.setText(str(balance_xmr) + ' xmr')

        if os.path.isfile('Pascal_Wallet/Pascal_Settings.txt'):
            with open('Pascal_Wallet/Pascal_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            balance_pasc = self.scrape_nanopool('pasc', account)
            self.pasc_coin.setText(str(balance_pasc) + ' pasc')

    def handle_back(self):
        global setuppage
        setuppage = SetupPage()
        setuppage.show()
        self.close()

    def handle_currency(self):
        global nowmining
        global miningwallet
        global currency_caller
        global account
        global account2
        global account3
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
            if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Sia_Wallet/Sia_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                with open('Sia_Wallet/Sia_Settings.txt', 'r') as f:
                    account2 = f.readlines()[0]
                #global nowmining
                currency_caller = 'ETH-SIA'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Oh no! we couldin't your wallets. please make sure you have a ethereum wallet and SIA wallet with us by clicking on the curency and"
                            "creating a wallet or adding you previously owned wallet")
                msg.setWindowTitle("Mr.Miner Incorrect Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

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

        elif self.sender() == self.monero_gpu:
                if os.path.isfile('Monero_Wallet/Monero_Settings.txt'):
                    with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                        account = f.readlines()[0]
                    # global nowmining
                    currency_caller = 'monero_gpu'
                    nowmining = NowMining()
                    nowmining.show()
                    self.close()
                else:
                    # global currency_caller
                    # global miningwallet
                    currency_caller = 'monero_gpu'
                    miningwallet = MiningWallet()
                    miningwallet.show()
                    self.close()

        elif self.sender() == self.monero_gpu_cpu:
            if os.path.isfile('Monero_Wallet/Monero_Settings.txt'):
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                #global nowmining
                currency_caller = 'monero_gpu_cpu'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                #global currency_caller
                #global miningwallet
                currency_caller = 'monero_gpu_cpu'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()

        elif self.sender() == self.monero_zcash:
            if os.path.isfile('Monero_Wallet/Monero_Settings.txt') and os.path.isfile('Zcash_Wallet/Zcash_Settings.txt'):
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                with open('Zcash_Wallet/Zcash_Settings.txt', 'r') as f:
                    account2 = f.readlines()[0]
                #global nowmining
                currency_caller = 'monero_zcash'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Oh no! we couldin't find your wallets. please make sure you have a monero wallet and zcash wallet with us by clicking on the curency and"
                            "creating a wallet or adding you previously owned wallet")
                msg.setWindowTitle("Mr.Miner Incorrect Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

        elif self.sender() == self.monero_eth_sia:
            if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Monero_Wallet/Monero_Settings.txt') and os.path.isfile('Sia_Wallet/Sia_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                with open('Sia_Wallet/Sia_Settings.txt', 'r') as f:
                    account2 = f.readlines()[0]
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                    account3 = f.readlines()[0]
                #global nowmining
                currency_caller = 'ETH-SIA-monero'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Oh no! we couldn't find your wallets. please make sure you have a ethereum wallet, a Monero wallet and SIA wallet with us by clicking on the curency and"
                            "creating a wallet or adding you previously owned wallet")
                msg.setWindowTitle("Mr.Miner Incorrect Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

        elif self.sender() == self.monero_pasc_monero:
            if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Monero_Wallet/Monero_Settings.txt') and os.path.isfile('Pascal_Wallet/Pascal_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                with open('Pascal_Wallet/Pascal_Settings.txt', 'r') as f:
                    account2 = f.readlines()[0]
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                    account3 = f.readlines()[0]
                #global nowmining
                currency_caller = 'ETH-Pascal-monero'
                nowmining = NowMining()
                nowmining.show()
                self.close()
            elif os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Monero_Wallet/Monero_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                    account = f.readlines()[0]
                with open('Monero_Wallet/Monero_Settings.txt', 'r') as f:
                    account3 = f.readlines()[0]
                currency_caller = 'ETH-Pascal-monero'
                miningwallet = MiningWallet()
                miningwallet.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Oh no! we couldn't find your wallets. please make sure you have a ethereum wallet, and Monero wallet with us by clicking on the curency and"
                            "creating a wallet or adding you previously owned wallet")
                msg.setWindowTitle("Mr.Miner Incorrect Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

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
        #change for other pools
        if currency_caller == 'Sia' and graphic_card == 'nvidia\n' or graphic_card == 'nvidia':
            self.urlprogress_label.setText('https://siamining.com/addresses/' + account)
        elif currency_caller == 'Ethereum':
            self.urlprogress_label.setText('https://eth.nanopool.org/account/0x' + account)
        elif currency_caller == 'Ethereum_Classic':
            self.urlprogress_label.setText('https://etc.nanopool.org/account/0x' + account)
        elif currency_caller == 'Zcash':
            self.urlprogress_label.setText('https://zec.nanopool.org/account/' + account)
        elif currency_caller == 'Monero':
            self.urlprogress_label.setText('http://dwarfpool.com/xmr/address?wallet=' + account)

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
        self.close()

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
        if currency_caller == 'Ethereum_Classic' or currency_caller == 'Ethereum':
            global createnewwallet
            createnewwallet = CreateNewWallet()
            createnewwallet.show()
            self.close()
        elif currency_caller == 'Zcash':
            subprocess.Popen("Santas_helpers\zcash_wallet_creator.bat", shell=True)
        elif currency_caller == 'Sia':
            subprocess.Popen("Santas_helpers\sia_wallet_creator.bat", shell=True)
        #add monoero wallet t
        elif currency_caller == 'Monero':
            subprocess.Popen("Santas_helpers\monero_wallet_creator.bat", shell=True)
        elif currency_caller == 'ETH-Pascal-monero':
            subprocess.Popen("Santas_helpers\Pascal_wallet_creator.bat", shell=True)


    def add_wallet(self):
        self.entered_wallet_no = self.lineEdit_wallet_no.text()
        if len(self.entered_wallet_no) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("It seems like you haven't entered in a wallet number.")
            msg.setInformativeText("Please enter valid wallet number or create a new one.")
            msg.setWindowTitle("Mr.Miner Missing Information")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

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
        elif currency_caller == 'Monero':
            with open('Monero_Wallet/Monero_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)
        elif currency_caller == 'ETH-Pascal-monero':
            with open('Pascal_Wallet/Pascal_Settings.txt', 'w') as f:
                f.write(self.entered_wallet_no)

        global nowmining
        nowmining = NowMining()
        nowmining.show()
        self.close()

    def back_clicked(self):
        global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

class NowMining(QDialog, Ui_NowMining):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.start_mining()
        self.Establish_Connections()
        #self.scrape_nanopool()

    def get_hashrate(self, url):
        while True:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            info = json.loads(urlopen(req).read().decode('utf-8'))
            if info['status']:
                #print("working")
                #print(int(info['data']))
                return int(info['data'])
            else:
                #print('error')
                logging.error('Nanopool API:' + info['error'] + ', trying again in 30 seconds')

                return 0

    def check_hashrate(self, url):
        #count = 0
        #while True:
         #   if self.get_hashrate(url) == 0:
         #       count += 1
         #       logging.warning('Nanopool API: Hashrate seems to be zero')
         #   else:
         #       count = 0
        return self.get_hashrate()
            # Not going to worry about resetting if hashrate is 0
            #if count == 2:
            #    popen('taskkill /f /im {}'.format('ethminer.exe'))
            #    sleep(10)
            #    self.start_mining()

                #print("hashrate is 0")
                # Restarts the miner
                # popen('ethminer.exe' + ' )

            #sleep(5)

    def scrape_nanopool(self, coin_label):
        #print(coin_label)
        #print(account)

        # DISABLING FOR NOW
        #return self.check_hashrate('https://api.nanopool.org/v1/' + coin_label + '/hashrate/' + account)
        return "Coming Soon"

    def configure_monero_AMD(self):
        global num_gpus
        global rig_name
        global account

        with open(r'Santas_helpers/xmr-gpu.conf', 'r') as f:
            config = json.load(f)

        if len(config["Algorithms"][0]["devices"]) > int(num_gpus):
            for i in range(len(config["Algorithms"][0]["devices"]) - int(num_gpus)):
                config["Algorithms"][0]["devices"].pop()

        elif len(config["Algorithms"][0]["devices"]) < int(num_gpus):
            for i in range(num_gpus - len(config["Algorithms"][0]["devices"]), 0, -1):
                gpu = {"index": (num_gpus - i),
                       "corefreq": 500,
                       "memfreq": 1500,
                       "fanspeed": 65,
                       "powertune": 20,
                       "threads": 1,
                       "rawintensity": 640,
                       "worksize": 16
                       }
                config["Algorithms"][0]["devices"].append(gpu)

        config["Algorithms"][0]["name"] = rig_name

        for i in range(5):
            config["Algorithms"][0]["pools"][i]["user"] = account

        with open(r'Santas_helpers\xmr-gpu.conf', 'w') as f:
            json.dump(config, f, indent=4, sort_keys=True)

    # FOR MONERO CPU

    def configure_monero_CPU(self):
        global account
        global rig_name
        global num_threads

        proc = subprocess.Popen('WMIC CPU Get NumberOfCores,NumberOfLogicalProcessors /Format:List',
                                stdout=subprocess.PIPE, shell=True)

        with open(r'Santas_helpers\xmr-cpu.conf', 'r') as f:
            config = json.load(f)

        config["Algorithms"][0]["name"] = rig_name

        for i in range(5):
            config["Algorithms"][0]["pools"][i]["user"] = account

        proc = subprocess.Popen('WMIC CPU Get NumberOfCores,NumberOfLogicalProcessors /Format:List',
                                stdout=subprocess.PIPE, shell=True)

        num_threads = (proc.communicate()[0]).decode('utf-8').split()[-1].strip()
        num_threads = re.search(r"[0-9]+", num_threads).group(0).strip()
        config["Algorithms"][0]["devices"][0]["threads"] = int(num_threads) - 1

        with open(r'Santas_helpers\xmr-cpu.conf', 'w') as f:
            json.dump(config, f, indent=4, sort_keys=True)
    def sia_mine(self):
        if os.path.exists('Sia_Wallet/Sia_Settings.txt'):
            with open('Sia_Wallet/Sia_Settings.txt') as f:
                account = f.readlines()[0]
        with open('Santas_helpers\Sia_Start.bat', 'w')as batman:
            if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                shit_call = "Santas_helpers\ccminer -a sia -e --url=stratum+tcp://us-east.siamining.com:3333 -u " + account.replace(
                    "\n", "") + "." + rig_name.replace("\n", "") + " -i 28 \n"
                batman.write(shit_call)
            elif graphic_card == 'amd\n ' or 'amd' in graphic_card:
                shit_call = 'Santas_helpers\gominer.exe -I 28 -H sia-eu1.nanopool.org:9980 -Q "address=' + account.replace(
                    "\n", "") + '&worker=' + rig_name.replace("\n", "") + '&email=' + email.replace("\n", "") + '" \n'
                batman.write(shit_call)
        subprocess.Popen("Santas_helpers\Sia_Start.bat", shell=True)
    def monero_mine(self):
        if os.path.exists('Monero_Wallet/Monero_Settings.txt'):
            with open('Monero_Wallet/Monero_Settings.txt') as f:
                account = f.readlines()[0]
            with open('Santas_helpers\Monero_Start.bat', 'w')as batman:
                shit_call = r"Santas_helpers\xmrig.exe -o xmr-eu.dwarfpool.com:8005 -u " + account.replace("\n","") + " -p x -k"
                batman.write(shit_call)
                subprocess.Popen("Santas_helpers\Monero_Start.bat", shell=True)
    def monero_GPU_mine(self):
        if os.path.exists('Monero_Wallet/Monero_Settings.txt'):
            with open('Monero_Wallet/Monero_Settings.txt') as f:
                account = f.readlines()[0]
            with open('Santas_helpers\Sia_Start.bat', 'w')as batman:
                if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                    shit_call = r"Santas_helpers\xmrMiner_0.2.1.exe --url=stratum+tcp://xmr-eu.dwarfpool.com:8050 -u " + account.replace(
                        "\n", "") + " -p x  --bfactor=6 --bsleep=25"
                    batman.write(shit_call)
                    subprocess.Popen("Santas_helpers\Sia_Start.bat", shell=True)
                elif graphic_card == 'amd\n ' or 'amd' in graphic_card:
                    shit_call = r'Santas_helpers\NsGpuCNMiner.exe -o stratum+tcp://xmr-eu.dwarfpool.com:8050 -u ' + account.replace(
                        "\n", "") +' -p x'
                    batman.write(shit_call)
                    subprocess.Popen("Santas_helpers\Sia_Start.bat", shell=True)
    def eth_sia_mine(self):
        if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Sia_Wallet/Sia_Settings.txt'):
            with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            with open('Sia_Wallet/Sia_Settings.txt', 'r') as f:
                account2 = f.readlines()[0]
            with open('Santas_helpers\ETH-SIA_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                if account[0:2] == '0x':
                    batman.write(
                        'Santas_helpers\Claymore_dual\EthDcrMiner64.exe -epool eth-eu1.nanopool.org:9999 -ewal ' + account.replace(
                            "\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", "") +
                        ' -epsw x -dpool stratum+tcp://sia-eu1.nanopool.org:7777 -dwal ' + account2.replace("\n",
                                                                                                            "") + "/" + rig_name.replace(
                            "\n", "") + "/" + email.replace("\n", "") + ' -dpsw x -dcoin sia -ftime 10')
                else:
                    batman.write(
                        'Santas_helpers\Claymore_dual\EthDcrMiner64.exe -epool eth-eu1.nanopool.org:9999 -ewal 0x' + account.replace(
                            "\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", "") +
                        ' -epsw x -dpool stratum+tcp://sia-eu1.nanopool.org:7777 -dwal ' + account2.replace("\n",
                                                                                                            "") + "/" + rig_name.replace(
                            "\n", "") + "/" + email.replace("\n", "") + ' -dpsw x -dcoin sia -ftime 10')
            subprocess.Popen("Santas_helpers\ETH-SIA_Start.bat", shell=True)
    def eth_pascal_mine(self):
        if os.path.isfile('Ethereum_Wallet/Ethereum_Settings.txt') and os.path.isfile('Pascal_Wallet/Pascal_Settings.txt'):
            with open('Ethereum_Wallet/Ethereum_Settings.txt', 'r') as f:
                account = f.readlines()[0]
            with open('Pascal_Wallet/Pascal_Settings.txt', 'r') as f:
                account2 = f.readlines()[0]
            with open('Santas_helpers\ETH-Pascal_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                if account[0:2] == '0x':
                    batman.write(
                        'Santas_helpers\Claymore_dual\EthDcrMiner64.exe -epool eth-eu1.nanopool.org:9999 -ewal ' + account.replace(
                            "\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", "") +
                        ' -epsw x -dpool stratum+tcp://pasc-eu1.nanopool.org:15555 -dwal ' +
                        account2.replace("\n","") + ".0." + rig_name.replace(
                            "\n", "") + "/" + email.replace("\n", "") + ' -dpsw x -dcoin pasc -ftime 10')
                else:
                    batman.write(
                        'Santas_helpers\Claymore_dual\EthDcrMiner64.exe -epool eth-eu1.nanopool.org:9999 -ewal 0x' + account.replace(
                            "\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", "") +
                        ' -epsw x -dpool stratum+tcp://pasc-eu1.nanopool.org:15555 -dwal ' +
                        account2.replace("\n","") + ".0." + rig_name.replace(
                            "\n", "") + "/" + email.replace("\n", "") + ' -dpsw x -dcoin pasc -ftime 10')
            subprocess.Popen("Santas_helpers\ETH-Pascal_Start.bat", shell=True)
    def zcash_mine(self):
        if os.path.exists('Zcash_Wallet/Zcash_Settings.txt'):
            with open('Zcash_Wallet/Zcash_Settings.txt') as f:
                account = f.readlines()[0]
        proc = subprocess.Popen('WMIC CPU Get NumberOfCores,NumberOfLogicalProcessors /Format:List',
                                stdout=subprocess.PIPE, shell=True)

        num_threads = (proc.communicate()[0]).decode('utf-8').split()[-1].strip()
        num_threads = re.search(r"[0-9]+", num_threads).group(0).strip()
        cpu_t = int(num_threads) - 1  # adding thread count
        with open('Santas_helpers\Zcash_Start.bat', 'w')as batman:
            if graphic_card == 'nvidia\n' or graphic_card == 'nvidia':
                shit_call = r"Santas_helpers\nheqminer -l zec-eu1.nanopool.org:6666 -u " + account.replace("\n",
                                                                                                           "") + "/" + rig_name.replace(
                    "\n", "") + " -t " + str(cpu_t).replace("\n", "") + " -cd"
                for ig in range(int(num_gpus)):
                    shit_call = shit_call + " " + str(ig)
                shit_call = shit_call + '\n'
                batman.write(shit_call)
            elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                shit_call = "Santas_helpers\genoil.exe -c zec-eu1.nanopool.org:6666 -u " + account.replace("\n",
                                                                                                           "") + "/" + rig_name.replace(
                    "\n", "") + "/" + email.replace("\n", "") + " -p x -g"
                for ig in range(int(num_gpus)):
                    shit_call = shit_call + " " + str(ig)
                shit_call = shit_call + " -i 20 -w 64 -P 0\n"
                batman.write(shit_call)
                print(shit_call)
        subprocess.Popen("Santas_helpers\Zcash_Start.bat", shell=True)

    def start_mining(self):
        global account
        global account2
        global rig_name
        global email
        global currency_caller
        global num_threads

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
                #NVIDIA
                print(graphic_card)
                if graphic_card == 'nvidia\n' or graphic_card == 'nvidia':
                    batman.write(
                        "Santas_helpers\ethminer.exe -I -F http://eth-eu1.nanopool.org:8888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
                elif graphic_card == 'amd\n'  or 'amd' in graphic_card:
                    batman.write("Santas_helpers\ethminer.exe -P -F http://eth-eu1.nanopool.org:8888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
            subprocess.Popen("Santas_helpers\etherum_Start.bat", shell=True)
            hashrate = self.scrape_nanopool('eth')
            self.hashrate_label.setText(hashrate + 'Mh/s')

        elif currency_caller == 'Ethereum_Classic':
            if os.path.exists('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt') as f:
                    account = f.readlines()[0]
            with open('Santas_helpers\etherumClassic_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                if graphic_card == 'nvidia\n' or graphic_card == 'nvidia':
                    batman.write(
                        "Santas_helpers\ethminer.exe -I -F http://etc-eu1.nanopool.org:18888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", "") )
                elif graphic_card == 'amd\n '  or 'amd' in graphic_card:
                    batman.write(
                        "Santas_helpers\ethminer.exe -P -F http://etc-eu1.nanopool.org:18888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
            subprocess.Popen("Santas_helpers\etherumClassic_Start.bat", shell=True)

            hashrate = self.scrape_nanopool('etc')
            self.hashrate_label.setText(hashrate + 'Mh/s')

        elif currency_caller == 'Zcash':
            self.zcash_mine()
            hashrate = self.scrape_nanopool('zec')
            self.hashrate_label.setText(hashrate + 'Mh/s')

        elif currency_caller == 'Sia':
            self.sia_mine()
            hashrate = self.scrape_nanopool('zec')
            self.hashrate_label.setText(hashrate + 'Mh/s')

        elif currency_caller == 'Monero':
            self.monero_mine()
            hashrate = self.scrape_nanopool('xmr')
            self.hashrate_label.setText(hashrate + 'Mh/s')

        elif currency_caller == 'ETH-SIA':
            self.eth_sia_mine()

            hashrate_sia = self.scrape_nanopool('sia')
            hashrate_eth = self.scrape_nanopool('eth')
            self.hashrate_label.setText(hashrate_eth + 'Mh/s' + '\n' + hashrate_sia + 'Mh/s')

        elif currency_caller == 'ETH-Pascal-monero':
            self.eth_pascal_mine()
            self.monero_mine()

            hashrate_pasc = self.scrape_nanopool('pasc')
            hashrate_eth = self.scrape_nanopool('eth')
            hashrate_xmr = self.scrape_nanopool('xmr')
            self.hashrate_label.setText(hashrate_eth + 'Mh/s' + '\n' + hashrate_pasc + 'Mh/s' + '\n' +
                                        hashrate_xmr + 'Mh/s')

        elif currency_caller == 'monero_zcash':
            self.zcash_mine()
            self.monero_mine()

            hashrate_zec = self.scrape_nanopool('zec')
            hashrate_xmr = self.scrape_nanopool('xmr')
            self.hashrate_label.setText(hashrate_xmr + 'Mh/s' + '\n' + hashrate_zec + 'Mh/s')

        elif currency_caller == 'ETH-SIA-monero':
            self.eth_sia_mine()
            self.monero_mine()

            hashrate_sia = self.scrape_nanopool('sia')
            hashrate_eth = self.scrape_nanopool('eth')
            hashrate_xmr = self.scrape_nanopool('xmr')
            self.hashrate_label.setText(hashrate_eth + 'Mh/s' + '\n' + hashrate_sia + 'Mh/s' + '\n' +
                                        hashrate_xmr + 'Mh/s')
        elif currency_caller == 'monero_gpu':
            self.monero_GPU_mine()

            # HASHRATE FOR MONERO GOES HERE

        elif currency_caller == 'monero_gpu_cpu':
            self.monero_mine()
            self.monero_GPU_mine()

            # HASHRATE FOR MONERO GPU AND CPU GOES HERE

    def Establish_Connections(self):
        global currency_caller
        global num_threads

        proc = subprocess.Popen('WMIC CPU Get NumberOfCores,NumberOfLogicalProcessors /Format:List',
                                stdout=subprocess.PIPE, shell=True)

        num_threads = (proc.communicate()[0]).decode('utf-8').split()[-1].strip()
        num_threads = re.search(r"[0-9]+", num_threads).group(0).strip()

        self.coinName_label.setText(currency_caller)

        if currency_caller == 'ETH-SIA' or currency_caller == 'monero_zcash':
            self.address_label.setText('0x' + account + '\n' +
                                       '0x' + account2)
        elif currency_caller == 'ETH-SIA-monero' or currency_caller == 'ETH-Pascal-monero':
            self.address_label.setText('0x' + account + '\n' +
                                       '0x' + account2 + '\n' +
                                       '0x' + account3)
        else:
            self.address_label.setText('0x'+ account)

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
        elif currency_caller == 'Ethereum_Classic':
            os.system("taskkill /f /im  ethminer.exe")
        elif currency_caller == 'Zcash':
            if graphic_card == 'nvidia\n'  or 'nvidia' in graphic_card:
                os.system("taskkill /f /im  nheqminer.exe")
            elif graphic_card == 'amd\n'  or 'amd' in graphic_card:
                os.system("taskkill /f /im  genoil.exe")
        elif currency_caller == 'Sia':
            if graphic_card == 'nvidia\n'  or 'nvidia' in graphic_card:
                os.system("taskkill /f /im  ccminer.exe")
            elif graphic_card == 'amd\n'  or 'amd' in graphic_card:
                os.system("taskkill /f /im  ominer.exe")
        elif currency_caller == 'ETH-SIA':
            os.system("taskkill /f /im EthDcrMiner64.exe")
        elif currency_caller == 'Monero':
            os.system("taskkill /f /im  xmrig.exe")
        elif currency_caller == 'monero_gpu':
            os.system("taskkill /f /im  xmrMiner_0.2.1.exe")
        elif currency_caller == 'monero_gpu_cpu':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im  xmrMiner_0.2.1.exe")
        elif currency_caller == 'ETH-Pascal-monero':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im EthDcrMiner64.exe")
        elif currency_caller == 'monero_zcash':
            if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                os.system("taskkill /f /im  nheqminer.exe")
            elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                os.system("taskkill /f /im  genoil.exe")
            os.system("taskkill /f /im  xmrig.exe")
        elif currency_caller == 'ETH-SIA-monero':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im EthDcrMiner64.exe")
        global choosecurrency
        choosecurrency = ChooseCurrency()
        choosecurrency.show()
        self.close()

    def startOver(self):
        global currency_caller
        global num_threads

        if currency_caller == 'Ethereum':
            os.system("taskkill /f /im  ethminer.exe")
            if os.path.exists('Ethereum_Wallet/Ethereum_Settings.txt'):
                with open('Ethereum_Wallet/Ethereum_Settings.txt') as f:
                    account = f.readlines()[0]
            with open('Santas_helpers\etherum_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                # NVIDIA

                if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                    batman.write(
                        "Santas_helpers\ethminer.exe -I -F http://eth-eu1.nanopool.org:8888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
                elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                    batman.write(
                        "Santas_helpers\ethminer.exe -P -F http://eth-eu1.nanopool.org:8888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
            subprocess.Popen("Santas_helpers\etherum_Start.bat", shell=True)
        elif currency_caller == 'Ethereum_Classic':
            os.system("taskkill /f /im  ethminer.exe")
            if os.path.exists('EthereumClassic_Wallet/EthereumClassic_Settings.txt'):
                with open('EthereumClassic_Wallet/EthereumClassic_Settings.txt') as f:
                    account = f.readlines()[0]
            with open('Santas_helpers\etherumClassic_Start.bat', 'w')as batman:
                batman.write('setx GPU_FORCE_64BIT_PTR 0\n')
                batman.write('setx GPU_MAX_HEAP_SIZE 100\n')
                batman.write('setx GPU_USE_SYNC_OBJECTS 1\n')
                batman.write('setx GPU_SINGLE_ALLOC_PERCENT 100\n')
                batman.write('setx GPU_MAX_ALLOC_PERCENT 100\n')
                if graphic_card == 'nvidia\n'  or 'nvidia' in graphic_card:
                    batman.write(
                        "Santas_helpers\ethminer.exe -I -F http://etc-eu1.nanopool.org:18888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
                elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                    batman.write(
                        "Santas_helpers\ethminer.exe -P -F http://etc-eu1.nanopool.org:18888/0x" + account.replace("\n", "") + "/" + rig_name.replace("\n", "") + "/" + email.replace("\n", ""))
            subprocess.Popen("Santas_helpers\etherumClassic_Start.bat", shell=True)
        elif currency_caller == 'Zcash':
            if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                os.system("taskkill /f /im  nheqminer.exe")
            elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                os.system("taskkill /f /im  genoil.exe")
            self.zcash_mine()
        elif currency_caller == 'Sia':
            if graphic_card == 'nvidia\n':
                os.system("taskkill /f /im  ccminer.exe")
            elif graphic_card == 'amd\n':
                os.system("taskkill /f /im  ominer.exe")
            self.sia_mine()
        elif currency_caller == 'Monero':
            os.system("taskkill /f /im  xmrig.exe")
            self.monero_mine()
        elif currency_caller == 'monero_gpu':
            os.system("taskkill /f /im  xmrMiner_0.2.1.exe")
            self.monero_GPU_mine()
        elif currency_caller == 'monero_gpu_cpu':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im  xmrMiner_0.2.1.exe")
            self.monero_GPU_mine()
            self.monero_mine()
        elif currency_caller == 'ETH-SIA':
            os.system("taskkill /f /im EthDcrMiner64.exe")
            self.eth_sia_mine()
        elif currency_caller == 'ETH-Pascal-monero':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im EthDcrMiner64.exe")
            self.eth_pascal_mine()
            self.monero_mine()
        elif currency_caller == 'monero_zcash':
            if graphic_card == 'nvidia\n' or 'nvidia' in graphic_card:
                os.system("taskkill /f /im  nheqminer.exe")
            elif graphic_card == 'amd\n' or 'amd' in graphic_card:
                os.system("taskkill /f /im  genoil.exe")
            os.system("taskkill /f /im  xmrig.exe")
            self.zcash_mine()
            self.monero_mine()
        elif currency_caller == 'ETH-SIA-monero':
            os.system("taskkill /f /im  xmrig.exe")
            os.system("taskkill /f /im EthDcrMiner64.exe")
            self.eth_sia_mine()
            self.monero_mine()

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
    if not os.path.exists('Monero_Wallet'):
        os.makedirs('Monero_Wallet')
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