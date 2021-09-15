import datetime

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox


class QButtonBlock(QWidget):
    def __init__(self):
        super().__init__()

        # Create buttons
        self.__button1 = QPushButton("Button 1", self)
        self.__button1.setGeometry(2, 2, 200, 30)
        self.__button1.clicked.connect(self.slot1)
        self.__button2 = QPushButton("Button 2", self)
        self.__button2.setGeometry(2, 32, 200, 30)
        self.__button2.clicked.connect(self.slot2)

        # Display
        self.__label1 = QLabel(self)
        self.__label1.setGeometry(204, 2, 200, 30)
        self.__label1.setText(f"{datetime.datetime.now()}")

    # Define slots to connect signals
    @Slot()
    def slot1(self):
        self.__label1.setText(f"{datetime.datetime.now()}")

    @Slot()
    def slot2(self):
        QMessageBox.information(self, "MegaExplorer", "Coucou")
