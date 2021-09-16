import statistics

from PySide6.QtCore import Slot
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QSpinBox, \
    QSlider, QLabel


class RGBSelectorDialog(QDialog):
    COLOR_MIN_VALUE = 0
    COLOR_MAX_VALUE = 255

    def __init__(self, parent):
        super().__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle("RGB selector - " + parent.windowTitle())
        self.setModal(True)

        # Create buttons
        ok = QPushButton("Ok")
        ok.clicked.connect(self.okSlot)
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.cancelSlot)

        # self.__red = RGBSelectorDialog.COLOR_MIN_VALUE
        # self.__green = RGBSelectorDialog.COLOR_MAX_VALUE
        # self.__blue = RGBSelectorDialog.COLOR_MIN_VALUE

        # Widgets creation
        self.__red_slider = QSlider(Qt.Horizontal, self)
        self.__red_slider.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__red_slider.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)
        self.__red_spinbox = QSpinBox()
        self.__red_spinbox.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__red_spinbox.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)

        self.__green_slider = QSlider(Qt.Horizontal, self)
        self.__green_slider.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__green_slider.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)
        self.__green_slider.setValue(RGBSelectorDialog.COLOR_MAX_VALUE)
        self.__green_spinbox = QSpinBox()
        self.__green_spinbox.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__green_spinbox.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)
        self.__green_spinbox.setValue(RGBSelectorDialog.COLOR_MAX_VALUE)

        self.__blue_slider = QSlider(Qt.Horizontal, self)
        self.__blue_slider.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__blue_slider.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)
        self.__blue_spinbox = QSpinBox()
        self.__blue_spinbox.setMinimum(RGBSelectorDialog.COLOR_MIN_VALUE)
        self.__blue_spinbox.setMaximum(RGBSelectorDialog.COLOR_MAX_VALUE)

        # Slot connections
        self.__red_slider.valueChanged.connect(self.__red_spinbox.setValue)
        self.__red_spinbox.valueChanged.connect(self.__red_slider.setValue)
        self.__green_slider.valueChanged.connect(self.__green_spinbox.setValue)
        self.__green_spinbox.valueChanged.connect(self.__green_slider.setValue)
        self.__blue_slider.valueChanged.connect(self.__blue_spinbox.setValue)
        self.__blue_spinbox.valueChanged.connect(self.__blue_slider.setValue)
        self.__red_slider.valueChanged.connect(self.valueChanged)
        self.__green_slider.valueChanged.connect(self.valueChanged)
        self.__blue_slider.valueChanged.connect(self.valueChanged)

        # Layout creation
        red_lyt = QHBoxLayout()
        red_lyt.addWidget(self.__red_slider)
        red_lyt.addWidget(self.__red_spinbox)
        green_lyt = QHBoxLayout()
        green_lyt.addWidget(self.__green_slider)
        green_lyt.addWidget(self.__green_spinbox)
        blue_lyt = QHBoxLayout()
        blue_lyt.addWidget(self.__blue_slider)
        blue_lyt.addWidget(self.__blue_spinbox)

        form_layout = QFormLayout()
        form_layout.addRow("Red:", red_lyt)
        form_layout.addRow("Green:", green_lyt)
        form_layout.addRow("Blue:", blue_lyt)

        btnLayout = QHBoxLayout()
        btnLayout.addStretch(1)
        btnLayout.addWidget(ok)
        btnLayout.addWidget(cancel)

        self.__color_widget = QLabel()
        self.valueChanged()

        globalLayout = QVBoxLayout()
        globalLayout.addLayout(form_layout)
        globalLayout.addWidget(self.__color_widget, 1)
        globalLayout.addLayout(btnLayout)
        self.setLayout(globalLayout)

    # Slot definitions
    @Slot()
    def valueChanged(self):
        red = self.__red_slider.value()
        green = self.__green_slider.value()
        blue = self.__blue_slider.value()
        color = f'{red},{green},{blue}'

        # textcolo = f'{255-red},{255-green},{255-blue}'
        textcolo = "white" if statistics.mean([red, green, blue]) < 128 else "black"

        self.__color_widget.setText(color)
        self.__color_widget.setAlignment(Qt.AlignCenter)
        self.__color_widget.setStyleSheet("background: rgb(" + color + "); color: " + textcolo)

    @Slot()
    def okSlot(self):
        self.close()

    @Slot()
    def cancelSlot(self):
        self.close()
