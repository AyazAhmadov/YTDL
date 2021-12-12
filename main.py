from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from widgets.main_window import MainWindow

# TODO:
#   Handle error for connection issues

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(width=520, height=500, title='Youtube Downloader', icon='assets/icon.png')
    app.exec()