import sys
import datetime

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MegaExplorer v1.0")
        self.setWindowIcon(QIcon("../iconsDL/new.png"))
        self.resize(800, 600)

        # Set window position
        self.move(50, 50)

        # Create buttons
        self.__button1 = QPushButton("Button 1", self)
        self.__button1.setGeometry(10, 210, 200, 30)
        self.__button1.clicked.connect(self.slot1)
        self.__button2 = QPushButton("Button 2", self)
        self.__button2.setGeometry(10, 250, 200, 30)
        self.__button2.clicked.connect(self.slot2)

        # Display
        self.__label1 = QLabel(self)
        self.__label1.setGeometry(220, 210, 200, 30)
        self.__label1.setText(f"{datetime.datetime.now()}")

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
        self.statusBar().showMessage("Example of MenuBar with Python & Qt")

    # Define slots to connect signals
    @Slot()
    def slot1(self):
        self.__label1.setText(f"{datetime.datetime.now()}")

    @Slot()
    def slot2(self):
        QMessageBox.information(self, "MegaExplorer", "Coucou")

    @Slot()
    def about(self):
        QMessageBox.about(self, "MegaExplorer", "Voici la v1")


if __name__ == '__main__':
    sys.argv.append("-stylesheet")
    sys.argv.append("styles.css")
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
