from PySide6.QtWidgets import (QApplication, QDockWidget, QWidget, QLabel,
                               QMainWindow, QVBoxLayout, QHBoxLayout,
                               QStackedWidget, QPushButton, QGroupBox, QFileDialog)

from ToggleWidget import *
from Keybinds import KeybindsPane
from BottomBar import *
from Settings import Settings
from Collections import *
from Songs import *

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
        collections.collections.set_songs_ref(songs.songs) # Should consider renaming this. First songs is the pane,
                                                           # second is the real Songs class. Same with collections.collections
        keybinds = KeybindsPane()
        settings = Settings()
        settings.file_widget.refreshReady.connect(
            lambda : songs.songs.populate(songs.songs.load_all_songs()))
        settings.file_widget.refreshReady.connect(
            lambda : collections.collections.populate(collections.collections.load_collections()))

        stacked = ToggleWidget(songs, settings)

        panes_layout.addWidget(collections)
        panes_layout.addWidget(stacked)
        panes_layout.addWidget(keybinds)

        panes.setLayout(panes_layout)

        #create settings window

        #add panes and settings to toggleable widget

        #create bottom bar
        bottom_bar = BottomBar(stacked)
        bottom_bar.media_controls.set_songs_ref(songs.songs)
        songs.songs.itemClicked.connect(bottom_bar.media_controls.set_current_song)

        #add toggleable widget and bottom bar to QVBoxLayout
        layout.addWidget(panes)
        layout.addWidget(bottom_bar)
