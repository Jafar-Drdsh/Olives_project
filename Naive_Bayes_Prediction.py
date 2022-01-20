# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predicton.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QLabel, QFileDialog, QAction
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from NB_load import Ui_MainWindow2
import os.path



class Ui_MainWindow5(QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "NB_Prediction.ui")

    def __init__(self):
        super(Ui_MainWindow5, self).__init__()
        uic.loadUi(self.UI_FILE, self)

        self.pushButton_6.clicked.connect(self.predict)
        self.pushButton_2.clicked.connect(super(Ui_MainWindow5, self).close)
        self.pushButton_3.clicked.connect(self.openload)
        self.setWindowTitle("NB_Prediction")
        self.setWindowIcon(QIcon('Logo.png'))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

    def  openload(self):
        try:
            self.window = Ui_MainWindow2()
            self.window.show()
        except:
            print("")


    def predict(self):
        try:
            print('Step 2: Load and Pre-Process The Data .....')
            candidates = pd.read_excel(r'dataset-1.xlsx')
            df = pd.DataFrame(candidates, columns=['Y_%', 'G_%', 'B_%', 'Level of disease'])
            print(df)
            print(' ')

            print('Step 3: Subset The Data to build model .....')
            X = df[['Y_%', 'G_%', 'B_%']]
            y = df['Level of disease']
            print(' ')

            print('Step 4: Split The Data Into Train And Test Sets .....')
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
            print(type(X_train))
            print(type(y_train))
            print(' ')

            print('Step 5: Build A MultinomialNB Classifier .....')
            MultiNB = MultinomialNB()
            MultiNB.fit(X_train, y_train)
            print(1)

            print('Step 6: Prediction: use the model to predict for X_test and compare the result of prediction with y_test to measure the accuracy .....')
            print(' ')
            y_expect = y_test
            y_predict = MultiNB.predict(X_test)
            print(' ')
            print('The accuracy of MultinomialNB Classifier:', accuracy_score(y_expect, y_predict))
            print(' ')

            print('Step 7: Predictions for new data using MultinomialNB .....')
            print(' ')


            y = float(self.lineEdit_4.text())
            g = float(self.lineEdit_2.text())
            b = float(self.lineEdit_3.text())
            print(type(y))
            print(type(g))
            print(type(b))

            prediction1 =  MultiNB.predict([[y, g, b]])
            print('Predicted Result1 using NB Classifier: ', prediction1)
            print(' ')
            print(type(prediction1[0]))
            self.lineEdit.setText(prediction1[0])
        except:
            print("")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow5()
    window.show()
    sys.exit(app.exec_())

