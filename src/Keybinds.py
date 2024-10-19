
from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget


class KeybindsPane(QWidget):
    '''
    Outer widget to hold user keybinds.
    '''
    def __init__(self):
        super().__init__()
        # using vertical layout
        layout = QVBoxLayout()

        # Create Keybinds object
        # Hover to see description or, it extends a listwidget
        keybinds = Keybinds()

        # Create label
        label = QLabel()
        label.setText("Keybinds")

        # Add widgets to layout template
        layout.addWidget(label)
        layout.addWidget(keybinds)

        # Apply layout
        self.setLayout(layout)

class Keybind(QListWidgetItem):
    '''
    Keybind widget, contains ???
    '''

    # Need id?
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name


class Keybinds(QListWidget): 
    '''
    Keybinds extends ListWidget and will hold keybind objects (?)
    Spacing between child items is 5 and wrapping is set to true\n
    List is populated on initialisation 
    '''
    def __init__(self, spacing=5, wrapping=True):
        super().__init__()
        # Apply label to self
        self.label = QLabel("Collections")

        # Kwargs specify standard spacing as 5px and wrapping True.
        self.setSpacing(spacing)
        self.setWrapping(wrapping)
        
        # Visibile to user
        self.setVisible(True)

        # Populate user keybinds in the pane
        self.populate(self.loadKeybinds())


    def populate(self, keybindList: list['Keybind']):
        '''
        ### TODO
        do we allow empty lists? 

        Populate ListWidget instance (self) with keybind objects.
        '''

        # Enumerate input list
        for row, item in enumerate(keybindList):
            item.setText(item.name)
            self.insertItem(row, item)

    def loadKeybinds(self) -> list['Keybind']:
        #TODO: replace with loading from JSON/XML/TOML/WHATEVER
        loaded_keybinds = [Keybind(0,"P - Toggle Play / Pause"), Keybind(1,"S - Skip song")]
        return loaded_keybinds
