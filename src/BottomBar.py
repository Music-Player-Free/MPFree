from PySide6.QtCore import SLOT
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton

from ToggleWidget import ToggleWidget

class BottomBar(QWidget):
    def __init__(self, ref: 'ToggleWidget'):
        super().__init__()
        layout = QHBoxLayout()

        # Instantiate NowPlaying object
        now_playing = NowPlaying()
        layout.addWidget(now_playing)

        # Instantiate MediaControl object
        media_controls = MediaControls()
        layout.addWidget(media_controls)

        # Instantiate SettingsButton object
        settings_button = SettingsButton(ref)
        layout.addWidget(settings_button)

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
    def  __init__(self):
        
        super().__init__()
        # Using Horizontal layout
        layout = QHBoxLayout()
        

        #TODO: Connect buttons up to slots/methods!!!!

        # Instantiate button with text, 
        shuffle_button = QPushButton() 
        shuffle_button.setText("Shuffle")

        # Instantiate button with text
        prev_button = QPushButton()
        prev_button.setText("Previous")

        # Instantiate button with text
        play_button = QPushButton()
        play_button.setText("Play / Pause")

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

    #TODO
    def toggle_play_pause(self):
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
    def __init__(self, ref: 'ToggleWidget'):
        super().__init__()
        # Create layout template
        layout = QHBoxLayout()

        # Better name for this variable?
        self.ref = ref

        # Create, label and connect button
        button = QPushButton()
        button.setText("Settings")
        button.clicked.connect(self.ref.toggle)

        layout.addWidget(button)

        # Apply layout
        self.setLayout(layout)

