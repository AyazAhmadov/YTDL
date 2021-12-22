from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from widgets.widgets import LineEdit, Button, RadioButton, Label
from classes.downloader import Downloader

class VideoFrame(QFrame):
    def __init__(
        self,
        downloader: Downloader,
        parent=None,
        width: int=620,
        height: int=400
    ):
        QFrame.__init__(self)
        self.setFixedSize(width, height)
        self.setParent(parent)

        self.downloader = downloader
        pixmap = self.downloader.load_thumbnail()
        text = self.downloader.title

        self.thumbnail_label = Label(
            parent=self,
            width=162,
            height=162,
            pixmap_path=pixmap
        )
        rect = self.get_central_pos(self.thumbnail_label, y=20)
        self.thumbnail_label.setGeometry(rect)

        self.title_edit = LineEdit(
            parent=self,
            input_text=text,
            border=True,
            border_radius=0
        )
        rect = self.get_central_pos(self.title_edit, y=210)
        self.title_edit.setGeometry(rect)

        self.save_button = Button(
            parent=self,
            input_text='Save',
            border=True,
            border_radius=0
        )
        rect = self.get_central_pos(self.save_button, y=350)
        self.save_button.setGeometry(rect)

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