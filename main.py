import slots
from slots import *

def main():
# TODO
#
# App
    app = QGuiApplication(sys.argv)

    # Run the main Qt loop
    engine = QQmlApplicationEngine()
    engine.load( QUrl("qml/UI_desktop.qml") )
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
