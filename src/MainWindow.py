from PySide6.QtWidgets import (QApplication, QDockWidget, QWidget, QLabel,
                               QMainWindow, QVBoxLayout, QHBoxLayout,
                               QStackedWidget, QPushButton, QGroupBox, QFileDialog)

from ToggleWidget import *
from Keybinds import KeybindsPane
from BottomBar import *
from Settings import Settings
from panes import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        self.setMainPage()

    def setMainPage(self):
        layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        #create panes
        panes = QWidget()
        panes_layout = QHBoxLayout()

        collections = CollectionsPane()
        songs = SongsPane()
        keybinds = KeybindsPane()

        panes_layout.addWidget(collections)
        panes_layout.addWidget(songs)
        panes_layout.addWidget(keybinds)
        
        panes.setLayout(panes_layout)


        #create settings window
        settings = Settings()

        #add panes and settings to toggleable widget
        stacked = ToggleWidget(panes, settings)



        #create bottom bar
        bottom_bar = BottomBar(stacked)

        #add toggleable widget and bottom bar to QVBoxLayout
        layout.addWidget(stacked)
        layout.addWidget(bottom_bar)
