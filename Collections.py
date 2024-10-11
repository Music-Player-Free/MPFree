from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QLabel, QListView, QWidget

class Collection(QListWidgetItem): # For playlists, albums
    def __init__(self, thumbnail, name, artist):
        self.thumbnail = thumbnail
        self.name = name
        self.artist = artist

class Collections(QListWidget): # Displays collections
    def __init__(self, collectionList):
        super(Collections, self).__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Collections")

        for n in collectionList:
            self.addItem(n)
