from PyQt5 import QtWidgets, uic, QtGui
import sys
from modules import excel


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('excel.ui', self)

        self.setWindowTitle('My Excel')

        self.buttonOpen: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.buttonOpen.triggered.connect(self.action_open)

        self.buttonSave: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionSave')
        self.buttonSave.triggered.connect(self.action_save)

        self.buttonExit: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionExit')
        self.buttonExit.triggered.connect(self.action_exit)

        self.tableWidget: QtWidgets.QTableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        # self.tableWidget.doubleClicked.connect(self.slotDoubleClicked)

        self.show()

    def slotDoubleClicked(self, mi):
        print('double click')

    def action_save(self):
        print('save')

    def action_open(self):
        print('open')

    def action_exit(self):
        print('exit')


app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec_()
