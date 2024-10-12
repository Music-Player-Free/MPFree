from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from Collections import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        layout = QHBoxLayout()

        loaded_collections = [Collection("thumbnail","name","artist"), Collection("thumbnail","name","artist")] #TODO: replace with a list, loaded from database
        collections = Collections()
        collections.populate(loaded_collections)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addWidget(collections)
        self.setLayout(layout)
        #layout.addWidget(songs)
        #layout.addWidget(keybinds)
