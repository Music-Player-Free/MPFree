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
    **TODO**
    '''
    def __init__(self):
        super().__init__()

        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Songs")
        self.setVisible(True)

        self.populate(self.loadSongs())

    def populate(self, songList: list['Song']):
        '''
        Set text for songs (base class ItemWidgets) and insert into self.
        '''
        self.clear()
        for row, item in enumerate(songList):
            item.setText(item.title)
            self.insertItem(row, item)

    def loadSongs(self) -> list['Song']:
        #TODO: replace with loading from DB
        loaded_songs = [Song(0, "/folder/song1.mp3", "song 1", "sample", 300), Song(1, "/folder/song2.mp3", "Never Gonna Give You Up", "Rick Astley", 302)]
        return loaded_songs


class SongsPane(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        songs = Songs()
        label = QLabel()
        label.setText("Songs")

        layout.addWidget(label)
        layout.addWidget(songs)
