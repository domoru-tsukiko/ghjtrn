from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize

from order import Order
from change import Change


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Главная')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pixmap = QPixmap('wid_main/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pixmap)

        self.btn = QPushButton(self)
        self.btn.setIcon(QIcon('wid_main/btn.jpg'))
        self.btn.setIconSize(QSize(230, 60))
        self.btn.setGeometry(73, 364, 230, 60)
        self.btn.clicked.connect(self.open_order)

        self.btn2 = QPushButton(self)
        self.btn2.setIcon(QIcon('wid_main/btn2.jpg'))
        self.btn2.setIconSize(QSize(230, 60))
        self.btn2.setGeometry(73, 444, 230, 60)
        self.btn2.clicked.connect(self.open_change)

    def open_order(self):
        self.second_form = Order()
        self.second_form.show()

    def open_change(self):
        self.form = Change()
        self.form.show()
