from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem


class QMainGraphicsScene(QGraphicsScene):
    # Allows editing images

    textChanged = pyqtSignal(str)

    def __init__(self, image=None):
        super().__init__()

        self.image = image
        self.text = "x: 0,  y: 0"
        self.vertLine = self.addLine(0, 0, 0, 0, QPen(Qt.black, 3, Qt.SolidLine))
        self.horzLine = self.addLine(0, 0, 0, 0, QPen(Qt.black, 3, Qt.SolidLine))

    def mouseMoveEvent(self, e):
        x = e.scenePos().x()
        y = e.scenePos().y()

        self.vertLine.setLine(0, 0, self.sceneRect().width(), 0)
        self.horzLine.setLine(0, 0, 0, self.sceneRect().height())

        self.text = "x: {0},  y: {1}".format(x, y)
        self.textChanged.emit(self.text)