from pyuic.delbook import Ui_DeleteBooks
from PyQt5.QtWidgets import QWidget
import sqlite3


class DelBookForm(QWidget, Ui_DeleteBooks):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.cursor = self.base_books.cursor()
        authors_from_db = self.cursor.execute(f'''SELECT author FROM authors''').fetchall()
        self.convert_id_in_name = ''
        self.box_author_del.addItem('')
        for i in authors_from_db:
            self.box_author_del.addItem(i[0])
        self.box_author_del.currentTextChanged.connect(self.Event)
        self.btn_del_ba.clicked.connect(self.func_del_book_from_db)


    def Event(self):
        self.box_book_del.clear()
        if self.box_author_del.currentText() != '':
            self.convert_id_in_name = self.cursor.execute(f'''SELECT id FROM authors 
            WHERE author = "{self.box_author_del.currentText()}"''').fetchall()[0][0]
            books_from_db = self.cursor.execute(f'''SELECT name FROM books WHERE author 
            = {self.convert_id_in_name}''').fetchall()
            for i in books_from_db:
                self.box_book_del.addItem(i[0])

    def func_del_book_from_db(self):
        self.cursor.execute(f'''DELETE from books WHERE 
        author = {self.convert_id_in_name} AND name = "{self.box_book_del.currentText()}"''')
        self.box_book_del.removeItem(self.box_book_del.currentIndex())
        self.base_books.commit()

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()
