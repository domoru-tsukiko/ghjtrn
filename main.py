import sys

from PyQt5.QtWidgets import QApplication
from first import FirstForm


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
