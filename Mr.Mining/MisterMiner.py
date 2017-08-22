import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Build the window widget
    w = QWidget()
    w.setGeometry(300, 300, 250, 150)  # x, y, w, h
    w.setWindowTitle("My First Qt App")

    # Add a label with tooltip
    label = QLabel("Hello World  🚀", w)
    label.setToolTip("This is a <b>QLabel</b> widget with Tooltip")
    label.resize(label.sizeHint())
    label.move(80, 50)



    browser = QWebEngineView()
    browser.load(QUrl("https://eth.nanopool.org/account/0xabc5d8b3d2bb800de6bccd100c5cb7ca5d57edd2"))
    frame = browser.page()
    frame.runJavaScript("return hashrate()")

    # Show window and run
    w.show()
    app.exec_()