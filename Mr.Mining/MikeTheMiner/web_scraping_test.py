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

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://eth.nanopool.org/account/0xabc5d8b3d2bb800de6bccd100c5cb7ca5d57edd2")
#a = driver.execute_script("return hashrate()")
element = driver.find_elements_by_class_name("panel-body")
print(element)

#element.click()
#"text: hashrate() + ' Mh/s'"