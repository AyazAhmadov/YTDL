from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from widgets.widgets import LineEdit, Button, TopFrame
from classes.downloader import Downloader
from constants import *

class MainWindow(QMainWindow):
    def __init__(
        self,
        width: int=600,
        height: int=300,
        title: str='Main Window',
        icon: str=None,
        background_color: str='#FFFFFF',
        border_radius: int=None
    ):
        QMainWindow.__init__(self)
        self.setFixedSize(width, height)

        self.setWindowTitle(title)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # Setting attributes
        self.title = title
        self.icon = icon
        self.background_color = background_color
        self.border_radius = border_radius

        self.setStyleSheet(f'background-color: {self.background_color}; border-radius: {self.border_radius}px')

        # Setting central widget
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName('central_widget')

        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setSpacing(0)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName('central_layout')

        # Top frame
        # self.top_container = QFrame(self.central_widget)
        # self.top_container.setObjectName('top_container')

        # self.top_layout = QVBoxLayout(self.top_container)
        # self.top_layout.setSpacing(0)
        # self.top_layout.setContentsMargins(0, 0, 0, 0)
        # self.top_layout.setObjectName('top_layout')

        # self.top_frame = TopFrame(parent=self.central_widget, width=self.width())
        # self.top_frame.setObjectName('top_frame')

        # self.top_layout.addWidget(self.top_frame, Qt.AlignTop, Qt.AlignCenter)

        # self.central_layout.addWidget(self.top_frame, Qt.AlignTop, Qt.AlignCenter)

        # Setting main frame
        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName('main_frame')

        self.main_layout = QVBoxLayout(self.main_frame)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName('main_layout')

        # Inserting icon to main frame
        self.icon_frame = QFrame(self.main_frame)
        self.icon_frame.setFixedHeight(270)
        self.icon_frame.setObjectName('icon_frame')

        self.icon_layout = QVBoxLayout(self.icon_frame)
        self.icon_layout.setSpacing(0)
        self.icon_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_layout.setObjectName('icon_layout')

        self.icon_label = QLabel(self.icon_frame)
        pixmap = QPixmap(ICON_SMALL)
        self.icon_label.setPixmap(pixmap)
        self.icon_label.setAlignment(Qt.AlignTop)
        self.icon_label.setObjectName('icon_label')

        self.icon_layout.addWidget(self.icon_label, Qt.AlignTop, Qt.AlignCenter)
        
        self.main_layout.addWidget(self.icon_frame, Qt.AlignCenter, Qt.AlignCenter)

        # Inserting LineEdit and Button
        self.url_frame = QFrame(self.main_frame)
        self.url_frame.setFixedHeight(200)
        self.url_frame.setObjectName('url_frame')

        self.url_edit = LineEdit(parent=self.url_frame, border=True, border_radius=20, placeholder_text='Enter URL of the youtube video')
        self.url_edit.setGeometry(self.get_central_pos(self.url_edit, y=90))
        self.url_edit.setObjectName('url_edit')

        self.search_button = Button(parent=self.url_frame, height=34, border=True, border_radius=0, font_size=12, button_text='Search')
        self.search_button.setGeometry(self.get_central_pos(self.search_button, y=150))
        self.search_button.setObjectName('search_button')

        ###
        self.main_layout.addWidget(self.url_frame)

        self.central_layout.addWidget(self.main_frame)

        self.setCentralWidget(self.central_widget)

        self.show()

    def get_central_pos(self, widget: QWidget, x: int=0, y: int=0) -> QRect:
        w = widget.width()
        h = widget.height()
        w_m = self.width()
        h_m = self.height()

        if not x:
            x = (w_m - w)/2
        if not y:
            y = (h_m - h)/2
        return QRect(x, y, w, h)

    def search(self):
        url = self.url_edit.text()
        d = Downloader(url)
