from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, \
    QComboBox, QCheckBox


class DBPropertiesDialog(QDialog):
    db_ports_sqlite3 = "Sqlite3"
    db_ports = {db_ports_sqlite3: None, "MySql": 3306, "Oracle": 1748, "MSQLServer": 1433}

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

        # Widgets creation
        self.__txt_type = QComboBox()
        self.__txt_type.addItems(self.db_ports.keys())
        self.__txt_type.currentIndexChanged.connect(self.on_db_type_changed)
        self.__txt_host = QLineEdit()
        self.__txt_host.textChanged.connect(self.on_text_changed)
        self.__txt_port = QSpinBox()
        self.__txt_port.setMinimum(1_024)
        self.__txt_port.setMaximum(65_535)
        self.__txt_database = QLineEdit()
        self.__txt_database.textChanged.connect(self.on_text_changed)
        self.__txt_login = QLineEdit()
        self.__txt_login.textChanged.connect(self.on_text_changed)
        self.__txt_password = QLineEdit()
        self.__txt_password.setEchoMode(QLineEdit.Password)
        self.__autocommit = QCheckBox("Auto connect")
        self.__pingbutton = QPushButton("Ping Database")

        # Init inputs from Slots
        self.__txt_type.currentIndexChanged.emit(0)
        self.on_text_changed()

        # Layout creation
        ping_layout = QHBoxLayout()
        ping_layout.addWidget(self.__autocommit)
        ping_layout.addWidget(self.__pingbutton)

        form_layout = QFormLayout()
        form_layout.addRow("&Type:", self.__txt_type)
        form_layout.addRow("&Host:", self.__txt_host)
        form_layout.addRow("&Port:", self.__txt_port)
        form_layout.addRow("&Database name:", self.__txt_database)
        form_layout.addRow("&Login:", self.__txt_login)
        form_layout.addRow("Pass&word:", self.__txt_password)
        form_layout.addRow(ping_layout)

        btnLayout = QHBoxLayout()
        btnLayout.addStretch(1)
        btnLayout.addWidget(ok)
        btnLayout.addWidget(cancel)

        globalLayout = QVBoxLayout()
        globalLayout.addLayout(form_layout)
        globalLayout.addStretch(1)
        globalLayout.addLayout(btnLayout)
        self.setLayout(globalLayout)

    # Slot definitions
    @Slot(int)
    def on_db_type_changed(self, index):
        key = self.__txt_type.itemText(index)
        value = self.db_ports[key]

        if key == self.db_ports_sqlite3:
            self.__txt_host.setEnabled(False)
            self.__txt_port.setEnabled(False)
            self.__txt_login.setEnabled(False)
            self.__txt_password.setEnabled(False)
            self.__pingbutton.setEnabled(False)
        else:
            self.__txt_host.setEnabled(True)
            self.__txt_port.setEnabled(True)
            self.__txt_login.setEnabled(True)
            self.__txt_password.setEnabled(True)
            # Update port value
            self.__txt_port.setValue(value)
            # Update ping button from text values
            self.on_text_changed()

    @Slot(str)
    def on_text_changed(self):
        ping_status = (self.__txt_host.text().strip() != "" or not self.__txt_host.isEnabled()) \
                and (self.__txt_database.text().strip() != "" or not self.__txt_database.isEnabled()) \
                and (self.__txt_login.text().strip() != "" or not self.__txt_login.isEnabled())
        self.__pingbutton.setEnabled(ping_status)

    @Slot()
    def okSlot(self):
        confJson = {
            "type": str(self.__txt_type.currentText().strip()),
            "host": str(self.__txt_host.text().strip()),
            "port": str(self.__txt_port.text().strip()),
            "database": str(self.__txt_database.text().strip()),
            "login": str(self.__txt_login.text().strip()),
            "password": str(self.__txt_password.text().strip()),
        }
        print(confJson)

    @Slot()
    def cancelSlot(self):
        self.close()
        print("cancel")
