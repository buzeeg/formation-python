import sys
from random import randint

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication
from matplotlib.backend_bases import MouseEvent

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
        self.canvas.mpl_connect("button_press_event", self.canvasClicked)

        layout = QVBoxLayout(mainWidget)
        layout.addWidget(btnClickMe)
        layout.addWidget(self.canvas)

        self.plt = self.canvas.figure.subplots()
        xValues = range(randint(10, 20))
        yValues = [x**2 for x in xValues]
        self.plt.plot(xValues, yValues, "r-o")

    @Slot(MouseEvent)
    def canvasClicked(self, event):
        self.plt.scatter(event.xdata, event.ydata, marker="+", s=100)
        self.canvas.draw()

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
