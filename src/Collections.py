from PySide6.QtWidgets import QListWidget, QListWidgetItem, QStyleOptionTab, QVBoxLayout, QLabel, QListView, QWidget

from db import CollectionDB



class Collection(QListWidgetItem): 
    '''
    For playlists, albums. Extends WidgetItem. <br>
    Takes integer id and string name as input
    '''

    def __init__(self, db_id:int, name: str):
        super().__init__()
        self.name = name



class Collections(QListWidget): # Displays collections
    def __init__(self):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Collections")
        self.setVisible(True)

        self.populate(self.loadCollections())
        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html


    def populate(self, collectionList: list['Collection']):
        self.clear()
        for row, item in enumerate(collectionList):
            item.setText(item.name)
            self.insertItem(row, item)


    def loadCollections(self) -> list['Collection']:
        #TODO: replace with loading from DB
        print('here!')

        # Mock list of collection objects
        with CollectionDB() as cdb:
            print(cdb.read(1))

        loaded_collections = [Collection(0,"My Playlist"), Collection(1,"Cool Album")]
        return loaded_collections



class CollectionsPane(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Get collections
        collections = Collections()
        # Set label for widget
        label = QLabel()
        label.setText("Collections")

        # Add label and widget to layout
        layout.addWidget(label)
        layout.addWidget(collections)
        
        # apply layout to instance of Collections pane (self)
        self.setLayout(layout)

