import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class QLabelWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('LabelBoost: Tool for ML-supported labelling')
        self.setWindowIcon(QIcon('resources/icon.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QLabelWindow()
    sys.exit(app.exec_())