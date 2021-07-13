import MainScreen
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ex = MainScreen.MainScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

