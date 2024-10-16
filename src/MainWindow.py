from PySide6.QtWidgets import (QApplication, QDockWidget, QWidget, QLabel,
                               QMainWindow, QVBoxLayout, QHBoxLayout,
                               QStackedWidget, QPushButton, QGroupBox, QFileDialog)

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
        self.label = QLabel("MPFree Music Player")
        
        # loaded_collections = [Collection(0,"My Playlist"), Collection(1, "Cool Album")] # TODO: replace with a list, loaded from database
        # collections = Collections()
        # collections.populate(loaded_collections)

        songs = Songs()
        loaded_songs = [Song(0, "/folder/song1.mp3", "song 1", "sample", 300), Song(1, "/folder/song2.mp3", "Never Gonna Give You Up", "Rick Astley", 302)]
        songs.populate(loaded_songs)
        
        # Vertical layout.
        layout = QVBoxLayout()


        
        # Set background "outline" widget
        outline_widget = QGroupBox()

        settings = QWidget()


        # TODO:
        # resize button
        # add text input also.
        file_button = QPushButton("Choose source folder")
        file_button.clicked.connect(self.button_file)

        

        layout2 = QVBoxLayout()
        layout2.addWidget(file_button)
        settings.setLayout(layout2)

        # Create button to swap stack
        button = QPushButton("here")
        button.clicked.connect(self.clickable)

        # Create stacked widget for songs/collections
        stacked = QStackedWidget()
        stacked.addWidget(songs)
        stacked.addWidget(settings)

        layout.addWidget(button)
        layout.addWidget(stacked)


        outline_widget.setLayout(layout) # apply vertical layout to this also
        self.setCentralWidget(outline_widget)  # set as central widget for others to reside in.
        

        # TODO
        # THIS IS BAD BROS OMG !!!!1! 
        # No dynamicism, hard-coded.
        self.widgets = {}
        self.widgets['settings'] = stacked.indexOf(settings)
        self.widgets['songs'] = stacked.indexOf(songs)
        # self.widgets['collections'] = stacked.indexOf(collections)
       
    def button_file(self):
        dialog = QFileDialog()
        file = dialog.getExistingDirectory(None, "Choose folder")
        return file

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
