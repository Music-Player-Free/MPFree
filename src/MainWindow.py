from PySide6.QtWidgets import (QApplication, QDockWidget, QWidget, QLabel,
                               QMainWindow, QVBoxLayout, QHBoxLayout,
                               QStackedWidget, QPushButton)

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
        self.label = QLabel("MPFree Music Player")
        
        loaded_collections = [Collection("My Playlist"), Collection("Cool Album")] # TODO: replace with a list, loaded from database
        collections = Collections()
        collections.populate(loaded_collections)

        songs = Songs()
        loaded_songs = [Song(0, "/folder/song1.mp3", "song 1", "sample", 300), Song(1, "/folder/song2.mp3", "Never Gonna Give You Up", "Rick Astley", 302)]
        songs.populate(loaded_songs)

        # Vertical layout.
        layout = QVBoxLayout()
        
        # Set background "outline" widget
        outline_widget = QWidget()
        outline_widget.setLayout(layout) # apply vertical layout to this also
        self.setCentralWidget(outline_widget)  # set as central widget for others to reside in.

        # Create button to swap stack
        button = QPushButton("here")
        button.clicked.connect(self.clickable)
        layout.addWidget(button)

        # Create stacked widget for songs/collections
        stacked = QStackedWidget()
        stacked.addWidget(songs)
        stacked.addWidget(collections)

        layout.addWidget(stacked)


        # self.setCentralWidget(stacked)
        
        # TODO
        # THIS IS BAD BROS OMG !!!!1! 
        # No dynamicism, hard-coded.
        self.widgets = {}
        self.widgets['collections'] = stacked.indexOf(collections)
        self.widgets['songs'] = stacked.indexOf(songs)


        print(self.widgets)
        


    def clickable(self):
        widgets = self.centralWidget().children()
        stacked = None
        for widget in widgets:
            if isinstance(widget, QStackedWidget):
                stacked = widget
        if not stacked:
            print('YER FUCKED')
            #TODO throw error
        else:
            # Swap state
            stacked.setCurrentIndex((stacked.currentIndex() + 1) % 2)
