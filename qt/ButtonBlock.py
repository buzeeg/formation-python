import datetime

from PySide6.QtCore import Slot
from PySide6.QtGui import QMouseEvent, Qt, QCursor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QMenu

from QActionPushButton import QActionPushButton


class ButtonBlock(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Create buttons
        # self.__button1 = QPushButton("Button 1", self)
        # self.__button1.setGeometry(2, 2, 200, 30)
        # self.__button1.clicked.connect(self.slot1)
        # self.__button2 = QPushButton("Button 2", self)
        # self.__button2.setGeometry(2, 32, 200, 30)
        # self.__button2.clicked.connect(self.slot2)

        # Create buttons from actions
        self.__btn1_action = QAction(QIcon("../iconsDL/add.png"), "&Button 1", self)
        self.__btn1_action.setStatusTip("Click moi 1")
        self.__btn1_action.triggered.connect(self.slot1)
        self.__btn2_action = QAction(QIcon("../iconsDL/remove.png"), "&Button 2", self)
        self.__btn2_action.setStatusTip("Click moi 2")
        self.__btn2_action.triggered.connect(self.slot2)
        self.__button1 = QActionPushButton(self.__btn1_action, self)
        self.__button1.setGeometry(2, 2, 200, 30)
        self.__button2 = QActionPushButton(self.__btn2_action, self)
        self.__button2.setGeometry(2, 32, 200, 30)

        # Display
        self.__label1 = QLabel(self)
        self.__label1.setGeometry(204, 2, 200, 30)
        self.__label1.setText(f"{datetime.datetime.now()}")

        # PopupMenu
        # self.__popupMenu = QMenu("Demo PopupMenu")
        # self.__popupMenu.addAction(parent.actOpen)
        # self.__popupMenu.addAction(self.topLevelWidget().actSave)
        # self.__popupMenu.addSeparator()
        # self.__popupMenu.addAction(parent.actExit)

    # Override mousePressEvent of QWidget
    # def mousePressEvent(self, mouseEvent: QMouseEvent):
    #     if mouseEvent.button() == Qt.RightButton:
    #         self.__popupMenu.popup(QCursor.pos())

    # Define slots to connect signals
    @Slot()
    def slot1(self):
        self.__label1.setText(f"{datetime.datetime.now()}")

    @Slot()
    def slot2(self):
        self.__label1.setText(f"{datetime.datetime.now()}")
        # QMessageBox.information(self.topLevelWidget(), "MegaExplorer", "Coucou")
