from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import QTableView

from DatabaseManager import DatabaseManager
from SqlTableModel import SqlTableModel


# headers = ["Col1", "Col2", "Col3", "Col4", "Col5"]
# data = [
#     [10, 20, 30, 40, 50],
#     [20, 10, 30, 70, 50],
#     [30, 20, 50, 40, 20],
#     [40, 30, 30, 80, 30],
#     [50, 40, 60, 40, 40]
# ]


class SqlTableView(QTableView):
    def __init__(self, tableName):
        super().__init__()

        # Get DB info
        db_manager = DatabaseManager()
        table = db_manager.getTableData(tableName)
        db_manager.close()

        # Check if empty table
        if table is not None \
                and len(table[0]) > 0 \
                and len(table[1]) > 0:
            model = SqlTableModel(table[1], table[0])

            # Proxy model for sort
            proxyModel = QSortFilterProxyModel()
            proxyModel.setSourceModel(model)
            
            self.setModel(proxyModel)
            self.setSortingEnabled(True)

        self.setWindowTitle("Mes datas")
        self.resize(400, 300)
