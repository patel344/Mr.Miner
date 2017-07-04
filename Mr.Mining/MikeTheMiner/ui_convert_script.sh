#!/bin/bash

pyuic5 MainPage.ui -o MainPage.py
pyuic5 AccountInfo.ui -o AccountInfo.py
pyuic5 ChooseCurrency.ui -o ChooseCurrency.py
pyuic5 CreateNewWallet.ui -o CreateNewWallet.py
pyuic5 MiningWallet.ui -o MiningWallet.py
pyuic5 NowMining.ui -o NowMining.py
pyuic5 SetupPage.ui -o SetupPage.py

pyrcc5 MainPageMining.qrc -o MainPageMining_rc.py
pyrcc5 ChooseCurrency.qrc -o ChooseCurrency_rc.py