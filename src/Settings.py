from PySide6.QtWidgets import QFileDialog, QPushButton, QVBoxLayout, QWidget


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        print("settings page created")

        file_button = QPushButton("Import music from folder")
        file_button.clicked.connect(self.button_file)
        layout.addWidget(file_button)

    def button_file(self):
        dialog = QFileDialog()
        file = dialog.getExistingDirectory(None, "Choose folder")
        return file
