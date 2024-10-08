import sys
import slots
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot
import vlc



app = QApplication(sys.argv)

# Create a button, connect it and show it
button = QPushButton("Play/Pause")
button.clicked.connect(slots.toggle_play_pause)
button.show()

# Run the main Qt loop
app.exec()
