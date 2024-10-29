from PySide6.QtWidgets import (QFileDialog, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import (QSize)

class Settings(QWidget):
    '''
    Settings button

    Extends QWidget.
    '''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()  # Vertical

        file_button = QPushButton("Import music from folder") # create button
        file_button.setFixedSize(QSize(80, 20))
        file_button.clicked.connect(self.get_user_dir) # connect to slot
        

        layout.addWidget(file_button)  # add to layout
        self.setLayout(layout)  # apply layout


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
