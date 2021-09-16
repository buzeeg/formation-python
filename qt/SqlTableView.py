from PySide6.QtWidgets import QTableView
from SqlTableModel import SqlTableModel


headers = ["Col1", "Col2", "Col3", "Col4", "Col5"]
data = [
    [10, 20, 30, 40, 50],
    [20, 10, 30, 70, 50],
    [30, 20, 50, 40, 20],
    [40, 30, 30, 80, 30],
    [50, 40, 60, 40, 40]
]


class SqlTableView(QTableView):
    def __init__(self):
        super().__init__()
        model = SqlTableModel(data, headers)
        self.setModel(model)

        self.setWindowTitle("Mes datas")
        self.resize(400, 300)
