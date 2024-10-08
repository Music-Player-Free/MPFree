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
class Bridge(QObject):

    @Slot()
    def toggle_play_pause(self):
        print("toggled")
