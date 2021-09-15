import sys
import datetime

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)

        # Set window position
        self.move(50, 50)

        # Create buttons
        self.__button1 = QPushButton("Button 1", self)
        self.__button1.setGeometry(10, 210, 200, 30)
        self.__button1.clicked.connect(self.slot1)
        self.__button1.setToolTip("Super <u>bouton</u>")  # HTML support!
        self.__button2 = QPushButton("Button 2", self)
        self.__button2.setGeometry(10, 250, 200, 30)
        self.__button2.clicked.connect(self.slot2)
        self.__button2.setToolTip("""Super <u>bouton</u><br/>
                <ul>
                    <li>First</li>
                    <li>Second</li>
                </ul><br/>
                <img src="../iconsDL/file.png">
                """)  # HTML support!
        # self.__button2.setStyleSheet("background: red; color: white; border-radius: 20px 20px;")

        # Display
        self.__label1 = QLabel(self)
        self.__label1.setGeometry(220, 210, 200, 30)
        self.__label1.setText(f"{datetime.datetime.now()}")

    # Define slots to connect signals
    @Slot()
    def slot1(self):
        self.__label1.setText(f"{datetime.datetime.now()}")

    @Slot()
    def slot2(self):
        QMessageBox.information(self, "Message box", "Button2 pushed")


if __name__ == '__main__':
    sys.argv.append("-stylesheet")
    sys.argv.append("styles.css")
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
