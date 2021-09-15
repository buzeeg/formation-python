import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar
from QButtonBlock import QButtonBlock


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MegaExplorer v1.0")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)

        # Set window position
        self.move(50, 50)

        self.setCentralWidget(QButtonBlock())

        # Actions definition
        actNew = QAction(QIcon("../iconsDL/new.png"), "&New", self)
        actNew.setStatusTip("New file")
        actOpen = QAction(QIcon("../iconsDL/open.png"), "&Open...", self)
        actOpen.setShortcut("Ctrl+O")
        actOpen.setStatusTip("Open file")
        # actOpen.triggered.connect(self.open)
        actSave = QAction(QIcon("../iconsDL/save.png"), "&Save", self)
        actSave.setStatusTip("Save file")
        actSave.setShortcut("Ctrl+S")
        actExit = QAction(QIcon("../iconsDL/exit.png"), "E&xit", self)
        actExit.setShortcut("Alt+F4")
        actExit.setStatusTip("Exit app")
        actExit.triggered.connect(self.close)
        actUndo = QAction(QIcon("../iconsDL/undo.png"), "&Undo", self)
        actUndo.setStatusTip("Undo")
        actUndo.setShortcut("Ctrl+Z")
        actRedo = QAction(QIcon("../iconsDL/redo.png"), "&Redo", self)
        actRedo.setStatusTip("Redo")
        actRedo.setShortcut("Ctrl+Y")
        actCopy = QAction(QIcon("../iconsDL/copy.png"), "&Copy", self)
        actCopy.setStatusTip("Copy")
        actCopy.setShortcut("Ctrl+C")
        actCut = QAction(QIcon("../iconsDL/cut.png"), "Cu&t", self)
        actCut.setStatusTip("Cut")
        actCut.setShortcut("Ctrl+X")
        actPaste = QAction(QIcon("../iconsDL/paste.png"), "&Paste", self)
        actPaste.setStatusTip("Paste")
        actPaste.setShortcut("Ctrl+V")
        actAbout = QAction(QIcon("../iconsDL/about_(info).png"), "&About...", self)
        actAbout.setStatusTip("About")
        actAbout.triggered.connect(self.about)

        # MenuBar definition
        menuBar = self.menuBar()
        file = menuBar.addMenu("&File")
        file.setStatusTip("File menu")
        file.addAction(actNew)
        file.addSeparator()
        file.addAction(actOpen)
        file.addAction(actSave)
        file.addSeparator()
        file.addAction(actExit)
        edit = menuBar.addMenu("&Edit")
        file.setStatusTip("Edit menu")
        edit.addAction(actUndo)
        edit.addAction(actRedo)
        edit.addSeparator()
        edit.addAction(actCopy)
        edit.addAction(actCut)
        edit.addAction(actPaste)
        helpp = menuBar.addMenu("&Help")
        file.setStatusTip("Help menu")
        helpp.addAction(actAbout)

        # ToolBar definition
        toolBar1 = self.addToolBar("File Toolbar")
        toolBar1.addAction(actNew)
        toolBar1.addSeparator()
        toolBar1.addAction(actOpen)
        toolBar1.addAction(actSave)
        toolBar2 = self.addToolBar("Edit Toolbar")
        toolBar2.addAction(actUndo)
        toolBar2.addAction(actRedo)
        toolBar2.addSeparator()
        toolBar2.addAction(actCopy)
        toolBar2.addAction(actCut)
        toolBar2.addAction(actPaste)

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


if __name__ == '__main__':
    sys.argv.append("-stylesheet")
    sys.argv.append("styles.css")
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.createStatusBar()
    myWindow.show()

    sys.exit(app.exec())
