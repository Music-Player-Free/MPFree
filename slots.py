import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot
import vlc


@Slot()
def toggle_play_pause():
    print("toggled")
