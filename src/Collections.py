from PySide6.QtWidgets import QListWidget, QListWidgetItem, QStyleOptionTab, QVBoxLayout, QLabel, QListView, QWidget
from collections import defaultdict # might not need this
from functools import lru_cache

from db import CollectionDB

# Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.
# ^^^ this is for functools.cache if we want to use that.

'''
CollectionS (widget) will poulate itself with ALL collections of the db.
collections -> populate -> load db -> create collection using id gathered

populate:
    create db instance
    res = readall()
    for row in res:
        create widget (input=row)
        self(coll).append new coll widget


'''


class Collection(QListWidgetItem): 
    '''
    For playlists, albums. Extends WidgetItem. <br>
    Takes integer id and string name as input
    '''

    def __init__(self, db_id: int, name: str):
        super().__init__()
        self.name = name



class Collections(QListWidget): # Displays collections
    def __init__(self, spacing:int = 5, wrapping:bool = True):
        super().__init__()
        self.setSpacing(spacing)
        self.setWrapping(wrapping)

        self.label = QLabel("Collections")
        self.setVisible(True)

        self.populate(self.loadCollections())


    def populate(self, collectionList: list['Collection']):
        self.clear()
        for row, item in enumerate(collectionList):
            item.setText(item.name)
            self.insertItem(row, item)


    def loadCollections(self) -> list['Collection']:
        # Mock list of collection objects
        load = []
        with CollectionDB() as cdb:
            print(cdb.read_all())
            pass
        return load
        
