from pyuic.multyreader import Ui_AddReaders
from PyQt5.QtWidgets import QWidget
import sqlite3


class AddReaderForm(QWidget, Ui_AddReaders):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add_reader.clicked.connect(self.func_add_reader)
        self.base_books = sqlite3.connect("./assets/base_lib")

    def func_add_reader(self):
        self.label_error.setStyleSheet('')
        self.label_error.setText('')
        name_reader = self.name_reader.text()
        if name_reader == '':
            self.label_error.setText(f'Поле пустое')
            self.label_error.setStyleSheet("background-color: #ff6161")
        else:
            cursor = self.base_books.cursor()
            count = cursor.execute(f'''SELECT user_name FROM users 
                                    WHERE user_name = "{name_reader}"''').fetchall()
            if len(count) > 0:
                self.label_error.setText(f'Читатель {name_reader} существует')
                self.label_error.setStyleSheet("background-color: #ff6161")
            else:
                cursor.execute(f'''INSERT INTO users(user_name) VALUES("{name_reader}") ''')
                self.label_error.setText(f'Читатель {name_reader} добавлен')
                self.label_error.setStyleSheet("background-color: #a5ed9d")
            self.name_reader.setText('')
            self.base_books.commit()
            cursor.close()

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)