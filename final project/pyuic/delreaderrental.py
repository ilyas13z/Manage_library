from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteReaders(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(366, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name_reader_rental = QtWidgets.QLabel(self.centralwidget)
        self.label_name_reader_rental.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_reader_rental.setFont(font)
        self.label_name_reader_rental.setObjectName("label_name_reader_rental")
        self.box_del_rental_reader = QtWidgets.QComboBox(self.centralwidget)
        self.box_del_rental_reader.setGeometry(QtCore.QRect(140, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_del_rental_reader.setFont(font)
        self.box_del_rental_reader.setObjectName("box_del_rental_reader")
        self.btn_del_rental_bor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_rental_bor.setGeometry(QtCore.QRect(10, 70, 351, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_del_rental_bor.setFont(font)
        self.btn_del_rental_bor.setObjectName("btn_del_rental_bor")
        self.box_del_rental_book = QtWidgets.QComboBox(self.centralwidget)
        self.box_del_rental_book.setGeometry(QtCore.QRect(140, 40, 221, 21))
        self.box_del_rental_book.setObjectName("box_del_rental_book")
        self.label_name_book_rental = QtWidgets.QLabel(self.centralwidget)
        self.label_name_book_rental.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_book_rental.setFont(font)
        self.label_name_book_rental.setObjectName("label_name_book_rental")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name_reader_rental.setText(_translate("MainWindow", "Имя читателя"))
        self.btn_del_rental_bor.setText(_translate("MainWindow", "Удалить у читателя книгу с проката"))
        self.label_name_book_rental.setText(_translate("MainWindow", "Имя книги"))

