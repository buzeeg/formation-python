import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar

from CalcGridDialog import CalcGridDialog
from DBPropertiesDialog import DBPropertiesDialog
from ButtonBlock import ButtonBlock


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MegaExplorer v1.0")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)

        # Set window position
        self.move(50, 50)
        # Init attributes
        self.actNew = None
        self.actOpen = None
        self.actSave = None
        self.actExit = None
        self.actUndo = None
        self.actRedo = None
        self.actCopy = None
        self.actCut = None
        self.actPaste = None
        self.actConnect = None
        self.actCalc = None
        self.actAbout = None

        self.createActions()
        self.createMenuBar()
        self.createToolBar()
        self.createStatusBar()
        self.setCentralWidget(ButtonBlock(self))

    # Actions definition
    def createActions(self):
        self.actNew = QAction(QIcon("../iconsDL/new.png"), "&New", self)
        self.actNew.setStatusTip("New file")
        self.actOpen = QAction(QIcon("../iconsDL/open.png"), "&Open...", self)
        self.actOpen.setShortcut("Ctrl+O")
        self.actOpen.setStatusTip("Open file")
        self.actSave = QAction(QIcon("../iconsDL/save.png"), "&Save", self)
        self.actSave.setStatusTip("Save file")
        self.actSave.setShortcut("Ctrl+S")
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
        self.actConnect = QAction(QIcon("../iconsDL/SQL.png"), "&Connect", self)
        self.actConnect.setStatusTip("Connect database")
        self.actConnect.triggered.connect(self.connectDialog)
        self.actCalc = QAction(QIcon(), "C&alc", self)
        self.actCalc.setStatusTip("Launch calculator")
        self.actCalc.triggered.connect(self.calcDialog)
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
        file.addAction(self.actExit)
        edit = menuBar.addMenu("&Edit")
        file.setStatusTip("Edit menu")
        edit.addAction(self.actUndo)
        edit.addAction(self.actRedo)
        edit.addSeparator()
        edit.addAction(self.actCopy)
        edit.addAction(self.actCut)
        edit.addAction(self.actPaste)
        datab = menuBar.addMenu("&Database")
        datab.addAction(self.actConnect)
        datab.addAction(self.actCalc)
        helpp = menuBar.addMenu("&Help")
        file.setStatusTip("Help menu")
        helpp.addAction(self.actAbout)

    # ToolBar definition
    def createToolBar(self):
        toolBar1 = self.addToolBar("File Toolbar")
        toolBar1.addAction(self.actNew)
        toolBar1.addSeparator()
        toolBar1.addAction(self.actOpen)
        toolBar1.addAction(self.actSave)
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

    @Slot()
    def about(self):
        QMessageBox.about(self, "MegaExplorer", "Voici la v1")

    @Slot()
    def connectDialog(self):
        pass
        DBPropertiesDialog(self).show()

    @Slot()
    def calcDialog(self):
        CalcGridDialog(self).show()


if __name__ == '__main__':
    # sys.argv.append("-stylesheet")
    # sys.argv.append("styles.css")
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
