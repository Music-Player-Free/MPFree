from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QLabel, QListView, QWidget

class Collection(QListWidgetItem): # For playlists, albums
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
        for row, item in enumerate(collectionList):
            item.setText(item.name)
            self.insertItem(row, item)

    def loadCollections(self) -> list['Collection']:
        #TODO: replace with loading from BD
        loaded_collections = [Collection(0,"My Playlist"), Collection(1,"Cool Album")]
        return loaded_collections
