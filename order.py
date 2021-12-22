import sqlite3

from PyQt5.QtGui import QPixmap, QIcon, QPicture
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize


class Order(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.open_db()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Заказ')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('wid_order/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pic)

        # кнопка назад
        self.btn1 = QPushButton(self)
        self.btn1.setIcon(QIcon('wid_order/btn1.jpg'))
        self.btn1.setIconSize(QSize(72, 30))
        self.btn1.setGeometry(5, 218, 72, 30)
        self.btn1.clicked.connect(self.btn1_click)

        # кнопка вперёд
        self.btn2 = QPushButton(self)
        self.btn2.setIcon(QIcon('wid_order/btn3.jpg'))
        self.btn2.setIconSize(QSize(72, 30))
        self.btn2.setGeometry(299, 218, 72, 30)
        self.btn2.clicked.connect(self.btn2_click)

        # кнопка добавить
        self.btn3 = QPushButton(self)
        self.btn3.setIcon(QIcon('wid_order/btn2.jpg'))
        self.btn3.setIconSize(QSize(87, 24))
        self.btn3.setGeometry(214, 341, 87, 24)
        self.btn3.clicked.connect(self.btn3_click)

        # кнопка заказать
        self.btn4 = QPushButton(self)
        self.btn4.setIcon(QIcon('wid_order/btn4.jpg'))
        self.btn4.setIconSize(QSize(138, 42))
        self.btn4.setGeometry(218, 605, 138, 42)
        self.btn4.clicked.connect(self.btn_order_click)

        # введение имени
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(77, 49, 222, 26)

        # картинка
        self.picture = QLabel(self)
        self.picture.setGeometry(98, 132, 180, 180)

        # название блюда
        self.title = QLabel(self)
        self.title.setGeometry(83, 312, 209, 16)

        # количество
        self.count_input = QLineEdit(self)
        self.count_input.setGeometry(77, 343, 32, 20)
        self.count_input.setText('0')

        # цена
        self.cost = QLabel(self)
        self.cost.setGeometry(118, 349, 80, 18)
        self.cost.setText('по 0 руб')

        # заказ
        self.order_list = QLabel(self)
        self.order_list.setGeometry(77, 412, 222, 163)

    def btn_order_click(self):
        # доработать!

        self.form = Confirmation()
        self.form.show()
        self.hide()

    def open_db(self):
        self.connect = sqlite3.connect('cafe_db.db')
        self.cur = self.connect.cursor()

        self.menu = self.cur.execute('''
                                SELECT * FROM menu
                                WHERE id > 0''').fetchall()

        # print(self.menu)
        self.start()

    def start(self):
        self.number = 1
        self.order = []
        self.picture.setPixmap(QPixmap(f'cafe/{self.menu[0][0]}.png'))
        self.title.setText(self.menu[0][1])
        self.cost.setText(f'по {self.menu[0][2]} руб')

    def btn1_click(self):
        self.count_input.setText('0')
        if self.number > 1:
            self.number -= 1
            self.picture.setPixmap(QPixmap(f'cafe/{self.menu[self.number - 1][0]}.png'))
            self.title.setText(self.menu[self.number - 1][1])
            self.cost.setText(f'по {self.menu[self.number - 1][2]} руб')
        else:
            self.number = 19
            self.picture.setPixmap(QPixmap(f'cafe/{self.menu[self.number - 1][0]}.png'))
            self.title.setText(self.menu[self.number - 1][1])
            self.cost.setText(f'по {self.menu[self.number - 1][2]} руб')

    def btn2_click(self):
        self.count_input.setText('0')
        if self.number < len(self.menu):
            self.number += 1
            self.picture.setPixmap(QPixmap(f'cafe/{self.menu[self.number - 1][0]}.png'))
            self.title.setText(self.menu[self.number - 1][1])
            self.cost.setText(f'по {self.menu[self.number - 1][2]} руб')
        else:
            self.number = 1
            self.picture.setPixmap(QPixmap(f'cafe/{self.menu[self.number - 1][0]}.png'))
            self.title.setText(self.menu[self.number - 1][1])
            self.cost.setText(f'по {self.menu[self.number - 1][2]} руб')

    def btn3_click(self):
        if self.count_input.text() != '0' and self.count_input.text().isdigit():
            self.order.append([self.count_input.text(), self.menu[self.number - 1][0]])
            self.order_list.setText('')
            for i in range(len(self.order)):
                name = self.cur.execute(f"""SELECT title FROM menu WHERE id = {self.order[i][1]}""").fetchone()
                self.order_list.setText(self.order_list.text() +
                                        f'{self.order[i][0]} шт - {name[0]}\n')


class Confirmation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 500, 375, 170)
        self.setWindowTitle('Подтверждение')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_pod/orig1.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 170)
        self.image.setPixmap(self.pic)

        self.btn_ok = QPushButton(self)
        self.btn_ok.setIcon(QIcon('win_pod/btn_ok.jpg'))
        self.btn_ok.setIconSize(QSize(116, 36))
        self.btn_ok.setGeometry(130, 116, 116, 36)
        self.btn_ok.clicked.connect(self.btn_ok_click)

    def btn_ok_click(self):
        self.form = Enjoy()
        self.form.show()
        self.hide()


class Enjoy(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('Приятного аппетита')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_enj/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 667)
        self.image.setPixmap(self.pic)

        # на столе
        self.label = QLabel(self)
        self.label.setGeometry(55, 137, 265, 289)

        # кнопка оплаты
        self.btn = QPushButton(self)
        self.btn.setIcon(QIcon('win_enj/btn_opl.jpg'))
        self.btn.setIconSize(QSize(138, 42))
        self.btn.setGeometry(210, 605, 138, 42)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.form = Pay()
        self.form.show()
        self.hide()


class Pay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 500, 375, 170)
        self.setWindowTitle('Оплата')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_che/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 170)
        self.image.setPixmap(self.pic)

        # ввод
        self.card_input = QLineEdit(self)
        self.card_input.setGeometry(35, 51, 305, 26)

        # предупреждение при ошибке
        self.mess = QLabel(self)
        self.mess.setGeometry(35, 89, 192, 16)

        # кнопка ок
        self.btn_ok = QPushButton(self)
        self.btn_ok.setIcon(QIcon('win_che/btn_ok.jpg'))
        self.btn_ok.setIconSize(QSize(116, 36))
        self.btn_ok.setGeometry(130, 117, 116, 36)
        self.btn_ok.clicked.connect(self.btn_ok_click)

    def btn_ok_click(self):
        self.form = GoodDay()
        self.form.show()
        self.hide()


class GoodDay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 500, 375, 170)
        self.setWindowTitle('Хорошего дня!')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.pic = QPixmap('win_goo/orig.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 375, 170)
        self.image.setPixmap(self.pic)

        self.btn = QPushButton(self)
        self.btn.setIcon(QIcon('win_goo/btn.jpg'))
        self.btn.setIconSize(QSize(157, 36))
        self.btn.setGeometry(109, 117, 157, 36)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.hide()