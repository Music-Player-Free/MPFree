from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from Collections import *
from Keybinds import KeybindsPane
from Songs import *
from BottomBar import *

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

        panes = QWidget()
        panes_layout = QHBoxLayout()
        panes.setLayout(panes_layout)

        #create panes
        collections = CollectionsPane()
        panes_layout.addWidget(collections)

        songs = SongsPane()
        panes_layout.addWidget(songs)

        keybinds = KeybindsPane()
        panes_layout.addWidget(keybinds)

        #create bottom bar
        bottom_bar = BottomBar()

        #add widgets to QVBoxLayout
        layout.addWidget(panes)
        layout.addWidget(bottom_bar)



class Not_ify(QMainWindow):
    def __init__(self):
        super().__init__()
