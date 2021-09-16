from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTextEdit


class MdiSubWindow(QTextEdit):
    def __init__(self, title="", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.setMinimumSize(300, 200)
