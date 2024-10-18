from PySide6.QtWidgets import QFileDialog, QPushButton, QVBoxLayout, QWidget


class Settings(QWidget):
    '''
    Settings button

    Extends QWidget.
    '''
    def __init__(self):
        super().__init__()
        # Using Vertical layout
        layout = QVBoxLayout()

        # Create button
        file_button = QPushButton("Import music from folder")
        file_button.clicked.connect(self.button_file)
        
        # Add file button to layout
        layout.addWidget(file_button)

        # Apply layout
        self.setLayout(layout)

    def button_file(self, button_text="Choose folder"):
        '''
        ### TODO:
        <li>Might need to put this somewhere else, but for now can stay
        <li>Look into existing directoy for user preference. WIll help when we store stuff eventually.
        

        Returns File Dialog window instance
        '''
        dialog = QFileDialog()
        file = dialog.getExistingDirectory(None, button_text)
        return file
