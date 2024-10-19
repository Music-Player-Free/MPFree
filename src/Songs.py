from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from db import SongDB

class Song(QListWidgetItem):
    '''
    Song object. \n
    Duration is a paramater passed as length of song in seconds, represented
    as integers.
    '''

    def __init__(self, **kwargs):
        super().__init__()
        # self.db_id = kwargs['db_id']

        self.path_to_file = kwargs['path_to_file']

        self.song_name = kwargs['song_name']
        self.artist = kwargs['artist']
        self.track_len = kwargs['track_len']

    def __repr__(self):
        return "Song widget "

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
            item.setText(item.song_name) # items are song objects, python interpreter knows this through the type hinting.
            self.insertItem(idx, item)

    def loadSongs(self) -> list['Song']:
        #TODO: replace with loading from DB
        db = SongDB()
        loaded = db.read_all()
        loaded_to_songs = []
        for result in loaded:
            instance = Song(path_to_file = result[0], song_name = result[1], track_len = result[2], artist = result[3])
            loaded_to_songs.append(instance)

        return loaded_to_songs


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
