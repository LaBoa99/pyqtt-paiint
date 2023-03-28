from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from herramientas import Herramientas


class PaintWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.tool = Herramientas.PINCEL
        self.image = QPixmap(self.size())
        self.image.fill(QColor(255, 255, 255))
        self.last_pos = QPoint()
        self.draw_color = QColor(0, 0, 0)
        self.draw_size = 3
        
        self.points: list[QPoint] = []

    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_pos = event.pos()
            if int(self.tool.value) >= 6:
                self.points.append(event.pos())
                if len(self.points) == 2:
                    painter = QPainter(self.image)
                    pointEnd = self.points.pop()
                    pointStart = self.points.pop()
                    painter.setPen(QPen(self.draw_color, self.draw_size, Qt.PenStyle.SolidLine))
                    rect = QRect(pointStart.x(), pointStart.y(), pointEnd.x() - pointStart.x(), pointEnd.y() - pointStart.y())
                    match self.tool:
                        case Herramientas.CUADRADO:
                            painter.drawRect(rect)
                        case Herramientas.CUADRADO_REDONDO:
                            painter.drawRoundedRect(rect, 10, 10)
                        case Herramientas.CIRCULO:
                            painter.drawEllipse(rect)
                        case Herramientas.TRIANGULO:
                            thirdPoint = QPoint(pointStart.x() * 2, pointStart.y())
                            path = QPainterPath()
                            path.moveTo(pointStart.x(), pointStart.y())
                            path.lineTo(pointEnd.x(), pointEnd.y())
                            path.lineTo(thirdPoint.x(), thirdPoint.y())
                            path.lineTo(pointStart.x(), pointStart.y())
                            painter.drawPath(path)
                        case Herramientas.LINEA:
                            painter.drawLine(pointStart.x(), pointStart.y(), pointEnd.x(), pointEnd.y())
                    self.points.clear()
                    self.update()
            else:
                match self.tool:
                    case Herramientas.CUBETA:
                        painter = QPainter(self.image)
                        painter.setPen(QPen(self.draw_color, 1, Qt.PenStyle.SolidLine))
                        image = self.image.toImage()
                        limitColor = image.pixelColor(self.last_pos)
                        to_paint = [ (self.last_pos, limitColor) ]
                        to_fill = []
                        while to_paint:
                            pos, color = to_paint.pop(0)
                            pixel_color = image.pixelColor(pos)
                            if not self.image.rect().contains(self.pos()):
                                continue
                            if color != pixel_color:
                                to_fill.append(QPoint(x, y))
                                continue

                            #painter.drawPoint(pos)
                            x, y = pos.x(), pos.y()
                            to_paint.append((QPoint(x - 1, y), color))
                            to_paint.append((QPoint(x + 1, y), color))
                            to_paint.append((QPoint(x, y - 1), color))
                            to_paint.append((QPoint(x, y + 1), color))
                            to_fill.append(QPoint(x, y))
                        print("Finalizo relleno", to_fill)
                        for i in to_fill:
                            print("Rellenando")
                            painter.drawPoint(i)
                        self.update()
                    case Herramientas.CUENTA_GOTAS:
                        self.draw_color = self.image.toImage().pixelColor(self.last_pos)
                        self.tool = Herramientas.PINCEL
            
        
    
    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() and Qt.MouseButton.LeftButton:
            painter = QPainter(self.image)
            match self.tool:
                case Herramientas.PINCEL:
                    painter.setPen(QPen(self.draw_color, self.draw_size, Qt.PenStyle.SolidLine))
                    painter.drawLine(self.last_pos, event.pos())
                case Herramientas.BORRADOR:
                    painter.eraseRect(event.pos().x(), event.pos().y(), 20, 20)
                case Herramientas.CUADRADO_REDONDO:
                    pass
            self.last_pos = event.pos()
            self.update()

    def set_color(self, color):
        self.draw_color = color