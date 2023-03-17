from pyuic.catalog import Ui_CatalogList
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QWidget
import sqlite3


class CatalogForm(QWidget, Ui_CatalogList):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.clicked.connect(self.func_search)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.book = self.base_books.cursor().execute('''SELECT * FROM books ORDER BY name''').fetchall()
        self.condition_clmn = self.base_books.cursor().execute(
            f'''SELECT name FROM books WHERE id in 
        (SELECT book FROM rental) or id = (SELECT book FROM rental)''').fetchall()
        self.condition_clmn = [i[0] for i in self.condition_clmn]
        self.select_data(self.book)

    def select_data(self, books_from_db):
        self.catalog_table.setColumnCount(4)
        self.catalog_table.setRowCount(0)
        for i, row in enumerate(books_from_db):
            self.catalog_table.setRowCount(
                self.catalog_table.rowCount() + 1)
            author = self.base_books.cursor().execute(
                f'''SELECT author FROM authors
                    WHERE id =
                (SELECT author FROM books
                    WHERE  author == {row[2]})''').fetchall()
            for j, elem in enumerate(row):
                if j == 2:
                    self.catalog_table.setItem(
                        i, j, QTableWidgetItem(str(*author[0])))
                    if row[1] in self.condition_clmn:
                        self.catalog_table.setItem(
                            i, 3, QTableWidgetItem('В прокате'))
                else:
                    self.catalog_table.setItem(
                        i, j, QTableWidgetItem(str(elem)))

        self.catalog_table.setHorizontalHeaderLabels(('№', 'Название книги', 'Автор', 'Состояние'))
        self.catalog_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.catalog_table.setColumnWidth(2, 200)
        self.catalog_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.catalog_table.setColumnWidth(0, 30)
        self.catalog_table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.catalog_table.setColumnWidth(3, 200)
        self.catalog_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

    def func_search(self):
        searh_text = self.search.text()
        if searh_text == '':
            self.select_data(self.book)
        else:
            books_from_bd = self.base_books.cursor().execute(
                f'''SELECT * FROM books WHERE name LIKE "%{searh_text}%"
                or name LIKE "%{searh_text.capitalize()}%"''').fetchall()
            self.select_data(books_from_bd)

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()
