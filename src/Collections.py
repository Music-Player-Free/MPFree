from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QLabel, QListView, QWidget

class Collection(QListWidgetItem): # For playlists, albums
    def __init__(self, name):
        super().__init__()
        self.name = name


# Inherits QListWidget, which uses own implementation of QListItem
# So each list is object (JSON-ish?)
class Collections(QListWidget): # Displays collections
    def __init__(self):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Collections")
        self.setVisible(True)

        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html

    def populate(self, collectionList: list['Collection']):# TODO: how to pass a list of Collection?
        for row, item in enumerate(collectionList):
            item.setText(item.name)
            self.insertItem(row, item)

        #newItem = Collection("thumbnail","name","artist")
        #newItem.setText("testing of course")
        #row = 0 # I think it is in 0-indexed format
        #self.insertItem(row, newItem)
