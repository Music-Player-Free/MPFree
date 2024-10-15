from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from Collections import *
from Songs import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        layout = QHBoxLayout()

        loaded_collections = [Collection("My Playlist"), Collection("Cool Album")] #TODO: replace with a list, loaded from database
        collections = Collections()
        collections.populate(loaded_collections)

        songs = Songs()
        loaded_songs = [Song(0, "/folder/song1.mp3", "song 1", "sample", 300), Song(1, "/folder/song2.mp3", "Never Gonna Give You Up", "Rick Astley", 302)]
        songs.populate(loaded_songs)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setLayout(layout)
        layout.addWidget(collections)
        layout.addWidget(songs)
        #layout.addWidget(keybinds)

class Not_ify(QMainWindow):
    def __init__(self):
        super().__init__()

