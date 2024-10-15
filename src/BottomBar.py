from PySide6.QtCore import SLOT
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton

class BottomBar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        now_playing = NowPlaying()
        layout.addWidget(now_playing)

        media_controls = MediaControls()
        layout.addWidget(media_controls)

class NowPlaying(QWidget):

    def __init__(self):#TODO: Should take string as args for label texts
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        song = QLabel()
        song.setText("Song Name")
        layout.addWidget(song)

        artist = QLabel()
        artist.setText("Artist")
        layout.addWidget(artist)


class MediaControls(QWidget):
    def  __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        shuffle_button = QPushButton()#TODO: Connect buttons up to slots/methods
        shuffle_button.setText("Shuffle")
        layout.addWidget(shuffle_button)

        shuffle_button = QPushButton()
        shuffle_button.setText("Shuffle")
        layout.addWidget(shuffle_button)

        prev_button = QPushButton()
        prev_button.setText("Previous")
        layout.addWidget(prev_button)

        play_button = QPushButton()
        play_button.setText("Play / Pause")
        layout.addWidget(play_button)

        next_button = QPushButton()
        next_button.setText("Next")
        layout.addWidget(next_button)


    #TODO
    def toggle_play_pause(self):
        print("toggled")

    #TODO
    def skip(self):
        #interact with song queue
        print("song skipped")

    #TODO
    def previous(self):
        #if current timestamp <5s
        print("previous song loaded")
        #else:
            #print("song restarted") // set time to 0
