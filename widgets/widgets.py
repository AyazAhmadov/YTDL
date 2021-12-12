from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from classes.errors import IrrelevantArgumentError
from constants import *

class LineEdit(QLineEdit):
    def __init__(
        self,
        parent: QWidget=None,
        width: int=400,
        height: int=40,
        background_color: str=BACKGROUND_COLOR,
        text_color: str=TEXT_COLOR,
        placeholder_text: str=None,
        border: bool=False,
        border_color: str=None,
        border_width: int=0,
        border_radius: int=None,
        font_family: str='Segoe UI',
        font_size: int=15
    ):
        if not border and border_color:
            raise IrrelevantArgumentError('border', 'border_color', border)

        if not border and border_width:
            raise IrrelevantArgumentError('border', 'border_width', border)

        QLineEdit.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)

        # Setting Attributes
        self.background_color = background_color
        self.text_color = text_color
        self.placeholder_text = placeholder_text
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.font_family = font_family
        self.font_size = font_size

        self.set_stylesheet()

        self.setTextMargins(10, 0, 0, 0)

        # Setting Font
        font = QFont(self.font_family, self.font_size)
        self.setFont(font)
        self.setPlaceholderText(self.placeholder_text)
        
    def set_stylesheet(self):
        qss = f'''
        background-color: {self.background_color};
        color: {self.text_color};
        '''

        if self.border:
            if self.border_width:
                border_qss = f'border: {self.border_width}px'
            else:
                border_qss = 'border: 2px'

            border_qss += ' solid '

            if self.border_color:
                border_qss += self.border_color + ';'
            else:
                border_qss += self.text_color + ';'

            qss += border_qss

        if self.border_radius is not None:
            if self.border_radius == 0:
                border_radius_qss = f'border-radius: {self.height()//2}px;'
            else:
                border_radius_qss = f'border-radius: {self.border_radius}px;'

            qss += border_radius_qss

        qss = qss.strip()
        self.setStyleSheet(qss)

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget=None,
        width: int=90,
        height: int=30,
        button_text: str='Button',
        background_color: str=BACKGROUND_COLOR,
        hover_color: str=HOVER_COLOR,
        pressed_color: str=PRESSED_COLOR,
        text_color: str=TEXT_COLOR,
        border: bool=False,
        border_color: str=None,
        border_width: int=0,
        border_radius=None,
        font_family: str='Segoe UI',
        font_size: int=10
    ):
        if not border and border_color:
            raise IrrelevantArgumentError('border', 'border_color', border)

        if not border and border_width:
            raise IrrelevantArgumentError('border', 'border_width', border)

        QPushButton.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)

        # Setting Attributes
        self.button_text = button_text
        self.background_color = background_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.text_color = text_color
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.font_family = font_family
        self.font_size = font_size

        self.set_stylesheet()

        # Setting font and text
        font = QFont(self.font_family, self.font_size)
        self.setFont(font)
        self.setText(self.button_text)

    def set_stylesheet(self):
        button_qss = f'''QPushButton{{
        background-color: {self.background_color};
        color: {self.text_color};
        '''

        if self.border:
            if self.border_width:
                border_qss = f'border: {self.border_width}px'
            else:
                border_qss = 'border: 2px'

            border_qss += ' solid '

            if self.border_color:
                border_qss += self.border_color + ';\n'
            else:
                border_qss += self.text_color + ';\n'

            button_qss += border_qss

        if self.border_radius is not None:
            if self.border_radius == 0:
                border_radius_qss = f'border-radius: {self.height()//2}px;\n'
            else:
                border_radius_qss = f'border-radius: {self.border_radius}px;\n'

            button_qss += border_radius_qss

        button_qss = button_qss + '}\n\n'

        hover_qss = f'''QPushButton:hover{{
            background-color: {self.hover_color}\n}}\n\n
        '''

        pressed_qss = f'''QPushButton:pressed{{
            background-color: {self.pressed_color}\n}}
            '''

        qss = button_qss + hover_qss + pressed_qss
        qss = qss.strip()
        self.setStyleSheet(qss)

class TopFrame(QFrame):
    def __init__(
        self,
        parent: QWidget=None,
        width: int=600,
        height: int=30
    ):
        QFrame.__init__(self)
        self.setParent(parent)
        self.setFixedHeight(height)
        self.setMinimumWidth(width)

        # self.setStyleSheet('border: 2px solid black; background-color: red')

        self.pressing = False

        self.close_button = Button(
            parent=self,
            width=14,
            height=14,
            background_color=CLOSE_BACKGROUND,
            hover_color=CLOSE_HOVER,
            pressed_color=CLOSE_PRESSED,
            border_radius=0,
            button_text=''
        )
        self.close_button.setGeometry(
            self.width()-20,
            (self.height()-self.close_button.height())/2,
            self.close_button.width(),
            self.close_button.height()
        )
        self.close_button.clicked.connect(lambda: self.window().close())

        self.minimize_button = Button(
            parent=self,
            width=14,
            height=14,
            background_color=MINIMIZE_BACKGROUND,
            hover_color=MINIMIZE_HOVER,
            pressed_color=MINIMIZE_PRESSED,
            border_radius=0,
            button_text=''
        )
        self.minimize_button.setGeometry(
            self.close_button.x()-20,
            (self.height()-self.minimize_button.height())/2,
            self.minimize_button.width(),
            self.minimize_button.height()
        )
        self.minimize_button.clicked.connect(lambda: self.window().showMinimized())

        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.pressing = True
            self.start = self.window().mapToGlobal(event.pos())

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.pressing = False

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.pressing:
            self.end = self.window().mapToGlobal(event.pos())
            self.movement = self.end - self.start
            rect = self.window().mapToGlobal(self.movement)
            self.window().setGeometry(
                rect.x(),
                rect.y(),
                self.window().width(),
                self.window().height()
                )
            self.start = self.end

    # def paintEvent(self, event: QPaintEvent) -> None:
    #     p = QPainter(self)
    #     p.setPen(QColor('#000000'))

    #     p.drawRect(self.rect())

    #     p.end()

class DownloadPage(QFrame):
    def __init__(self):
        QFrame.__init__(self)