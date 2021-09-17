import sys
from random import randint

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas


class CurveWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        btnClickMe = QPushButton("Push Me!")
        btnClickMe.clicked.connect(self.clickMeSlot)
        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))

        layout = QVBoxLayout(mainWidget)
        layout.addWidget(btnClickMe)
        layout.addWidget(self.canvas)

        self.plt = self.canvas.figure.subplots()
        xValues = range(randint(10, 20))
        yValues = [x**2 for x in xValues]
        self.plt.plot(xValues, yValues, "r-o")

    @Slot()
    def clickMeSlot(self):
        self.plt.clear()
        xValues = range(randint(10, 20))
        yValues = [x**2 for x in xValues]
        self.plt.plot(xValues, yValues, "g-+")
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CurveWindow()
    window.show()

    sys.exit(app.exec_())
