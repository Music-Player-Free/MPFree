import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQuickControls2 import QQuickStyle
import vlc

QML_IMPORT_NAME = "my.slots.name" # Required by @QmlElement to bridge slots into QML file
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Media_Controls(QObject):

    @Slot()
    def toggle_play_pause(self):
        print("toggled")

    @Slot()
    def skip(self):
        #interact with song queue
        print("song skipped")

    @Slot()
    def previous(self):
        #if current timestamp <5s
        print("previous song loaded")
        #else:
            #print("song restarted") // set time to 0
