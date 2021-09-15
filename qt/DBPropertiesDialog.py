from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout


class DBPropertiesDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle("Connection info - " + parent.windowTitle())
        self.setWindowIcon(QIcon("../iconsDL/sql.png"))
        self.setModal(True)

        # Create buttons
        ok = QPushButton("Ok")
        ok.clicked.connect(self.okSlot)
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.cancelSlot)

        # Create layouts
        btnLayout = QVBoxLayout()
        btnLayout.addWidget(ok)
        btnLayout.addWidget(cancel)
        btnLayout.addStretch(1)

        globalLayout = QHBoxLayout()
        globalLayout.addStretch(1)
        globalLayout.addLayout(btnLayout)

        self.setLayout(globalLayout)


    @Slot()
    def okSlot(self):
        print("ok")

    @Slot()
    def cancelSlot(self):
        # self.close()
        print("cancel")
