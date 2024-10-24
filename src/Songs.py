from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from db import SongDB

# M̶o̶v̶e̶ ̶g̶e̶n̶e̶r̶a̶t̶e̶k̶w̶a̶r̶g̶s̶ ̶s̶o̶m̶e̶w̶h̶e̶r̶e̶ // removed completely, use dict comp from now on, will specify in main.py
#̶ ̶r̶e̶p̶l̶a̶c̶e̶ ̶'̶s̶e̶l̶e̶c̶t̶ ̶*̶ ̶f̶r̶o̶m̶ ̶?̶'̶ ̶w̶i̶t̶h̶ ̶'̶s̶e̶l̶e̶c̶t̶ ̶(̶c̶o̶l̶1̶,̶ ̶c̶o̶l̶2̶)̶
#̶ ̶F̶i̶g̶u̶r̶e̶ ̶o̶u̶t̶ ̶w̶h̶a̶t̶ ̶t̶o̶ ̶d̶o̶ ̶w̶i̶t̶h̶ ̶i̶d̶
#̶ ̶L̶o̶a̶d̶ ̶w̶i̶t̶h̶o̶u̶t̶ ̶I̶D̶,̶ ̶
#̶ ̶q̶u̶e̶r̶y̶ ̶d̶b̶ ̶t̶o̶ ̶i̶n̶s̶t̶a̶n̶t̶i̶a̶t̶e̶ ̶o̶b̶j̶ ̶w̶i̶t̶h̶ ̶l̶a̶s̶t̶R̶o̶w̶I̶D̶
# i̶m̶p̶l̶e̶m̶e̶n̶t̶ ̶a̶l̶l̶ ̶t̶a̶b̶l̶e̶s̶

class Song(QListWidgetItem):
    '''
    Song object. \n
    Duration is a paramater passed as length of song in seconds, represented
    as integers. 
    '''

    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs['id']

        self.path_to_file = kwargs['path_to_file']

        self.song_name = kwargs['song_name']
        self.artist = kwargs['artist']
        self.track_len = kwargs['track_len']

    def __repr__(self):
        return "Song widget {}".format(self.id)


class Songs(QListWidget):
    '''
    # TODO 
    docstring
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
        # self.populate(self.load_songs())


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


    def load_songs(self) -> list['Song']:
        loaded_to_songs = []

        with SongDB() as sdb:
            for result in sdb.read_all():
                kw = {col: result[i] for i, col in enumerate(sdb.columns)}
                instance = Song(**kw)
                loaded_to_songs.append(instance)

        return loaded_to_songs
