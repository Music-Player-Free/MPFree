from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem

class Song(QListWidgetItem):
    def __init__(self, id, path_to_file, title, artist, duration):
        super().__init__()
        self.id = id
        self.path_to_file = path_to_file
        self.title = title
        self.artist = artist
        self.duration = duration

class Songs(QListWidget):
    def __init__(self):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Songs")
        self.setVisible(True)

    def populate(self, songList: list['Song']):
        for row, item in enumerate(songList):
            item.setText(item.title)
            self.insertItem(row, item)
