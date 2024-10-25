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
    def __init__(self, songs_ref: Songs):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)

        self.label = QLabel("Collections")
        self.setVisible(True)

        self.populate(self.load_collections())
        self.itemClicked.connect(popu)

    def populate(self, collection_list: list['Collection']):
        self.clear()
        for row, item in enumerate(collection_list):
            item.setText(item.name)
            self.insertItem(row, item)

    def get_songs_from_collection(self, item: Collection) -> list['Song']: # This could be just id?
        #Get ID when item clicked
        #Get all songs with that Song-Collection Relationship
        #Create song object for each and populate collections with that

        song_list = [Song()]
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
