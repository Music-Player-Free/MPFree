from PySide6.QtWidgets import (QFileDialog, QPushButton, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QLineEdit, QLabel, QComboBox, QListWidget)
from PySide6.QtCore import (QSize, QObject, Slot, Signal, SignalInstance)
from PySide6.QtGui import (QValidator, QRegularExpressionValidator)
from abc import ABC, abstractmethod
import regex
import os
import vlc

from configuration import Config, Dict
from constants import JSON_PATH
from db import SongDB, Songs_Collections, Songs_Tags, CollectionDB, Collections_Tags



'''
<<<<<<< HEAD
TODO
UI clean up, but that's the whole program really.
file text functionality
dropdown functionality
=======
TODO 
UI styling
    refresh icon
theme dropdown functionality
>>>>>>> angus
keybinds
add option to disable automatic folder creation?


m̶i̶g̶h̶t̶ ̶b̶e̶ ̶g̶o̶o̶d̶ ̶i̶d̶e̶a̶ ̶t̶o̶ ̶s̶e̶p̶a̶r̶a̶t̶e̶ ̶t̶h̶e̶ ̶b̶o̶i̶l̶e̶r̶p̶l̶a̶t̶e̶ ̶s̶t̶u̶f̶f̶ ̶i̶n̶t̶o̶ ̶m̶e̶t̶h̶o̶d̶s̶ ̶o̶f̶ ̶s̶e̶t̶t̶i̶n̶g̶s̶.̶.̶.̶?̶ ̶(̶l̶a̶t̶e̶r̶)̶ ̶ 7.11.24
'''
class Settings(QWidget):
    '''
    Settings button
    Extends QWidget.
    '''
    def __init__(self, spacing=5, wrapping=True):
        super().__init__()
        settings_layout = QVBoxLayout()  # Vertical

        # Create label
        settings_label = QLabel()
        settings_label.setText("Settings")


<<<<<<< HEAD
        file_widget = FilePane(user_data.filePath)
=======
        conf: Dict = Config.load_json(JSON_PATH)
>>>>>>> angus

        # Create file widget 
        self.file_widget = FilePane(conf.userData.filePath) 

        # Theme widget
        self.theme_widget = ThemePane()

        # Keybinds widget
        self.keybinds_widget = KeybindsPane()  # or list view?

        # add widgets to layout
        settings_layout.addWidget(settings_label)
<<<<<<< HEAD
        settings_layout.addWidget(file_widget)
        settings_layout.addWidget(theme_widget)
        settings_layout.addWidget(keybinds_widget)
=======
        settings_layout.addWidget(self.file_widget)  
        settings_layout.addWidget(self.theme_widget)
        settings_layout.addWidget(self.keybinds_widget)
>>>>>>> angus

        self.setLayout(settings_layout)  # apply layout


'''FileEdit'''
# ------------------------------------------------------------------------------------ #
class FileLineEdit(QLineEdit):
    filePathChanged = Signal(name="filePathChanged")  # Add custom signal

    def __init__(self, path):
        '''
        LineEdit subclassed for file panes use.\n
        Uses regular expression validator to prevent users typing "//"\n
        '''
        super().__init__()  # Init LineEdit

        # match file paths with word characters but NOT "//" (empty file path)
        rex = "^[\\w]+(?:\\/[a-zA-Z0-9]+)*\\/?$" 


        # Init validator obj. Uses params: regex, parent
        validator = QRegularExpressionValidator(rex, None)
        '''
        ^^ not added as an instance variable because it would prevent users' typing.
        '''


        # Lambda function to pass argument correctly.
        # Without lambda, this would call the validator on init, however we can use
        # named argument (kw) 
        self.returnPressed.connect(
            lambda validator=validator : self.on_text_changed(validator)) 

        # Set placeholder text OR user path.
        if not path:
            self.setPlaceholderText("Enter file path")
        else:
            self.setText(path)


    @Slot()
    def on_text_changed(self, validator: QRegularExpressionValidator):
        '''
        Slot to validate user file input. 
        '''
        if (validator
            and validator.validate(self.text(), 1)[0].name == "Acceptable"):  # [0] because it returns tuple,
                                                                              #  .name because its enum
            # Allows user to just type "audio" or "src" (in our case) and OS will append the base path (Home/users/...)
            path = os.path.abspath(self.text())
            
            # If path exists, and is path, and is a NEW path
            # This defines the function to be only on CHANGED path name
            if (os.path.exists(path)
<<<<<<< HEAD
                and os.path.isdir(path)):

=======
                and os.path.isdir(path)
                and not path == JSON_PATH):
                
>>>>>>> angus
                # load config
                conf = Config.load_json(JSON_PATH)
                conf["userData"]["filePath"] = path  # Could also do conf.userData.filePath but idk which is more clear

                # write to config
                Config.save_json(conf, JSON_PATH)

<<<<<<< HEAD
=======
                # Update text with new file path
                self.setText(path)

                # Emit path changed signal. This will be connected to the refresh slot somewhere else. 
                self.filePathChanged.emit()


    def __repr__(self):
        return "FileLineEdit: {}".format(self.text())
                
'''FileButton'''
# ------------------------------------------------------------------------------------ #
>>>>>>> angus

class FileDialogButton(QPushButton):
    filePathChanged = Signal(name="filePathChanged")  

    def __init__(self, button_text: str):
        super().__init__(button_text)

        # Custom signal

        # Use qsize to set size for button.
        button_size = (80,20)
        self.setFixedSize(QSize(button_size[0], button_size[1]))

        self.clicked.connect(
            lambda checked: self.get_user_dir(button_text)) # connect to slot, lambda to ignore .clicked param (checked).
        '''
        If lambda is not used, this will try to pass checked (type: bool) into slot, and python will bitch about it.
        '''

    @Slot()
    def get_user_dir(self, button_text):
        '''
        Open FileDialog, QT sorts out most error checking stuff, so we 
        can just cast to string and use the path as we want.

        No need to check if exists as users have to pick A folder at least.
        No need to check if directory because that's all QT will allow.
        '''

        # init dialog
        dialog = QFileDialog()
        
        # cast to string for in-house use
        path = str(dialog.getExistingDirectory(caption=button_text))

        # load config
        conf = Config.load_json(JSON_PATH)
        conf["userData"]["filePath"] = path

        # write to config
        Config.save_json(conf, JSON_PATH)

        # emit signal on successful change
        self.filePathChanged.emit()
    
    def __repr__(self):
        return "FileDialogButton: {}".format()

'''FilePane'''
# ------------------------------------------------------------------------------------ #
class FilePane(QWidget):
    '''
    This is leftover from testing. To make things a bit easier we could pass this
    into the init functions of FileLineEdit and FileDialogButton?
    '''
    # filePathChanged = Signal(name="filePathChanged")  
    refreshReady = Signal(name="refreshReady")


    def __init__(self, file_path="Enter file path"):
        super().__init__()
        file_layout = QHBoxLayout()

        # TODO styling:
        # display **why** // is not allowed.
        # lose focus once enter is pressed, or mouse clicked??
<<<<<<< HEAD

        file_text = self.line_edit(file_path)

        file_button = QPushButton("Import music from folder") # create button
        file_button.setFixedSize(QSize(80, 20))
        file_button.clicked.connect(self.get_user_dir) # connect to slot
=======
        
        file_text = FileLineEdit(file_path)
        file_text.filePathChanged.connect(
            lambda sig=self.refreshReady: FilePane.refresh(sig))  
        
        file_button = FileDialogButton("Choose Folder")
        file_button.filePathChanged.connect(
            lambda sig=self.refreshReady: FilePane.refresh(sig))

        refresh_button = QPushButton("Refresh!")  # TODO: refresh icon
        icon_size = (20, 20)  # Replace with refresh icon size

        refresh_button.setFixedSize(QSize(icon_size[0], icon_size[1]))
        refresh_button.clicked.connect(
            lambda checked, sig=self.refreshReady: FilePane.refresh(sig))
>>>>>>> angus

        file_layout.addWidget(file_text)
        file_layout.addWidget(file_button)
        file_layout.addWidget(refresh_button)

        self.setLayout(file_layout)

    @staticmethod
    def refresh(signal: SignalInstance):

<<<<<<< HEAD
    def line_edit(self, path):
        '''
        os.path.exists()
        os.path.isdir()
        os.path.isfile()
        '''
        # match file paths with word characters but NOT // (empty file path)
        rex = "^[\\w]+(?:\\/[a-zA-Z0-9]+)*\\/?$"
        validator = QRegularExpressionValidator(rex, None)
=======
        # Drop songs, collections, songs_collections, songs_tags, collections_tags
>>>>>>> angus

        # THis is ugly as hell. Maybe we should look into having this instances in a list 
        # and we can loop through them?
        # Might have to do some factory stuff. Premature optimisation !!!!!!
        with SongDB() as sdb:
            sdb.drop()
        with CollectionDB() as cdb:
            cdb.drop()
        with Songs_Collections() as sc_rel:
            sc_rel.drop()
        with Songs_Tags() as st_rel:
            st_rel.drop()
        with Collections_Tags() as ct_rel:
            ct_rel.drop()

<<<<<<< HEAD
        if not path:
            edit.setPlaceholderText("Enter file path")
        else:
            edit.setText(path)

        return edit


    @Slot()
    def get_user_dir(self, clicked, button_text="Choose folder"):
        '''
        Returns File Dialog window instance
        '''
        dialog = QFileDialog()
        # print(str(dialog.getExistingDirectory(parent=self, caption=button_text)))
        return str(dialog.getExistingDirectory(self, button_text))

=======
        # Get user config settings
        conf = Config.load_json(JSON_PATH)

        # Access static method (no instance required)
        FilePane.load_from_path(conf.userData.filePath, [])
        
        signal.emit()


    @staticmethod
    def load_from_path(file: str, colls: list[int]):
        # If mp3 file
        if os.path.isfile(file) and file.endswith(".mp3"):
            song_id = -1  # init id variable. (Python might ignore scope here but oldschool == cool)
            
            with SongDB() as sdb:
                path = file  # dunno if we want absolute path or just the name..?

                '''
                DISCLAIMER!!
                VLC is all through cpython, and this obscures what instances have variables.##
                You CAN totally do . methods, i.e. instance.method(parameters)
                HOWEVER python cannot SEE these and they will be whited out, with no intellisense
                THEREFORE we can static methods i.e. vlc.class.method(instance, parameters) 
                WHICH WILL detect what the function does and give type hints etc.
                '''
                inst = vlc.Instance()
                media = vlc.Instance.media_new(inst, file)   # create media instance
                vlc.Media.parse(media)  # Parse the media (read it... blackbox stuff)

                '''
                Media.get_meta(col: int)
                cols that have useful data: 
                0 - title
                1 - artist
                4 - album
                    All the others I can't see, and since mp3 tags need to be edited at the byte-level,
                    I cba to test anymore <- I did actually investigate but it is too much effort for
                    an already solved problem lol.
                '''
                # Create dict: {0: artist, 1: artist, 4: album}
                meta = {}
                for i in [0, 1]: # select columns 0, 1 from metadata
                    ans = vlc.Media.get_meta(media, i)
                    if not ans:  # If no metadata present, returns None, so convert that to ""
                        ans = ""
                    meta[i] = ans

                track_len = vlc.Media.get_duration(media) // 1000  # Represented in ms

                # create list of data
                data = [path, meta[0], track_len, meta[1]]

                # Insert into DB
                song_id = sdb.create(data)
            
            with Songs_Collections() as sc_rel:
                for coll_id in colls:
                # Song Relations only uses two columns
                    data = [song_id, coll_id]
                    idx = sc_rel.create(data)  ## don't need idx as of 7.11.24, but create returns it.

            return 
        
        # If folder
        if os.path.isdir(file):
            obj = os.scandir(file) # Return iterator of all files in folder
            
            with CollectionDB() as cdb:
                
                name = file.split("/")[-1] if colls else "All Songs"
                description = ""            # leave blank for now
                author = ""                 # might deprecate?  <------------------TODO

                # create list of data to create
                data = [name, description, author]

                colls.append(cdb.create(data))  # insert to db
                # coll_id now has the most recent collection, to pass into each of the file creations.
                
            # Iterate through files from scandir obj
            for entry in obj:
                FilePane.load_from_path(str(entry.path), colls)

            colls.pop()

            # Memory safe (lol)
            obj.close()
            return 
        return

>>>>>>> angus
    def __repr__(self):
        return super().__repr__()


'''Theme Pane'''
# ------------------------------------------------------------------------------------ #
class ThemePane(QWidget):
    def __init__(self):
        super().__init__()
        theme_layout = QHBoxLayout()

        theme_label = QLabel()
        theme_label.setText("Choose theme")

        #TODO
        theme_dropdown = QComboBox()

        #TODO
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(theme_dropdown)

        self.setLayout(theme_layout)

    def __repr__(self):
        return super().__repr__()

'''Keybinds Pane'''
# ------------------------------------------------------------------------------------ #
class KeybindsPane(QListWidget):
    def __init__(self):
        super().__init__()
        keybinds_layout = QVBoxLayout()

        #TODO
        # add widgets for keybinds to lists

        keybinds_label = QLabel()
        keybinds_label.setText("Keybinds here")

        keybinds_layout.addWidget(keybinds_label)
        self.setLayout(keybinds_layout)

    def __repr__(self):
        return super().__repr__()
