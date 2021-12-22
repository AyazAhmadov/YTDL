from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from classes.errors import IrrelevantArgumentError
from constants import *

class Label(QLabel):
    def __init__(
        self,
        parent: QWidget=None,
        width: int=192,
        height: int=192,
        input_text: str=None,
        alignment: Qt.AlignmentFlag=Qt.AlignCenter,
        pixmap_path: str=None,
        font_family: str='Segoe UI',
        font_size: int=12
    ):
        QLabel.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)

        self.setText(input_text)

        pixmap = QPixmap(pixmap_path)
        self.setPixmap(pixmap)

        self.setAlignment(alignment)

        font = QFont(font_family, font_size)
        self.setFont(font)

class LineEdit(QLineEdit):
    def __init__(
        self,
        parent: QWidget=None,
        width: int=400,
        height: int=40,
        background_color: str=BACKGROUND_COLOR,
        text_color: str=TEXT_COLOR,
        placeholder_text: str=None,
        input_text: str=None,
        border: bool=False,
        border_color: str=None,
        border_width: int=None,
        border_radius: int=None,
        font_family: str='Segoe UI',
        font_size: int=15
    ):
        if not border and border_color is not None:
            raise IrrelevantArgumentError('border', 'border_color', border)

        if not border and border_width is not None:
            raise IrrelevantArgumentError('border', 'border_width', border)

        QLineEdit.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)

        # Setting Attributes
        self.background_color = background_color
        self.text_color = text_color
        self.placeholder_text = placeholder_text
        self.input_text = input_text
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
        self.setText(self.input_text)
        
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
        cursor: Qt.CursorShape=Qt.PointingHandCursor,
        width: int=90,
        height: int=30,
        input_text: str='Button',
        background_color: str=BACKGROUND_COLOR,
        hover_color: str=HOVER_COLOR,
        pressed_color: str=PRESSED_COLOR,
        text_color: str=TEXT_COLOR,
        border: bool=False,
        border_color: str=None,
        border_width: int=None,
        border_radius=None,
        font_family: str='Segoe UI',
        font_size: int=12
    ):
        if not border and border_color is not None:
            raise IrrelevantArgumentError('border', 'border_color', border)

        if not border and border_width is not None:
            raise IrrelevantArgumentError('border', 'border_width', border)

        QPushButton.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)
        self.setCursor(cursor)

        # Setting Attributes
        self.input_text = input_text
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
        self.setText(self.input_text)

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
        height: int=30,
        background_color: str=None,
        border_radius: int=None
    ):
        QFrame.__init__(self)
        self.setParent(parent)
        self.setFixedSize(width, height)

        self.pressing = False
        self.background_color = background_color
        self.border_radius = border_radius

        self.setStyleSheet(f'border-radius: {self.border_radius}px; background-color: {self.background_color}')

        self.close_button = Button(
            parent=self,
            width=14,
            height=14,
            background_color=CLOSE_BACKGROUND,
            hover_color=CLOSE_HOVER,
            pressed_color=CLOSE_PRESSED,
            border=True,
            border_color=CLOSE_PRESSED,
            border_radius=0,
            input_text=''
        )
        self.close_button.setGeometry(
            self.width()-20,
            (self.height()-self.close_button.height())//2,
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
            border=True,
            border_color=MINIMIZE_PRESSED,
            border_radius=0,
            input_text=''
        )
        self.minimize_button.setGeometry(
            self.close_button.x()-20,
            (self.height()-self.minimize_button.height())//2,
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

class RadioButton(QRadioButton):
    def __init__(
        self,
        parent: QWidget=None,
        cursor: Qt.CursorShape=Qt.PointingHandCursor,
        width: int=90,
        height: int=20,
        background_color: str=WHITE,
        outer_circle_color: str=OUTER_CIRCLE_COLOR,
        inner_circle_color: str=INNER_CIRCLE_COLOR,
        hover_color: str=RADIOBUTTON_HOVER,
        text_color: str=RADIOBUTTON_TEXT_COLOR,
        input_text: str='Button',
        font_family='Segoe UI',
        font_size: int=12
    ):
        QRadioButton.__init__(self)
        self.setParent(parent)
        self.setCursor(cursor)
        self.setFixedSize(width, height)

        self.hover = False

        self.background_color = background_color
        self.outer_circle_color = outer_circle_color
        self.inner_circle_color = inner_circle_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.input_text = input_text
        self.font_family = font_family
        self.font_size = font_size

        self.setStyleSheet(f'color: {self.text_color}')

        font = QFont(self.font_family, self.font_size)
        self.setFont(font)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.hover = True

    def leaveEvent(self, event: QEvent) -> None:
        self.hover = False

    def paintEvent(self, e: QPaintEvent) -> None:
        h = self.height()
        r = h-4

        p = QPainter(self)
        p.setRenderHints(QPainter.Antialiasing)

        if self.hover:
            brush = QBrush(self.hover_color)
        else:
            brush = QBrush(self.background_color)
        p.setBrush(brush)
        p.drawEllipse(6, 2, r, r)

        p.setBrush(Qt.NoBrush)

        pen = QPen(self.outer_circle_color)
        pen.setWidth(2)
        p.setPen(pen)
        p.drawEllipse(6, 2, r, r)

        if self.isChecked():
            p.setPen(Qt.NoPen)
            brush = QBrush(self.inner_circle_color)
            p.setBrush(brush)
            p.drawEllipse(r/2+2, r/2-2, r/2, r/2)
            p.setBrush(Qt.NoBrush)

        pen.setColor(self.text_color)
        p.setPen(pen)
        y = h-6
        x = 2*r+10
        p.drawText(x, y, self.input_text)

        p.end()