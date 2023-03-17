from pyuic.delreaderrental import Ui_DeleteReaders
from PyQt5.QtWidgets import QWidget
import sqlite3


class DelReaderRentalForm(QWidget, Ui_DeleteReaders):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.cursor = self.base_books.cursor()
        users_from_db = self.cursor.execute(f'''SELECT user_name FROM users''').fetchall()
        self.box_del_rental_reader.currentTextChanged.connect(self.Event)
        for i in users_from_db:
            self.box_del_rental_reader.addItem(i[0])
        self.btn_del_rental_bor.clicked.connect(self.func_del_rental)

    def Event(self):
        self.box_del_rental_book.clear()
        id_users = self.cursor.execute(f'''SELECT id FROM users WHERE user_name = 
        "{self.box_del_rental_reader.currentText()}"''').fetchone()
        books_rental = self.cursor.execute(f'''SELECT book FROM rental WHERE id_user = 
        "{list(id_users)[0]}"''').fetchall()
        list_books_rental = [i[0] for i in books_rental]
        if len(list_books_rental) > 1:
            rental_books_from_db = self.cursor.execute(
                f'''SELECT name FROM books WHERE id in {tuple(list_books_rental)}''').fetchall()
        elif len(list_books_rental) == 1:
            rental_books_from_db = self.cursor.execute(
                f'''SELECT name FROM books WHERE id = {list_books_rental[0]}''').fetchall()
        else:
            rental_books_from_db = ''
        for i in rental_books_from_db:
            self.box_del_rental_book.addItem(i[0])

    def func_del_rental(self):
        self.cursor.execute(f'''DELETE from rental WHERE book = 
        (SELECT id FROM books WHERE name = "{self.box_del_rental_book.currentText()}")''')
        self.box_del_rental_book.removeItem(self.box_del_rental_book.currentIndex())
        self.base_books.commit()

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()