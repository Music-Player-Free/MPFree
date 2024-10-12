from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from Collections import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        layout = QHBoxLayout()

        loaded_collections = [Collection("thumbnail","My Playlist","artist"), Collection("thumbnail","Cool Album","artist")] #TODO: replace with a list, loaded from database
        collections = Collections()
        collections.populate(loaded_collections)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setLayout(layout)
        layout.addWidget(collections)
        #layout.addWidget(songs)
        #layout.addWidget(keybinds)
