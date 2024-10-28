from typing import List
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QStyleOptionTab, QVBoxLayout, QLabel, QListView, QWidget
from collections import defaultdict # might not need this
from functools import lru_cache

from Songs import Song, Songs
from db import CollectionDB, SongDB, Songs_Collections

# Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.
# ^^^ this is for functools.cache if we want to use that.

'''
collection needs a button
button will load songs into the songs pane
button needs to show its been clicked
'''


class Collection(QListWidgetItem):
    '''
    For playlists, albums. Extends WidgetItem. <br>
    Takes integer id and string name as input
    '''

    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs['id']

        self.name = kwargs['name']
        self.description = kwargs['description']
        self.author = kwargs['author']


class Collections(QListWidget): # Displays collections
    def __init__(self):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.songs_ref: Songs # Get a reference to Songs List Widget, given on app startup inside MainWindow.py

        self.label = QLabel("Collections")
        self.setVisible(True)

        self.populate(self.load_collections())
        self.itemClicked.connect(self.populate_from_collection)

    def set_songs_ref(self, songs: Songs): # Set reference to Songs List Widget, given on app startup inside MainWindow.py
        self.songs_ref = songs

    def populate(self, collection_list: list['Collection']):
        self.clear()
        for row, item in enumerate(collection_list):
            item.setText(item.name)
            self.insertItem(row, item)

    def populate_from_collection(self, item):
        self.songs_ref.populate(self.get_songs_from_collection(item))


    def get_songs_from_collection(self, item: Collection) -> list['Song']:
        #Get ID when item clicked
        #Get all songs with that Song-Collection Relationship
        #Create song object for each and populate collections with that

        song_list = []
        with SongDB() as db:
            id_list = Songs_Collections().read(0, [item.id]).fetchall()
            id_list = [x[0] for x in id_list]

            for row in db.read(id_list):
                kw = {col: row[i] for i, col in enumerate(db.columns)}
                inst = Song(**kw)
                song_list.append(inst)
        return song_list

    def load_collections(self) -> list['Collection']:
        # Mock list of collection objects
        load = []
        with CollectionDB() as db:
            # Read from DB
            for row in db.read_all():
                # Create collection objs
                kw = {col: row[i] for i, col in enumerate(db.columns)}
                inst = Collection(**kw)

                # add to list
                load.append(inst)
        return load

class CollectionsPane(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Get collections
        self.collections = Collections()
        # Set label for widget
        label = QLabel()
        label.setText("Collections")

        # Add label and widget to layout
        layout.addWidget(label)
        layout.addWidget(self.collections)

        # apply layout to instance of Collections pane (self)
        self.setLayout(layout)
