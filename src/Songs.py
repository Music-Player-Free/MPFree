from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

class Song(QListWidgetItem):
    '''
    Song object. \n
    Duration is a paramater passed as length of song in seconds, represented
    as integers.
    '''
    def __init__(self, db_id: int, path_to_file: str, title: str, artist: str, duration: int):
        super().__init__()
        self.db_id = db_id

        self.path_to_file = path_to_file

        self.title = title
        self.artist = artist
        self.duration = duration

class Songs(QListWidget):
    '''
    ### TODO
    '''
    def __init__(self, spacing=5, wrapping=True):
        super().__init__()

        # Songs object extends list widget, and given spacing and wrapping properties
        self.setSpacing(spacing)
        self.setWrapping(wrapping)

        # Create label and apply to self
        self.label = QLabel("Songs")
        self.setVisible(True)

        # Populate songs
        self.populate(self.loadSongs())


    def populate(self, songList: list['Song']):
        '''
        Set text for songs (base class ItemWidgets) and insert into self.
        '''
        # Ensure listwidget is empty
        self.clear()

        # Enumerate through list of song objects and populate self (ListWidget)
        for idx, item in enumerate(songList):
            item.setText(item.title) # items are song objects, python interpreter knows this through the type hinting.
            self.insertItem(idx, item)

    def loadSongs(self) -> list['Song']:
        #TODO: replace with loading from DB
        loaded_songs = [Song(0, "/folder/song1.mp3", "song 1", "sample", 300), Song(1, "/folder/song2.mp3", "Never Gonna Give You Up", "Rick Astley", 302)]
        return loaded_songs


class SongsPane(QWidget):
    def __init__(self):
        super().__init__()

        # Init layout type V(ertical)Box
        layout = QVBoxLayout()

        # Create label for songs.
        label = QLabel()
        label.setText("Songs")

        # Create Songs object (extends ListWidget)
        songs = Songs()
        
        # Add widgets to the layout (following (V)ertical box format)
        layout.addWidget(label)
        layout.addWidget(songs)

        # Apply layout to instantiated widget (self)
        self.setLayout(layout)
