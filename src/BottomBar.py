from PySide6.QtCore import SLOT, Slot

from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton
from Songs import Song
from Songs import Songs as Songslist
import Songs
from ToggleWidget import ToggleWidget
import vlc

class BottomBar(QWidget):
    def __init__(self, ref: 'ToggleWidget'):
        super().__init__()
        layout = QHBoxLayout()

        # Instantiate NowPlaying object
        self.now_playing = NowPlaying()
        layout.addWidget(self.now_playing)

        # Instantiate MediaControl object
        self.media_controls = MediaControls()
        layout.addWidget(self.media_controls)

        # Instantiate SettingsButton object
        self.settings_button = SettingsButton(ref)
        layout.addWidget(self.settings_button)

        self.setLayout(layout)


class NowPlaying(QWidget):
    '''
    Extends QWidget and shows currently playing song <br>
    and artist.
    '''


    #TODO asf
    # Should take string as args for label texts
    # Remember last song played and position
    def __init__(self):
        super().__init__()
        # Using Vertical layout.
        layout = QVBoxLayout()

        # Create label, set text and add to vertical layout
        song = QLabel()
        song.setText("Song Name")

        # Create label, set text and add to vertical layout
        artist = QLabel()
        artist.setText("Artist")

        layout.addWidget(song)
        layout.addWidget(artist)

        # Apply newly made layout to self(Qwidget that represents now playing area)
        self.setLayout(layout)

class MediaControls(QWidget):
    '''
    ### TODO:
    <ul>
        <li>Shuffle button to randomize current collection. Should collections remember shuffle preference?</li>
        <li>Skip forward</li>
        <li>Skip backward</li>
    </ul>

    Media controls widget extending QWidget \n
    Shuffle, play/pause, skip back and forwards.
    '''
    def  __init__(self): #TODO: Connect buttons up to slots/methods!!!!
        super().__init__()
        self.is_paused = True
        self.current_song: Song
        self.songs_ref: Songslist = Songslist()# alias'd class to circumvent import problems

        # ---- Window setup
        # Using Horizontal layout
        layout = QHBoxLayout()

        # Instantiate button with text,
        shuffle_button = QPushButton()
        shuffle_button.setText("Shuffle")

        # Instantiate button with text
        prev_button = QPushButton()
        prev_button.setText("Previous")

        # Instantiate button with text
        play_button = QPushButton()
        play_button.setText("Play / Pause")
        play_button.clicked.connect(self.toggle_play_pause)

        # Instantiate button with text
        next_button = QPushButton()
        next_button.setText("Next")

        # Create playback widiget
        playback_widget =  PlaybackControls()

        # Add to layout template

        # add to layout template
        layout.addWidget(shuffle_button)
        layout.addWidget(prev_button)
        layout.addWidget(play_button)
        layout.addWidget(next_button)
        layout.addWidget(playback_widget)

        # Apply buttons to layout template
        self.setLayout(layout)
        #--------END window setup

        #---- vlc
        # start vlc
        # Load app with an example song. Should change this to be last played song
        self.player = vlc.MediaPlayer("file:////home/kyle/Documents/Projects/MPFree/audio/amalgam.mp3")
        # self.player.play() THIS WORKS
        #----- END vlc

    @Slot()
    def set_current_song(self, song: Song):
        self.current_song = song
        self.player = vlc.MediaPlayer(self.current_song.path_to_file)
        print(f"Set current song to {song.song_name}, {song.path_to_file}")
    def set_songs_ref(self,songs: Songslist):# alias'd class
        self.songs_ref = songs

    #TODO
    def toggle_play_pause(self):
        if self.is_paused:
            self.player.play()
            self.is_paused = not self.is_paused
        else:
            self.player.pause()
        print("toggled")

    #TODO
    def skip(self):
        #interact with song queue
        print("song skipped")

    #TODO
    def previous(self):
        #if current timestamp <2s
        print("previous song loaded")
        # else:
            #print("song restarted") // set time to 0


class PlaybackControls(QWidget):
    '''
    Playback controls extends QWidget.
    '''
    def __init__(self):
        super().__init__()
        # Create layout
        layout = QHBoxLayout()

        # Create button
        button = QPushButton()
        button.setText("Playback\nControls")

        # Add button to layout template
        layout.addWidget(button)

        # apply template to qwidget
        self.setLayout(layout)


class SettingsButton(QWidget):
    '''
    ### TODO:
    <ul>
        <li>Layout of settings page</li>
        <li>Add appropriate widgets of settings. </li>
    </ul>

    Replace central widgets with settings page.
    '''
    def __init__(self, toggle_ref: 'ToggleWidget'):
        super().__init__()
        # Create layout template
        layout = QHBoxLayout()

        # Better name for this variable?
        self.toggle_ref = toggle_ref

        # Create, label and connect button
        button = QPushButton()
        button.setText("Settings")
        button.clicked.connect(self.toggle_ref.toggle)

        layout.addWidget(button)

        # Apply layout
        self.setLayout(layout)
