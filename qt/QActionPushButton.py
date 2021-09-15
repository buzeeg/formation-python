from PySide6.QtGui import QAction
from PySide6.QtWidgets import QPushButton


class QActionPushButton(QPushButton):
    def __init__(self, action: QAction, parent=None):
        super().__init__(parent)
        self.setIcon(action.icon())
        self.setText(action.text())
        self.__action = action

        self.clicked.connect(action.triggered)

    def enterEvent(self, mouseEvent):
        self.topLevelWidget().statusBar().showMessage(self.__action.statusTip())

    def leaveEvent(self, mouseEvent):
        self.topLevelWidget().statusBar().showMessage("")
