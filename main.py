from PySide6.QtGui import QIcon
import slots
from slots import *
from MainWindow import MainWindow

def main():
# TODO
#
# App
    app = QApplication(sys.argv)
    # Run the main Qt loop
    #engine = QQmlApplicationEngine()
    #engine.load( QUrl("qml/UI_desktop.qml"))

    window = MainWindow()
    window.show()


    sys.exit(app.exec())

if __name__ == '__main__':
    main()
