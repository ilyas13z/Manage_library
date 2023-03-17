from pyuic.base_form import Ui_BaseWindow
from function_catalog import CatalogForm
from function_readers import ReaderForm
from function_multyreader import AddReaderForm
from function_books import AddBookForm
from function_rental_book import AddRentalForm
from function_del_books import DelBookForm
from function_del_rental_reader import DelReaderRentalForm

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets


class BaseForm(QMainWindow, Ui_BaseWindow):
    def __init__(self, parent=None):
        super(BaseForm, self).__init__(parent)
        self.setupUi(self)
        self.btn_catalog.clicked.connect(self.view_catalog)
        self.btn_readers.clicked.connect(self.view_readers)
        self.btn_add_readers.clicked.connect(self.view_add_readers)
        self.btn_add_book.clicked.connect(self.view_add_book)
        self.btn_rental_books.clicked.connect(self.view_add_rental_book)
        self.btn_del_book_for_reader.clicked.connect(self.view_del_book_rental_from_reader)
        self.btn_del_book.clicked.connect(self.view_del_book)

    def view_catalog(self):
        self.catalog_form = CatalogForm()
        self.catalog_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_readers(self):
        self.reader_form = ReaderForm()
        self.reader_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_add_readers(self):
        self.add_reader_form = AddReaderForm()
        self.add_reader_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_add_book(self):
        self.add_book_form = AddBookForm()
        self.add_book_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_add_rental_book(self):
        self.add_book_form = AddRentalForm()
        self.add_book_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_del_book(self):
        self.del_book_form = DelBookForm()
        self.del_book_form.show(on_close=lambda event: self.show())
        self.hide()

    def view_del_book_rental_from_reader(self):
        self.del_book_form = DelReaderRentalForm()
        self.del_book_form.show(on_close=lambda event: self.show())
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BaseForm()
    w.show()
    sys.exit(app.exec_())
