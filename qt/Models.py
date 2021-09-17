import sys

from PySide6.QtCore import QItemSelectionModel, QItemSelection, Slot
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableView, QListView, QTreeView, QHBoxLayout

dict_of_dicts = {
    'dict1': {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'},
    'dict2': {'k4': 'v4'},
    'dict3': {'k5': 'v5', 'k6': 'v6', 'k7': 'v7'},
}


def create_model_from_dict(d, parent=None):
    model = QStandardItemModel(0, 2, parent)
    for k, v in dict_of_dicts.items():
        it = QStandardItem(k)
        model.appendRow(it)
        for k2, v2 in v.items():
            it.appendRow([QStandardItem(k2), QStandardItem(v2)])
    return model


class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        model = create_model_from_dict(dict_of_dicts, self)

        self.listview = QListView()
        self.listview.setModel(model)

        self.tableview = QTableView()
        self.tableview.setModel(model)

        self.treeview = QTreeView()
        self.treeview.setModel(model)
        self.treeview.expandAll()

        hbox = QHBoxLayout()
        hbox.addWidget(self.listview)
        hbox.addWidget(self.tableview)
        hbox.addWidget(self.treeview)

        self.listview.selectionModel().selectionChanged.connect(self.handleSelectionChanged)
        self.listview.selectionModel().select(model.index(0, 0), QItemSelectionModel.Select)

        centralWidget = QWidget()
        centralWidget.setLayout(hbox)
        self.setCentralWidget(centralWidget)

    @Slot(QItemSelection)
    def handleSelectionChanged(self, item):
        ixs = item.indexes()
        if ixs:
            self.tableview.setRootIndex(ixs[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
