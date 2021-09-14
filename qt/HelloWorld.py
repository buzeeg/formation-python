import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
