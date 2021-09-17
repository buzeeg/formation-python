from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem, Qt
from PySide6.QtWidgets import QTreeView

from DatabaseManager import DatabaseManager


class DatabaseTreeModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(0, 1, parent)
        self.setHeaderData(0, Qt.Horizontal, "Database content :")

        # Get DB info
        db_manager = DatabaseManager()
        tables_names = db_manager.getAllTableNames()
        db_manager.close()

        # Load table names
        tables_item = QStandardItem("Tables")
        for table_name in tables_names:
            tables_item.appendRow([QStandardItem(table_name)])  # list because of only one column
        self.appendRow(tables_item)

        # Load views
        views_item = QStandardItem("Views")
        views_item.appendRow([QStandardItem("View 1")])
        views_item.appendRow([QStandardItem("View 2")])
        views_item.appendRow([QStandardItem("View 3")])
        self.appendRow(views_item)

        # Load stored procedures
        procs_item = QStandardItem("Stored Procedures")
        procs_item.appendRow([QStandardItem("Proc 1")])
        procs_item.appendRow([QStandardItem("Proc 2")])
        procs_item.appendRow([QStandardItem("Proc 3")])
        self.appendRow(procs_item)


class DatabaseTreeView(QTreeView):
    open_table = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModel(DatabaseTreeModel())
        self.setHeaderHidden(1)
        self.doubleClicked.connect(self.__fire_open_signal)
        self.expandAll()

    def __fire_open_signal(self, index):
        table_name = index.data(Qt.DisplayRole)
        self.open_table.emit(str(table_name))
