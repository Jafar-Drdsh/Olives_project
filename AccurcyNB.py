# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accurcy.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import xlrd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
import os.path


class Ui_MainWindow7(QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "AccurcyNB.ui")

    def __init__(self):
        super(Ui_MainWindow7, self).__init__()
        uic.loadUi(self.UI_FILE, self)


        try:
            file_name, _ = QFileDialog.getOpenFileName(QFileDialog(), 'Open xlsx File', r"<Default dir>", "xlsx files (*.xlsx)")
            self.z =  file_name
            self.anomaly_details = xlrd.open_workbook(r""+self.z+"")
            self.sheet = self.anomaly_details.sheet_by_index(0)
            self.data1 = pd.read_excel(self.z)
            self.df = pd.DataFrame(self.data1)

            self.df.fillna(self.df.mean(), inplace=True)

            X = self.df[['Y_%', 'G_%', 'B_%']]
            y = self.df['Level of disease']
            y.fillna('level 0', inplace=True)
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.25, random_state=1)  # 75% training and 30% test
            self.data=[self.X_test.columns.values.tolist()] + X.values.tolist()


            self.tableWidget.setColumnCount(len(self.X_test.columns))
            self.tableWidget.setRowCount(len(self.X_test))  # same no.of rows as of csv file
            for row, columnvalues in enumerate(self.data):
                for column, value in enumerate(columnvalues):
                    self.item = QtWidgets.QTableWidgetItem(str(value))  # str is to also display the integer values
                    self.tableWidget.setItem(row - 0, column, self.item)
                    # to set the elements read only
                    self.item.setFlags(QtCore.Qt.ItemIsEnabled)
        except:
            print("")
        self.pushButton.clicked.connect(self.NB_check)
        self.pushButton_2.clicked.connect(super(Ui_MainWindow7, self).close)


        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(159,87,43);")
        self.setWindowTitle("NB-Accurcy")
        self.setWindowIcon(QIcon('Logo.png'))
        self.lineEdit.setAlignment(Qt.AlignCenter)





    def NB_check(self):
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
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
            print(' ')

            print('Step 5: Build A MultinomialNB Classifier .....')
            MultiNB = MultinomialNB()
            MultiNB.fit(X_train, y_train)
            print(' ')

            print(
                'Step 6: Prediction: use the model to predict for X_test and compare the result of prediction with y_test to measure the accuracy .....')
            print(' ')
            y_expect = y_test
            y_predict = MultiNB.predict(X_test)
            print(' ')
            print('The accuracy of MultinomialNB Classifier:', accuracy_score(y_expect, y_predict) * 100)
            print(' ')
            accurcy = str(accuracy_score(y_expect, y_predict) * 100)
            self.lineEdit.setText(accurcy[0:5])
        except:
            print("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow7()
    window.show()
    sys.exit(app.exec_())

