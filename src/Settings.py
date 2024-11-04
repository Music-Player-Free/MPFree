from PySide6.QtWidgets import (QFileDialog, QPushButton, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QLineEdit, QLabel, QComboBox, QListWidget)
from PySide6.QtCore import (QSize, QObject, Slot)
from PySide6.QtGui import (QValidator, QRegularExpressionValidator)

import regex
import os

from configuration import Config, Dict
from constants import JSON_PATH



'''
TODO 
UI styling
theme dropdown functionality
keybinds

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

class FileLineEdit(QLineEdit):

    @staticmethod
    def line_edit(path):
        # match file paths with word characters but NOT // (empty file path)
        rex = "^[\\w]+(?:\\/[a-zA-Z0-9]+)*\\/?$" 
        validator = QRegularExpressionValidator(rex, None)

        edit = FileLineEdit()
        edit.returnPressed.connect(
            lambda validator=validator : edit.on_text_changed(validator))

        if not path:
            edit.setPlaceholderText("Enter file path")
        else:
            edit.setText(path)
        
        return edit

    @Slot()
    def on_text_changed(self, validator: QRegularExpressionValidator):
        if (validator
                and validator.validate(self.text(), 1)[0].name == "Acceptable"): # [0] because it returns tuple,
            path = self.text()                                                   #  .name because its enum
            if (os.path.exists(path)
                and os.path.isdir(path)):
                
                # load config
                conf = Config.load_json(JSON_PATH)
                conf["userData"]["filePath"] = path

                # write to config
                Config.save_json(conf, JSON_PATH)
    def __repr__(self):
        return "FileLineEdit: {}".format(self.text())
                

class FilePane(QWidget):
    def __init__(self, file_path: str="Enter file path"):
        super().__init__()
        file_layout = QHBoxLayout()

        # TODO styling:
        # display **why** // is not allowed.
        # lose focus once enter is pressed, or mouse clicked??
        
        file_text = FileLineEdit.line_edit(file_path)
        
        file_button = QPushButton("Import music from folder") # create button
        file_button.setFixedSize(QSize(80, 20))
        file_button.clicked.connect(
            lambda checked: self.get_user_dir()) # connect to slot

        file_layout.addWidget(file_text)
        file_layout.addWidget(file_button)

        self.setLayout(file_layout)


    @staticmethod
    def get_user_dir(button_text="Choose folder"):
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

        return

    def __repr__(self):
        return super().__repr__()



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
