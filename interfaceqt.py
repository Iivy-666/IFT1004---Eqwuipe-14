import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from qtdesigncode import Ui_MainWindow


class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):

        # """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        # End main UI
        self.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
