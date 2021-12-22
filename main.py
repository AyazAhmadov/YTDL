from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from widgets.main_window import MainWindow

# TODO:
#   Handle error for connection issues
#   Fps

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(title='Youtube Downloader', icon='assets/icon.png', border_radius=15)
    app.exec()