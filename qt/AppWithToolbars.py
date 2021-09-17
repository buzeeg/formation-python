import sys

from PySide6.QtCore import Slot, QDir
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QTabWidget, QSplitter, QTreeView, \
    QMdiArea, QInputDialog, QFileDialog, QFileSystemModel

from DatabaseTreeModel import DatabaseTreeView
from SqlTableView import SqlTableView
from CalcGridDialog import CalcGridDialog
from DBPropertiesDialog import DBPropertiesDialog
from ButtonBlock import ButtonBlock
from MdiSubWindow import MdiSubWindow
from RGBSelectorDialog import RGBSelectorDialog


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MegaExplorer v1.0")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)

        # Set window position
        self.move(50, 50)

        self.__mdiArea = None

        # Init attributes
        self.actNew = None
        self.actOpen = None
        self.actSave = None
        self.actClose = None
        self.actExit = None
        self.actUndo = None
        self.actRedo = None
        self.actCopy = None
        self.actCut = None
        self.actPaste = None
        self.actDisplayCasc = None
        self.actDisplayTile = None
        self.actDisplayTab = None
        self.actConnect = None
        self.actCalc = None
        self.actRGB = None
        self.actAbout = None

        self.createActions()
        self.createMenuBar()
        self.createToolBar()
        self.createStatusBar()

        # self.setCentralWidget(ButtonBlock(self))
        self.createContent()

    # Actions definition
    def createActions(self):
        self.actNew = QAction(QIcon("../iconsDL/new.png"), "&New", self)
        self.actNew.setStatusTip("New file")
        self.actNew.triggered.connect(self.newDoc)
        self.actOpen = QAction(QIcon("../iconsDL/open.png"), "&Open...", self)
        self.actOpen.setShortcut("Ctrl+O")
        self.actOpen.setStatusTip("Open file")
        self.actOpen.triggered.connect(self.openDoc)
        self.actSave = QAction(QIcon("../iconsDL/save.png"), "&Save", self)
        self.actSave.setStatusTip("Save file")
        self.actSave.setShortcut("Ctrl+S")
        self.actClose = QAction(QIcon("../iconsDL/cancel.png"), "&Close", self)
        self.actClose.setStatusTip("Close file")
        self.actClose.triggered.connect(self.closeDoc)
        self.actExit = QAction(QIcon("../iconsDL/exit.png"), "E&xit", self)
        self.actExit.setShortcut("Alt+F4")
        self.actExit.setStatusTip("Exit app")
        self.actExit.triggered.connect(self.close)
        self.actUndo = QAction(QIcon("../iconsDL/undo.png"), "&Undo", self)
        self.actUndo.setStatusTip("Undo")
        self.actUndo.setShortcut("Ctrl+Z")
        self.actRedo = QAction(QIcon("../iconsDL/redo.png"), "&Redo", self)
        self.actRedo.setStatusTip("Redo")
        self.actRedo.setShortcut("Ctrl+Y")
        self.actCopy = QAction(QIcon("../iconsDL/copy.png"), "&Copy", self)
        self.actCopy.setStatusTip("Copy")
        self.actCopy.setShortcut("Ctrl+C")
        self.actCut = QAction(QIcon("../iconsDL/cut.png"), "Cu&t", self)
        self.actCut.setStatusTip("Cut")
        self.actCut.setShortcut("Ctrl+X")
        self.actPaste = QAction(QIcon("../iconsDL/paste.png"), "&Paste", self)
        self.actPaste.setStatusTip("Paste")
        self.actPaste.setShortcut("Ctrl+V")
        self.actDisplayCasc = QAction(QIcon(""), "Cascade", self)
        self.actDisplayCasc.triggered.connect(self.displayCasc)
        self.actDisplayTile = QAction(QIcon(""), "Tile", self)
        self.actDisplayTile.triggered.connect(self.displayTile)
        self.actDisplayTab = QAction(QIcon(""), "Tab", self)
        self.actDisplayTab.triggered.connect(self.displayTab)
        self.actConnect = QAction(QIcon("../iconsDL/SQL.png"), "&Connect", self)
        self.actConnect.setStatusTip("Connect database")
        self.actConnect.triggered.connect(self.connectDialog)
        self.actCalc = QAction(QIcon(), "C&alc", self)
        self.actCalc.setStatusTip("Launch calculator")
        self.actCalc.triggered.connect(self.calcDialog)
        self.actRGB = QAction(QIcon(), "&RGB Selector", self)
        self.actRGB.setStatusTip("Launch RGB selector")
        self.actRGB.triggered.connect(self.rgbDialog)
        self.actAbout = QAction(QIcon("../iconsDL/about_(info).png"), "&About...", self)
        self.actAbout.setStatusTip("About")
        self.actAbout.triggered.connect(self.about)

    # MenuBar definition
    def createMenuBar(self):
        menuBar = self.menuBar()
        file = menuBar.addMenu("&File")
        file.setStatusTip("File menu")
        file.addAction(self.actNew)
        file.addSeparator()
        file.addAction(self.actOpen)
        file.addAction(self.actSave)
        file.addSeparator()
        file.addAction(self.actClose)
        file.addSeparator()
        file.addAction(self.actExit)
        edit = menuBar.addMenu("&Edit")
        edit.setStatusTip("Edit menu")
        edit.addAction(self.actUndo)
        edit.addAction(self.actRedo)
        edit.addSeparator()
        edit.addAction(self.actCopy)
        edit.addAction(self.actCut)
        edit.addAction(self.actPaste)
        display = menuBar.addMenu("&Display")
        display.setStatusTip("Display menu")
        display.addAction(self.actDisplayCasc)
        display.addAction(self.actDisplayTile)
        display.addSeparator()
        display.addAction(self.actDisplayTab)
        op = menuBar.addMenu("&Operations")
        op.addAction(self.actConnect)
        op.addAction(self.actCalc)
        op.addAction(self.actRGB)
        helpp = menuBar.addMenu("&Help")
        helpp.setStatusTip("Help menu")
        helpp.addAction(self.actAbout)

    # ToolBar definition
    def createToolBar(self):
        toolBar1 = self.addToolBar("File Toolbar")
        toolBar1.addAction(self.actNew)
        toolBar1.addSeparator()
        toolBar1.addAction(self.actOpen)
        toolBar1.addAction(self.actSave)
        toolBar1.addSeparator()
        toolBar1.addAction(self.actClose)
        toolBar2 = self.addToolBar("Edit Toolbar")
        toolBar2.addAction(self.actUndo)
        toolBar2.addAction(self.actRedo)
        toolBar2.addSeparator()
        toolBar2.addAction(self.actCopy)
        toolBar2.addAction(self.actCut)
        toolBar2.addAction(self.actPaste)

    # StatusBar definition
    def createStatusBar(self):
        status_bar = self.statusBar()
        status_bar.showMessage("Example of MenuBar with Python & Qt")
        progress = QProgressBar()
        # QProgressBar.setMaximumHeight(progress, 2)
        progress.setMaximumHeight(10)
        progress.setMaximumWidth(200)
        progress.setValue(66)
        status_bar.addPermanentWidget(progress)

    # Content definition
    def createContent(self):
        # MDI area
        self.__mdiArea = QMdiArea()

        # Navigation area
        file_model = QFileSystemModel()
        file_model.setRootPath(QDir().currentPath())
        file_tree_view = QTreeView()
        file_tree_view.setModel(file_model)

        database_view = DatabaseTreeView()
        database_view.open_table.connect(self.showTable)

        tabWidget = QTabWidget()
        tabWidget.setTabPosition(QTabWidget.South)
        tabWidget.setMinimumWidth(220)
        tabWidget.addTab(file_tree_view, "File System")
        tabWidget.addTab(database_view, "Database")
        tabWidget.addTab(ButtonBlock(self), "Buttons")
        tabWidget.setCurrentIndex(1)

        # Top container
        splitter = QSplitter()
        splitter.addWidget(tabWidget)
        splitter.addWidget(self.__mdiArea)
        self.setCentralWidget(splitter)

    @Slot()
    def newDoc(self):
        text, ok = QInputDialog.getText(self, "New doc", "Enter doc name:")
        if ok:
            doc1 = SqlTableView()
            # doc1 = MdiSubWindow(text, self)
            self.__mdiArea.addSubWindow(doc1)
            doc1.show()

    @Slot()
    def openDoc(self):
        filenameInfos = QFileDialog.getOpenFileName(self, "Open file", "/home")
        # QMessageBox.information(self, "Fichier choisi", str(filenameInfos))

        filename = filenameInfos[0]
        if len(filename.strip()) > 0:
            try:
                doc1 = MdiSubWindow(filename, self)
                with open(filename, "r") as f:
                    doc1.setText(f.read())
                self.__mdiArea.addSubWindow(doc1)
                doc1.show()
            except OSError:
                QMessageBox.information(self, "File error", "File " + filename + " cannot be opened")
            except ValueError:
                QMessageBox.information(self, "File error", "File " + filename + " cannot be read")

    @Slot(str)
    def showTable(self, tableName):
        table = SqlTableView(tableName)
        self.__mdiArea.addSubWindow(table)
        table.show()

    @Slot()
    def closeDoc(self):
        self.__mdiArea.closeActiveSubWindow()

    @Slot()
    def displayCasc(self):
        self.__mdiArea.setViewMode(QMdiArea.SubWindowView)
        self.__mdiArea.cascadeSubWindows()

    @Slot()
    def displayTile(self):
        self.__mdiArea.setViewMode(QMdiArea.SubWindowView)
        self.__mdiArea.tileSubWindows()

    @Slot()
    def displayTab(self):
        self.__mdiArea.setViewMode(QMdiArea.TabbedView)

    @Slot()
    def about(self):
        QMessageBox.about(self, "MegaExplorer", "Voici la v1")

    @Slot()
    def connectDialog(self):
        DBPropertiesDialog(self).show()

    @Slot()
    def calcDialog(self):
        CalcGridDialog(self).show()

    @Slot()
    def rgbDialog(self):
        RGBSelectorDialog(self).show()

    # Override windows closeEvent
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure you wanna quiiiit??",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # sys.argv.append("-stylesheet")
    # sys.argv.append("styles.css")
    # sys.argv.append("-style")
    # sys.argv.append("fusion")
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
