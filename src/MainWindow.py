from PySide6.QtWidgets import (QApplication, QDockWidget, QWidget, QLabel,
                               QMainWindow, QVBoxLayout, QHBoxLayout,
                               QStackedWidget, QPushButton, QGroupBox, QFileDialog)

from ToggleWidget import *
from Collections import *
from Keybinds import KeybindsPane
from Songs import *
from BottomBar import *
from Settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        self.setMainPage()

    def setMainPage(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        #create panes
        panes = QWidget()
        panes_layout = QHBoxLayout()
        panes.setLayout(panes_layout)

        collections = CollectionsPane()
        panes_layout.addWidget(collections)
        songs = SongsPane()
        panes_layout.addWidget(songs)
        keybinds = KeybindsPane()
        panes_layout.addWidget(keybinds)

        #create settings window
        settings = Settings()

        #add panes and settings to toggleable widget
        stacked = ToggleWidget(panes, settings)



        #create bottom bar
        bottom_bar = BottomBar(stacked)

        #add toggleable widget and bottom bar to QVBoxLayout
        layout.addWidget(stacked)
        layout.addWidget(bottom_bar)
