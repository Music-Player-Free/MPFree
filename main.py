import sys
from UI_desktop import QML
from slots import *
import vlc

def main():
    # TODO
    # App
    app = QGuiApplication(sys.argv)


    # Run the main Qt loop
    engine = QQmlApplicationEngine()
    engine.loadData(QML.encode('utf-8'))
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
