import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from container import Ui_Paint
from herramientas import Herramientas
from paint import PaintWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Establecer el tamaño mínimo y máximo de la ventana
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        
        # Establecer un tamaño fijo para la ventana
        self.setFixedSize(800, 600)
        
        self.tool = Herramientas.LAPIZ
        self.paint = PaintWidget()
        
        self.paint_widget = Ui_Paint(self)
        self.paint_widget.setupUi(self)
        self.paint_widget.connect_signals()
        
        self.paint_widget.onColorClick.connect(lambda color: self.changeColor(color))
        self.paint_widget.onToolClick.connect(lambda tool: self.changeTool(tool))
        self.paint_widget.onCheckFill.connect(lambda value: self.changeFill(value))
        
        self.paint_widget.columnaColores.replaceWidget(self.paint_widget.WPaint, self.paint)
        self.paint_widget.WPaint.deleteLater()
        
        self.init_ui()

    def changeColor(self, color : QColor):
        self.paint.draw_color = color
    
    def changeTool(self, tool):
        print(tool)
        self.paint.tool = tool
    
    def changeFill(self, value):
        self.paint.fill = value
    
    def init_ui(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
