
from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

class Keybind(QListWidgetItem):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name


class Keybinds(QListWidget): # Displays collections
    def __init__(self):
        super().__init__()
        self.setSpacing(5)
        self.setWrapping(True)
        self.label = QLabel("Collections")
        self.setVisible(True)

        self.populate(self.loadKeybinds())

    def populate(self, keybindList: list['Keybind']):
            for row, item in enumerate(keybindList):
                item.setText(item.name)
                self.insertItem(row, item)

    def loadKeybinds(self) -> list['Keybind']:
        #TODO: replace with loading from JSON/XML/TOML/WHATEVER
        loaded_keybinds = [Keybind(0,"P - Toggle Play / Pause"), Keybind(1,"S - Skip song")]
        return loaded_keybinds

class KeybindsPane(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        keybinds = Keybinds()
        label = QLabel()
        label.setText("Keybinds")

        layout.addWidget(label)
        layout.addWidget(keybinds)
