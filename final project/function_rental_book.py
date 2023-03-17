from pyuic.rental_book import Ui_RentaAddBooks
from PyQt5.QtWidgets import QWidget
import sqlite3
from datetime import datetime


class AddRentalForm(QWidget, Ui_RentaAddBooks):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.cursor = self.base_books.cursor()
        users_from_db = self.cursor.execute(f'''SELECT user_name FROM users''').fetchall()
        for i in users_from_db:
            self.box_readers_rental.addItem(i[0])
        book_rental = self.cursor.execute(f'''SELECT name FROM books''').fetchall()
        for i in book_rental:
            self.box_books_rental.addItem(i[0])
        self.btn_rental_book.clicked.connect(self.func_add_rental)

    def func_add_rental(self):
        books_in_db_rental = self.cursor.execute(f'''SELECT name FROM books WHERE id in 
        (SELECT book FROM rental) or id = (SELECT book FROM rental)''').fetchall()
        books_in_db_rental = [i[0] for i in books_in_db_rental]
        if self.box_books_rental.currentText() in books_in_db_rental:
            self.cursor.execute(f'''UPDATE rental
            SET date = "{datetime.now().strftime('%d-%m-%Y')}"
            WHERE book = (SELECT id FROM books WHERE name = "{self.box_books_rental.currentText()}")''')
        else:
            self.cursor.execute(f'''INSERT INTO rental(id_user,book,date) 
            VALUES((SELECT id FROM users WHERE user_name = "{self.box_readers_rental.currentText()}"), 
            (SELECT id FROM books WHERE name = "{self.box_books_rental.currentText()}"), 
            "{datetime.now().strftime('%d-%m-%Y')}")''')
        self.base_books.commit()

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()

