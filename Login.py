import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from sql_conn_class import sql
from MainPage import Ui_Form


class Ui_MainWindow4(QtWidgets.QMainWindow, sql):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "Log1.ui")

    def __init__(self):
        super(Ui_MainWindow4, self).__init__()
        uic.loadUi(self.UI_FILE, self)

        self.pushButton_2.clicked.connect(self.login)
        self.pushButton.clicked.connect(super(Ui_MainWindow4, self).close)
        self.setWindowTitle("Log-in")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.setWindowIcon(QIcon('Logo.png'))

        # sql.insert(self)
        sql.select(self,'SELECT * FROM test.dbo.login')

    def login(self):

        username = self.lineEdit_2.text()
        password = self.lineEdit.text()

        query = 'SELECT * FROM test.dbo.login Where username = \'%s\' AND password = \'%s\'' % (password, username)
        print(query)

        isUserExist = sql.isExist(self, query)

        if isUserExist:
            Ui_Form.main1(self)
        else:
            self.mess_warning('Existance', 'No')


    def mess_correct(self,title,message):
        mess = QMessageBox()
        mess.setText(message)
        mess.setWindowTitle(title)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

    def mess_warning(self,title,message):
        mess = QMessageBox()
        mess.setText(message)
        mess.setWindowTitle(title)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


    def main2(self):
        import sys
        app1 = QtWidgets.QApplication(sys.argv)
        window1 = Ui_MainWindow4()
        window1.show()
        sys.exit(app1.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow4()
    window.show()
    sys.exit(app.exec_())