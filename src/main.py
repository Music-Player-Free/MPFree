import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)

    # Run the main Qt loop
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
