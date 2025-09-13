from PyQt5.QtGui import QColor
from pyuic.readers import Ui_ReadersList
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import sqlite3
from datetime import datetime, timedelta


class ReaderForm(QWidget, Ui_ReadersList):
    on_close = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_books = sqlite3.connect("./assets/base_lib")
        self.initUI()

    def initUI(self):
        self.readers_table.setColumnCount(3)
        self.readers_table.setRowCount(0)
        condition_books = self.base_books.cursor().execute(f'''SELECT users.user_name, books.name, rental.date 
                                FROM rental
                                INNER JOIN users 
                                ON users.id = rental.id_user
                                INNER JOIN books 
                                ON rental.book = books.id ORDER BY users.user_name''').fetchall()
        for i, row in enumerate(condition_books):
            self.readers_table.setRowCount(
                self.readers_table.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 0:
                    self.readers_table.setItem(
                        i, 0, QTableWidgetItem(row[0]))
                elif j == 1:
                    self.readers_table.setItem(
                        i, 1, QTableWidgetItem(row[1]))
                else:
                    date_check = datetime.today() - timedelta(days=30)
                    self.readers_table.setItem(i, 2, QTableWidgetItem(row[2]))
                    if datetime.strptime(row[2], '%d-%m-%Y') >= date_check:
                        self.readers_table.item(i, 2).setBackground(QColor('green'))
                    else:
                        self.readers_table.item(i, 2).setBackground(QColor('red'))

        self.readers_table.setHorizontalHeaderLabels(('Читатель', 'Книга', 'Дата выдачи'))
        self.readers_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

    def show(self, on_close=None):
        super().show()
        self.on_close = on_close

    def closeEvent(self, event):
        if self.on_close:
            self.on_close(event)
        self.base_books.close()