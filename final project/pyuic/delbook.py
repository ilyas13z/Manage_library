from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteBooks(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(302, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_author_del_book = QtWidgets.QLabel(self.centralwidget)
        self.label_author_del_book.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_author_del_book.setFont(font)
        self.label_author_del_book.setObjectName("label")
        self.box_author_del = QtWidgets.QComboBox(self.centralwidget)
        self.box_author_del.setGeometry(QtCore.QRect(150, 10, 141, 21))
        self.box_author_del.setObjectName("box_author_del")
        self.label_name_del_book = QtWidgets.QLabel(self.centralwidget)
        self.label_name_del_book.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_del_book.setFont(font)
        self.label_name_del_book.setObjectName("label_2")
        self.box_book_del = QtWidgets.QComboBox(self.centralwidget)
        self.box_book_del.setGeometry(QtCore.QRect(150, 50, 141, 21))
        self.box_book_del.setObjectName("box_book_del")
        self.btn_del_ba = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_ba.setGeometry(QtCore.QRect(10, 90, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_del_ba.setFont(font)
        self.btn_del_ba.setObjectName("btn_del_ba")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_author_del_book.setText(_translate("MainWindow", "Имя автора"))
        self.label_name_del_book.setText(_translate("MainWindow", "Название книги"))
        self.btn_del_ba.setText(_translate("MainWindow", "Удалить"))
