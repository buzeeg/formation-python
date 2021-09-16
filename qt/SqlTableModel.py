from PySide6.QtCore import QAbstractTableModel, Qt


class SqlTableModel(QAbstractTableModel):
    def __init__(self, input_data, headers, parent=None):
        super().__init__(parent)
        self.input_data = input_data
        self.headers = headers

    def rowCount(self, parent):
        return len(self.input_data)

    def columnCount(self, parent):
        return len(self.input_data[0])

    def headerData(self, column:int, orientation:Qt.Orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[column]
        return None

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.input_data[index.row()][index.column()]