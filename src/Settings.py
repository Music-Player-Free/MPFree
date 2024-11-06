from PySide6.QtWidgets import (QFileDialog, QPushButton, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QLineEdit, QLabel, QComboBox, QListWidget)
from PySide6.QtCore import (QSize, QObject, Slot, Signal)
from PySide6.QtGui import (QValidator, QRegularExpressionValidator)
from abc import ABC, abstractmethod
import regex
import os
import vlc

from configuration import Config, Dict
from constants import JSON_PATH
from db import SongDB, Songs_Collections, Songs_Tags, CollectionDB, Collections_Tags



'''
TODO 
UI styling
    refresh icon
theme dropdown functionality
keybinds
DELETE ALBUM FROM SONGS OBJECTS.


might be good idea to separate the boilerplate stuff into methods of settings...? (later)
'''
class Settings(QWidget):
    '''
    Settings button
    Extends QWidget.
    '''
    def __init__(self, spacing=5, wrapping=True):
        super().__init__()
        settings_layout = QVBoxLayout()  # Vertical

        settings_label = QLabel()
        settings_label.setText("Settings")

        # deprecated
        user_data: Dict = Config.load_json(JSON_PATH).userData

        file_widget = FilePane(user_data.filePath) 

        theme_widget = ThemePane()

        keybinds_widget = KeybindsPane()  # or list view?

        settings_layout.addWidget(settings_label)
        settings_layout.addWidget(file_widget)  
        settings_layout.addWidget(theme_widget)
        settings_layout.addWidget(keybinds_widget)

        self.setLayout(settings_layout)  # apply layout


'''FileEdit'''
# ------------------------------------------------------------------------------------ #
class FileLineEdit(QLineEdit):
    filePathChanged = Signal(name="filePathChanged")  # No idea if int is correct here.

    def __init__(self, path):
        super().__init__()
        # match file paths with word characters but NOT // (empty file path)
        rex = "^[\\w]+(?:\\/[a-zA-Z0-9]+)*\\/?$" 
        validator = QRegularExpressionValidator(rex, None)

        self.returnPressed.connect(
            lambda validator=validator : self.on_text_changed(validator))

        if not path:
            self.setPlaceholderText("Enter file path")
        else:
            self.setText(path)


    @Slot()
    def on_text_changed(self, validator: QRegularExpressionValidator):
        if (validator
                and validator.validate(self.text(), 1)[0].name == "Acceptable"): # [0] because it returns tuple,
                                                                                 #  .name because its enum
            path = os.path.abspath(self.text())
            
            if (os.path.exists(path)
                and os.path.isdir(path)
                and not path == JSON_PATH):
                
                # load config
                conf = Config.load_json(JSON_PATH)
                conf["userData"]["filePath"] = path  # Could also do conf.userData.filePath but idk which is more clear

                # write to config
                Config.save_json(conf, JSON_PATH)

                self.setText(path)

                # Refresh 
                self.filePathChanged.emit()


    def __repr__(self):
        return "FileLineEdit: {}".format(self.text())
                
'''FileButton'''
# ------------------------------------------------------------------------------------ #

class FileDialogButton(QPushButton):
    filePathChanged = Signal(name="filePathChanged")  # No idea if int is correct here.

    def __init__(self):
        super().__init__("Import music from folder")
        self.setFixedSize(QSize(80, 20))
        self.clicked.connect(
            lambda checked: self.get_user_dir()) # connect to slot, lambda to ignore .clicked param (checked).
    
    @Slot()
    def get_user_dir(self, button_text="Choose folder"):
        '''
        Returns File Dialog window instance
        '''
        print("Here!")
        dialog = QFileDialog()
        
        path = str(dialog.getExistingDirectory(caption=button_text))

        # load config
        conf = Config.load_json(JSON_PATH)
        conf["userData"]["filePath"] = path

        # write to config
        Config.save_json(conf, JSON_PATH)

        self.filePathChanged.emit()
    
    def __repr__(self):
        return "FileDialogButton: {}".format()

'''FilePane'''
# ------------------------------------------------------------------------------------ #
class FilePane(QWidget):

    filePathChanged = Signal(name="filePathChanged")  # No idea if int is correct here.

    def __init__(self, file_path="Enter file path"):
        super().__init__()
        file_layout = QHBoxLayout()

        # TODO styling:
        # display **why** // is not allowed.
        # lose focus once enter is pressed, or mouse clicked??
        
        file_text = FileLineEdit(file_path)
        file_text.filePathChanged.connect(self.refresh)  # Testing
        
        file_button = FileDialogButton()
        file_button.filePathChanged.connect(self.refresh)

        refresh_button = QPushButton("QIcon")  # TODO: refresh icon
        icon_size = (40, 40)  # Replace with refresh icon size
        refresh_button.setFixedSize(QSize(icon_size[0], icon_size[1]))
        refresh_button.clicked.connect(
            lambda checked: self.refresh())

        file_layout.addWidget(file_text)
        file_layout.addWidget(file_button)

        self.setLayout(file_layout)

    @staticmethod
    def refresh():
        # Load from file path
        # Load into Python
        print("success!")

        # Drop songs, collections, songs_collections, songs_tags, collections_tags

        # THis is ugly as hell. Maybe we should look into having this instances in a list 
        # and we can loop through them?
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

        conf = Config.load_json(JSON_PATH)

        FilePane.load_from_path(conf.userData.filePath, 0)


    '''
    Media.get_meta(col: int)
    cols that have useful data: 
    0 - title
    1 - artist
    4 - album
        All the others I can't see, and since mp3 tags need to be edited at the byte-level,
        I cba to test anymore <- I did actually investigate but it is too much effort for
        an already solved problem lol.
    Media.get_duration()
    
    '''
    @staticmethod
    def load_from_path(file: str, coll_id: int):
        # Base case
        if not file:
            return
        
        # If mp3 file
        if os.path.isfile(file) and file.endswith(".mp3"):
            song_id = -1  # init id variable. (Python might ignore scope here but oldschool == cool)
            with SongDB() as sdb:
                path = file  # dunno if we want absolute path or just the name..?

                inst = vlc.Instance()
                media = inst.media_new(file)
                vlc.Media.parse(media)


                meta = {}
                for i in [0, 1]: # select columns 0, 1 from metadata
                    ans = vlc.Media.get_meta(media, i)
                    if not ans:
                        ans = ""
                    meta[i] = ans

                track_len = vlc.Media.get_duration(media) // 1000  # Represented in ms

                data = [path, meta[0], track_len, meta[1]]
                song_id = sdb.create(data)
            
            with Songs_Collections() as sc_rel:
                data = [song_id, coll_id]
                idx = sc_rel.create(data)  ## don't need idx, but it's there.

            return
        
        # If folder
        obj = os.scandir(file)
        coll_id = -1
        with CollectionDB() as cdb:
            name = file.split("/")[-1]  # folder name
            description = ""            # leave blank for now
            author = ""                 # might deprecate?  <------------------TODO

            data = [name, description, author]

            coll_id = cdb.create(data)  # insert to db
            

        for entry in obj:
            FilePane.load_from_path(str(entry.path), coll_id)
        
        # Memory safe (lol)
        obj.close()
        return



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
