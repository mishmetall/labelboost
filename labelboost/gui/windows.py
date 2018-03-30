import sys, cv2
from pathlib import Path

from PyQt5.QtCore import QRectF, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow, \
    QSplitter, QTreeView, QFileSystemModel
from PyQt5.QtGui import QIcon, QImage, QPixmap

from gui.QMainGraphicsScene import QMainGraphicsScene
from gui.QMainGraphicsView import QMainGraphicsView


class QLabelWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.window = QWidget(self)
        self.imview = QMainGraphicsView(self)
        self.imscene = QMainGraphicsScene(self)
        self.imview.setScene(self.imscene)
        self.openButton = QPushButton("Open")
        self.closeButton = QPushButton("Close")
        self.treeView = QTreeView(self)
        self.fsmodel = QFileSystemModel()
        self.statusBar()

        self.openButton.clicked.connect(self.openButtonClicked)
        self.imscene.textChanged.connect(self.displayText)

        hbox = QHBoxLayout()
        hbox.addWidget(self.openButton)
        hbox.addWidget(self.closeButton)
        hbox.addStretch(1)

        splitter = QSplitter()
        splitter.addWidget(self.treeView)
        splitter.addWidget(self.imview)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([125, 150])

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(splitter)

        self.fsmodel.setRootPath(QDir.currentPath())
        self.fsmodel.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.treeView.setModel(self.fsmodel)
        self.treeView.setRootIndex(self.fsmodel.index(QDir.currentPath()))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

        self.window.setLayout(vbox)
        self.setCentralWidget(self.window)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('LabelBoost: Tool for ML-supported labelling')
        self.setWindowIcon(QIcon('resources/icon.png'))

        self.show()

    def displayText(self, text):
        self.statusBar().showMessage(text)

    def openButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', str(Path.home()))[0]
        try:
            image = cv2.imread(fname)
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB, image)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qImg = QPixmap.fromImage(QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888))

            self.imview.setSceneRect(QRectF(qImg.rect()))  # Set scene size to image size.
            # self.updateViewer()

            [self.imscene.removeItem(item) for item in self.imscene.items()]
            self.imscene.addPixmap(qImg)
        except:
            self.statusBar().showMessage("Cannot open {fname}".format(fname))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QLabelWindow()
    sys.exit(app.exec_())