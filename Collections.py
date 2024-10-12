from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QLabel, QListView, QWidget

class Collection(QListWidgetItem): # For playlists, albums
    def __init__(self, thumbnail, name, artist):
        super().__init__()
        self.thumbnail = thumbnail
        self.name = name
        self.artist = artist


# Inherits QListWidget, which uses own implementation of QListItem
# So each list is object (JSON-ish?)
class Collections(QListWidget): # Displays collections
    def __init__(self, collectionList):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Collections")
        self.setVisible(True)

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html
        # Putting this here
        # I THINK (!) that the collections class (this one) should enumerate through a given
        # list of items we want creating, and then increment row also. enumerate() is perf for this.
        #  so, something like:
        '''
        for row, item enumerate(input):
            self.insertItem(row, item)
        '''
        newItem = QListWidgetItem()
        newItem.setText("testing of course")
        row = 0 # I think it is in 0-indexed format
        self.insertItem(row, newItem)

        for n in collectionList:
            self.addItem(n)
