from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReadersList(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(792, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.readers_table = QtWidgets.QTableWidget(self.centralwidget)
        self.readers_table.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.readers_table.setObjectName("readers_table")
        self.readers_table.setColumnCount(0)
        self.readers_table.setRowCount(0)
        self.label_list_readers = QtWidgets.QLabel(self.centralwidget)
        self.label_list_readers.setGeometry(QtCore.QRect(20, 10, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_list_readers.setFont(font)
        self.label_list_readers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_list_readers.setObjectName("label_list_readers")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_list_readers.setText(_translate("MainWindow", "Список читателей"))
