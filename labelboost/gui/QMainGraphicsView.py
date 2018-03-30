from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGraphicsView


class QMainGraphicsView(QGraphicsView):
    # Allows editing images
    textChanged = pyqtSignal(str)

    def __init__(self, image=None):
        super().__init__()

        self.image = image
        self.text = "x: 0,  y: 0"

        self.setMouseTracking(True)

