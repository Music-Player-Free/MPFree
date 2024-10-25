from Collections import *
from Songs import * 

class CollectionsPane(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Get collections
        self.collections = Collections()

        # Set label for widget
        label = QLabel()
        label.setText("Collections")

        # Add label and widget to layout
        layout.addWidget(label)
        layout.addWidget(self.collections)
        
        # apply layout to instance of Collections pane (self)
        self.setLayout(layout)

class SongsPane(QWidget):
    def __init__(self):
        super().__init__()

        # Init layout type V(ertical)Box
        layout = QVBoxLayout()

        # Create label for songs.
        label = QLabel()
        label.setText("Songs")

        # Create Songs object (extends ListWidget)
        self.songs = Songs()

        # Add widgets to the layout (following (V)ertical box format)
        layout.addWidget(label)
        layout.addWidget(self.songs)

        # Apply layout to instantiated widget (self)
        self.setLayout(layout)

    def insert_to_pane(self, id: int):
        li = []

        with SongDB() as db:
            id_list = Songs_Collections().read(0, [id]).fetchall()
            id_list = [x[0] for x in id_list]
            
            for row in db.read(id_list):
                kw = {col: row[i] for i, col in enumerate(db.columns)}
                inst = Song(**kw)

                li.append(inst)
        self.songs.populate(li)

    def __repr__(self):
        return "Songs Pane: {}".format(self.songs)
