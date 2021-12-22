from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize


class Change(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Способы изменения')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_izm/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pic)

        # кнопка добавить
        self.btn_add = QPushButton(self)
        self.btn_add.setIcon(QIcon('win_izm/btn_add.jpg'))
        self.btn_add.setIconSize(QSize(230, 60))
        self.btn_add.setGeometry(72, 257, 230, 60)
        self.btn_add.clicked.connect(self.btn_add_click)

        # кнопка удалить
        self.btn_del = QPushButton(self)
        self.btn_del.setIcon(QIcon('win_izm/btn_del.jpg'))
        self.btn_del.setIconSize(QSize(230, 60))
        self.btn_del.setGeometry(72, 369, 230, 60)
        self.btn_del.clicked.connect(self.btn_del_click)

    def btn_add_click(self):
        self.form = Add()
        self.form.show()
        self.hide()

    def btn_del_click(self):
        self.form = Del()
        self.form.show()
        self.hide()


class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Добавление')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_add/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pic)

        # состояние катринки
        self.img_status = QLabel(self)
        self.img_status.setGeometry(32, 168, 114, 16)
        self.img_status.setText('Не загружено')

        # кнопка загрузки изображения
        self.btn_dow = QPushButton(self)
        self.btn_dow.setIcon(QIcon('win_add/btn_dow.jpg'))
        self.btn_dow.setIconSize(QSize(142, 37))
        self.btn_dow.setGeometry(188, 144, 142, 37)
        # self.btn_dow.clicked.connect(self.btn_dow_click)

        # ввод названия
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(32, 286, 298, 26)

        # ввод цены
        self.cost_input = QLineEdit(self)
        self.cost_input.setGeometry(32, 407, 298, 26)

        # ошибки
        self.mess = QLabel(self)
        self.mess.setGeometry(32, 540, 314, 16)

        # кнопка добавить
        self.btn_add = QPushButton(self)
        self.btn_add.setIcon(QIcon('win_add/btn_add.jpg'))
        self.btn_add.setIconSize(QSize(138, 42))
        self.btn_add.setGeometry(208, 591, 138, 42)
        self.btn_add.clicked.connect(self.btn_add_click)

    def btn_add_click(self):
        self.form = Confirmation()
        self.form.show()
        self.hide()


class Del(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Удаление')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_del/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pic)

        # кнопка назад
        self.btn_1 = QPushButton(self)
        self.btn_1.setIcon(QIcon('wid_order/btn1.jpg'))
        self.btn_1.setIconSize(QSize(72, 30))
        self.btn_1.setGeometry(5, 278, 72, 30)
        # self.btn_1.clicked.connect(self.btn_1_click)

        # кнопка вперёд
        self.btn_2 = QPushButton(self)
        self.btn_2.setIcon(QIcon('wid_order/btn3.jpg'))
        self.btn_2.setIconSize(QSize(72, 30))
        self.btn_2.setGeometry(299, 278, 72, 30)
        # self.btn_2.clicked.connect(self.btn_2_click)

        # картинка
        self.picture = QLabel(self)
        self.picture.setGeometry(98, 192, 180, 180)

        # название
        self.title = QLabel(self)
        self.title.setGeometry(83, 372, 209, 16)

        # ошибка
        self.mess = QLabel(self)
        self.mess.setGeometry(32, 540, 314, 16)

        # кнопка удалить
        self.btn_del = QPushButton(self)
        self.btn_del.setIcon(QIcon('win_del/btn_del.jpg'))
        self.btn_del.setIconSize(QSize(166, 42))
        self.btn_del.setGeometry(180, 591, 166, 42)
        self.btn_del.clicked.connect(self.btn_del_click)

    def btn_del_click(self):
        self.form = Confirmation()
        self.form.show()
        self.hide()


class Confirmation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 500, 375, 170)
        self.setWindowTitle('Подтверждение')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_pod/orig2.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 170)
        self.image.setPixmap(self.pic)

        self.btn_ok = QPushButton(self)
        self.btn_ok.setIcon(QIcon('win_pod/btn_ok.jpg'))
        self.btn_ok.setIconSize(QSize(116, 36))
        self.btn_ok.setGeometry(130, 116, 116, 36)
        self.btn_ok.clicked.connect(self.btn_ok_click)

    def btn_ok_click(self):
        self.hide()
