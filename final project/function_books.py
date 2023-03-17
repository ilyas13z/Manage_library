from pyuic.multybook import Ui_AddBooks
from PyQt5.QtWidgets import QWidget
import sqlite3


class AddBookForm(QWidget, Ui_AddBooks):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add_ab.clicked.connect(self.func_add_book)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.chekbox_author.stateChanged.connect(self.Event)
        self.cursor = self.base_books.cursor()
        authors = self.cursor.execute(f'''SELECT author FROM authors''').fetchall()
        self.authors_list = [i[0] for i in authors]
        for i in authors:
            self.box_add_author.addItem(i[0])

    def Event(self):
        if self.chekbox_author.isChecked():
            self.box_add_author.setEnabled(False)
            self.label_add_author.setEnabled(False)
            self.line_add_new_author.setEnabled(True)
        else:
            self.box_add_author.setEnabled(True)
            self.label_add_author.setEnabled(True)
            self.line_add_new_author.setEnabled(False)
            self.line_add_new_author.setText('')

    def func_add_book(self):
        self.label_warning.setText('')
        if self.chekbox_author.isChecked():
            author_get = self.line_add_new_author.text()
            if author_get in self.authors_list:
                self.label_warning.setText('Такой автор существует')
            else:
                self.cursor.execute(f'''INSERT INTO authors(author) 
                VALUES("{author_get}") ''')
                self.authors_list.append(author_get)
                self.base_books.commit()
                self.line_add_new_author.setText('')
        else:
            author_get = self.box_add_author.currentText()
        if self.add_name_book.text():
            get_books = self.cursor.execute(f'''SELECT name FROM books''').fetchall()
            get_books = [i[0] for i in get_books]
            if author_get in self.authors_list and self.add_name_book.text() in get_books:
                self.label_warning.setText('Книга не добавлена, так как такая\nкнига с этим автором существует')
            else:
                author_get_from_db = self.cursor.execute(f'''SELECT id FROM authors 
                WHERE author = "{author_get}"''').fetchall()
                self.cursor.execute(f'''INSERT INTO books(name,author) 
                VALUES("{self.add_name_book.text()}", {author_get_from_db[0][0]})''')
                self.base_books.commit()
                self.label_warning.setText('Книга добавлена')
                self.add_name_book.setText('')

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()
