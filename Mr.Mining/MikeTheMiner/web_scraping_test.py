"""from ghost import Ghost

ghost = Ghost()
page, resources = ghost.open('https://eth.nanopool.org/account/0xabc5d8b3d2bb800de6bccd100c5cb7ca5d57edd2')
result, resources = ghost.evaluate("document.getElementByClassName('panel-body');")
"""
"""from PyQt5.QtWebEngineWidgets import QWebEngineView

browser = QWebEngineView()
browser.load("https://eth.nanopool.org/account/0xabc5d8b3d2bb800de6bccd100c5cb7ca5d57edd2")
frame = browser.page().currentFrame()
frame.evaluateJavaScript("hashrate()")
"""

#from selenium import webdriver
#driver = webdriver.Firefox()
#driver.get("https://eth.nanopool.org/account/0xabc5d8b3d2bb800de6bccd100c5cb7ca5d57edd2")
#a = driver.execute_script("return hashrate()")
#element = driver.find_elements_by_class_name("panel-body")
#text = driver.find_elements_by_xpath("Mh")
#text = driver.find_elements_by_name("#text")
#print(text)

#element.click()
#"text: hashrate() + ' Mh/s'"

from urllib.request import Request, urlopen
import json
import logging
from sys import argv
from subprocess import Popen as popen
from time import sleep

def get_hashrate(url):
    while True:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        info = json.loads(urlopen(req).read().decode('utf-8'))
        if info['status']:
            print("working")
            print(float(info['data']))
            return float(info['data'])
        else:
            print('error')
            logging.error('Nanopool API:' + info['error'] + ', trying again in 30 seconds')
            sleep(30)

def check_hashrate(url):
    count = 0
    while True:
        if get_hashrate(url) == 0:
            count += 1
            logging.warning('Nanopool API: Hashrate seems to be zero')
        else:
            count = 0

        if count == 2:
            popen('taskkill /f /im {}'.format('ethminer.exe'))
            sleep(10)
            print("hashrate is 0")
            # Restarts the miner
            #popen('ethminer.exe' + ' )

        sleep(5)

check_hashrate('https://api.nanopool.org/v1/eth/balance/0x2fc7723d8623eb414abb4fa6d81395d81b87a8f9')

#account = '4BKQQ7FPdpAFVne2icuXW53VdaepFWfPNLhv9bwHFD6xdGrPLMpXLYDSuDvTx8z8hQWM6k5r4PTAuFPXW1MKKBRhB45G15Z'
#get_hashrate('http://dwarfpool.com/xmr/api?wallet=' + account + '&email=xmr@example.com')
