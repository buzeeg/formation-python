from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QDialog, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy


class CalcGridDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Calc - " + parent.windowTitle())
        self.setWindowIcon(QIcon("../iconsDL/e-mail.png"))
        self.setModal(True)

        # Create buttons
        # ok = QPushButton("Ok")
        # ok.clicked.connect(self.okSlot)
        # cancel = QPushButton("Cancel")
        # cancel.clicked.connect(self.cancelSlot)

        # Create layouts
        lyt = QGridLayout()
        lineEdit = QLineEdit("0")
        # lineEdit.setMaximumHeight(200)
        # lineEdit.setTextMargins(0, 10, 2, 10)
        lineEdit.setAlignment(Qt.AlignRight)
        lineEdit.setStyleSheet("background: black")
        lyt.addWidget(lineEdit, 0, 0, 1, 4)

        lyt.addWidget(QPushButton("MC"), 1, 0)
        lyt.addWidget(QPushButton("M+"), 1, 1)
        lyt.addWidget(QPushButton("/"), 1, 2)
        lyt.addWidget(QPushButton("*"), 1, 3)

        lyt.addWidget(QPushButton("7"), 2, 0)
        lyt.addWidget(QPushButton("8"), 2, 1)
        lyt.addWidget(QPushButton("9"), 2, 2)
        lyt.addWidget(QPushButton("-"), 2, 3)

        lyt.addWidget(QPushButton("4"), 3, 0)
        lyt.addWidget(QPushButton("5"), 3, 1)
        lyt.addWidget(QPushButton("6"), 3, 2)
        lyt.addWidget(QPushButton("+"), 3, 3)

        lyt.addWidget(QPushButton("1"), 4, 0)
        lyt.addWidget(QPushButton("2"), 4, 1)
        lyt.addWidget(QPushButton("3"), 4, 2)
        egButton = QPushButton("=")
        # egButton.setMaximumHeight(200)
        # egButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        egButton.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        egButton.setStyleSheet("background: aqua")
        lyt.addWidget(egButton, 4, 3, 2, 1)

        lyt.addWidget(QPushButton("0"), 5, 0, 1, 2)
        lyt.addWidget(QPushButton("."), 5, 2)

        # Vertical & Horizontal alignments

        # globalLayout = QVBoxLayout()
        # globalLayout.addLayout(lyt)
        # globalLayout.addStretch(1)

        for i in range(lyt.count()):
            widget = lyt.itemAt(i).widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for r in range(lyt.rowCount()):
            lyt.setRowStretch(r, 1)
        lyt.setRowStretch(0, 3)

        self.setLayout(lyt)
