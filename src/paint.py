from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class PaintWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 500, 500)
        self.setFixedSize(500, 500)
        self.image = QPixmap(500, 500)
        self.image.fill(QColor(255, 255, 255))
        self.last_pos = QPoint()
        self.draw_color = QColor(0, 0, 0)
        self.draw_size = 3

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.draw_color, self.draw_size, Qt.PenStyle.SolidLine))
            painter.drawLine(self.last_pos, event.pos())
            self.last_pos = event.pos()
            self.update()

    def set_color(self, color):
        self.draw_color = color