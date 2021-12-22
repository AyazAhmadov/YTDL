from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from widgets.widgets import Label, LineEdit, Button, TopFrame, RadioButton
from widgets.video_frame import VideoFrame

from classes.downloader import Downloader
from constants import *

class MainWindow(QMainWindow):
    def __init__(
        self,
        width: int=620,
        height: int=430,
        title: str='Main Window',
        icon: str=None,
        background_color: str='#FAFAFA',
        border_radius: int=None
    ):
        QMainWindow.__init__(self)
        self.setFixedSize(width, height)

        self.setWindowTitle(title)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Setting attributes
        self.mode = 'v'

        self.title = title
        self.icon = icon
        self.background_color = background_color
        self.border_radius = border_radius

        self.main_frame = QFrame(self)
        self.main_frame.setFixedSize(self.size())

        self.setStyleSheet(f'background-color: {self.background_color}; border-radius: {self.border_radius}px')

        # TopFrame
        self.top_frame = TopFrame(
            parent=self.main_frame,
            width=self.width(),
            background_color=TOP_FRAME_BACKGROUND,
            border_radius=self.border_radius
        )
        self.top_frame.setGeometry(0, 0, self.top_frame.width(), self.top_frame.height())

        # Container
        self.container = QFrame(self.main_frame)
        self.container.setGeometry(0, 30, self.width(), self.height()-30)

        # Label
        self.icon_label = Label(
            parent=self.container,
            pixmap_path=ICON_SMALL
        )
        rect = self.get_central_pos(self.icon_label, y=10)
        self.icon_label.setGeometry(rect)

        # LineEdit
        self.url_edit = LineEdit(
            parent=self.container,
            width=470,
            placeholder_text='Enter the URL of the youtube video',
            border=True,
            border_radius=0
        )
        rect = self.get_central_pos(self.url_edit, y=220)
        self.url_edit.setGeometry(rect)
        self.url_edit.setFocus()

        # RadioButtons
        self.video_button = RadioButton(
            parent=self.container,
            input_text='Video',
            outer_circle_color=TEXT_COLOR,
            hover_color=HOVER_COLOR
        )
        rect = self.get_central_pos(self.video_button, y=280)
        self.video_button.setGeometry(rect)
        self.video_button.toggled.connect(self.__video)
        self.video_button.toggle()

        self.audio_button = RadioButton(
            parent=self.container,
            input_text='Audio',
            outer_circle_color=TEXT_COLOR,
            hover_color=HOVER_COLOR
        )
        rect = self.get_central_pos(self.audio_button, y=310)
        self.audio_button.setGeometry(rect)
        self.audio_button.toggled.connect(self.__audio)

        # Button
        self.donwload_button = Button(
            parent=self.container,
            border=True,
            border_radius=0,
            input_text='Download'
        )
        rect = self.get_central_pos(self.donwload_button, y=350)
        self.donwload_button.setGeometry(rect)
        self.donwload_button.clicked.connect(self.download)

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

    def __video(self):
        self.mode = 'v'

    def __audio(self):
        self.mode = 'a'

    def download(self):
        self.container.hide()

        url = self.url_edit.text()
        d = Downloader(url)

        v = VideoFrame(d, parent=self)
        v.setGeometry(0, 30, v.width(), v.height())
        # v.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Return:
            self.download()