from PySide6.QtWidgets import QStackedWidget


class ToggleWidget(QStackedWidget):
    def __init__(self, widget1, widget2):
        super().__init__()
        self.addWidget(widget1)
        self.addWidget(widget2)

    def toggle(self):
        self.setCurrentIndex((self.currentIndex()+1) % 2)
