from PySide6.QtWidgets import (QFileDialog, QPushButton, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QLineEdit, QLabel, QComboBox, QListWidget)
from PySide6.QtCore import (QSize)
from configuration import Config, Dict


'''
TODO 
UI clean up, but that's the whole program really.
file text functionality
dropdown functionality
keybinds

might be good idea to separate the boilerplate stuff into methods of settings...? (later)
'''
class Settings(QWidget):
    '''
    Settings button

    Extends QWidget.
    '''
    def __init__(self, json_path: str, spacing=5, wrapping=True):
        super().__init__()

        config = Config().load_json(json_path)

        settings_layout = QVBoxLayout()  # Vertical

        settings_label = QLabel()
        settings_label.setText("Settings")

        user_data: Dict = config.userData
        #TODO
        #input data from config
        file_widget = FilePane(user_data.filePath) 
        theme_widget = ThemePane()
        keybinds_widget = KeybindsPane()  # or list view?

        settings_layout.addWidget(settings_label)
        settings_layout.addWidget(file_widget)  
        settings_layout.addWidget(theme_widget)
        settings_layout.addWidget(keybinds_widget)

        self.setLayout(settings_layout)  # apply layout


class FilePane(QWidget):
    def __init__(self, file_path: str="Enter file path"):
        super().__init__()
        file_layout = QHBoxLayout()


        #TODO
        # some stuff here, validator, signals like text changed etc
        # lose focus once enter is pressed
        file_text = QLineEdit()
        if not file_path:
            file_text.setPlaceholderText("Enter file path")
        else:
            file_text.setText(file_path)
        
        file_button = QPushButton("Import music from folder") # create button
        file_button.setFixedSize(QSize(80, 20))
        file_button.clicked.connect(self.get_user_dir) # connect to slot

        file_layout.addWidget(file_text)
        file_layout.addWidget(file_button)

        self.setLayout(file_layout)

    def get_user_dir(self, clicked, button_text="Choose folder"):
        '''
        ### TODO:
        <li>Might need to put this somewhere else, but for now can stay
        <li>Look into existing directoy for user preference. WIll help when we store stuff eventually.
        

        Returns File Dialog window instance
        '''
        dialog = QFileDialog()
        # print(str(dialog.getExistingDirectory(parent=self, caption=button_text)))
        return str(dialog.getExistingDirectory(self, button_text))
    
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
