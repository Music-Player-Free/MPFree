from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from Collections import *
from Songs import *
from BottomBar import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("MPFree Music Player")
        layout = QHBoxLayout()

        collections = Collections()


        songs = Songs()


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        #self.setLayout(layout)
        layout.addWidget(collections)
        layout.addWidget(songs)
        #layout.addWidget(keybinds)

    def setMainPage(self):
        central_widget = QWidget()

        layout = QVBoxLayout()
        panes = QWidget()
        panes_layout = QHBoxLayout()
        panes.setLayout(panes_layout)

        #create panes
        collections = Collections()
        panes_layout.addWidget(collections)
        songs = Songs()
        panes_layout.addWidget(songs)

        #create bottom bar
        bottom_bar = BottomBar()

        #add widgets to QVBoxLayout
        layout.addWidget(panes)
        layout.addWidget(bottom_bar)



class Not_ify(QMainWindow):
    def __init__(self):
        super().__init__()
