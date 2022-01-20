from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from style import style
from Login import Ui_MainWindow4

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        Ui_MainWindow4.main2(self)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style)
    window = Window()
    window.show()
    sys.exit(app.exec_())

