# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import  cv2
import numpy as np
import os.path

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MainWindow2(QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "load2.ui")

    def __init__(self):
        super(Ui_MainWindow2, self).__init__()
        uic.loadUi(self.UI_FILE, self)

        self.pushButton_3.clicked.connect(super(Ui_MainWindow2, self).close)
        self.pushButton.clicked.connect(self.get_image_file)
        self.pushButton_2.clicked.connect(self.predict)
        self.pushButton_7.clicked.connect(self.gallery)
        self.pushButton_8.clicked.connect(self.Next)
        self.pushButton_6.clicked.connect(self.Prev)
        self.pushButton_4.clicked.connect(self.on_zoom_out)
        self.pushButton_5.clicked.connect(self.on_zoom_in)
        self.setWindowTitle("NB-Load")
        self.setWindowIcon(QIcon('Logo.png'))
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)



    Dict = {}
    Dict1 = {}
    C = 0
    def get_image_file(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(QFileDialog(), 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")


            self.imageLabel = QLabel()

            self.image = QPixmap(file_name)

            self.imageLabel.setPixmap(self.image)
            self.scrollArea.setWidget(self.imageLabel)
            self.height = self.image.height()

            image_Path = file_name


            Y_percentage_array = []
            G_percentage_array = []
            B_percentage_array = []

            Y_percentage_List = []
            G_percentage_List = []
            B_percentage_List = []

            Y_sum = 0.0
            G_sum = 0.0
            B_sum = 0.0


            global Y_percentage
            global G_percentage
            global B_percentage

            try:
                frame = cv2.imread(image_Path)
                hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                yellow_lower = np.array([20, 100, 100])
                yellow_upper = np.array([30, 255, 255])
                y_mask = cv2.inRange(hsvframe, yellow_lower, yellow_upper)
                y = y_mask.flatten().tolist()

                green_lower1 = np.array([20, 0, 0])
                green_upper1 = np.array([120, 100, 100])
                g_mask = cv2.inRange(hsvframe, green_lower1, green_upper1)
                g = g_mask.flatten().tolist()

                brouwn_lower1 = np.array([20, 10, 0])
                brouwn_upper1 = np.array([35, 255, 88])
                b_mask = cv2.inRange(hsvframe, brouwn_lower1, brouwn_upper1)
                b = b_mask.flatten().tolist()

                for i in range(len(b)):
                    Y_sum = Y_sum + y[i]
                    G_sum = G_sum + g[i]
                    B_sum = B_sum + b[i]

                try:
                    Leave_data = Y_sum + G_sum + B_sum
                    Y_percentage = (Y_sum / Leave_data) * 100.0
                    G_percentage = (G_sum / Leave_data) * 100.0
                    B_percentage = (B_sum / Leave_data) * 100.0

                except ZeroDivisionError:
                    Y_percentage = 0
                    G_percentage = 0
                    B_percentage = 0

                Y_percentage_array.insert(1, Y_percentage)
                G_percentage_array.insert(1, G_percentage)
                B_percentage_array.insert(1, B_percentage)

                for i in range(len(b)):

                    if (i == 0):
                        Y_percentage_List.insert(i, Y_percentage)
                        G_percentage_List.insert(i, G_percentage)
                        B_percentage_List.insert(i, B_percentage)

                    else:
                        Y_percentage_List.insert(i, '---')
                        G_percentage_List.insert(i, '---')
                        B_percentage_List.insert(i, '---')

            except:
                print("NON")


            print(Y_percentage)
            print(G_percentage)
            print(B_percentage)

            Ui_MainWindow2.Dict[Ui_MainWindow2.C] = file_name
        except:
            print("")

    def on_zoom_in(self, event):
        try:
            self.height += 50
            self.resize_image()
        except:
            print("")
    def on_zoom_out(self, event):
        try:
            self.height -= 100
            self.resize_image()
        except:
            print("")
    def resize_image(self):
        scaled_pixmap = self.image.scaledToHeight(self.height)
        self.imageLabel.setPixmap(scaled_pixmap)


    def predict(self):
        try:
            print('Step 2: Load and Pre-Process The Data .....')
            candidates = pd.read_excel(r'dataset-11.xlsx')
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

            print(
                'Step 6: Prediction: use the model to predict for X_test and compare the result of prediction with y_test to measure the accuracy .....')
            print(' ')
            y_expect = y_test
            y_predict = MultiNB.predict(X_test)
            print(' ')
            print('The accuracy of MultinomialNB Classifier:', accuracy_score(y_expect, y_predict))
            print(' ')

            print('Step 7: Predictions for new data using MultinomialNB .....')
            print(' ')

            y = Y_percentage
            g = G_percentage
            b = B_percentage

            self.prediction1 =  MultiNB.predict([[y, g, b]])
            print('Predicted Result1 using NB Classifier: ', self.prediction1)
            print(' ')
            print(type(self.prediction1[0]))
            self.lineEdit_3.setText(self.prediction1[0])
            Ui_MainWindow2.Dict1[Ui_MainWindow2.C] = self.prediction1[0]
            Ui_MainWindow2.C = Ui_MainWindow2.C + 1

            print(Ui_MainWindow2.Dict[0])
            print(Ui_MainWindow2.Dict1[0])
        except:
            print("")


    def gallery(self):
        try:
            Path = Ui_MainWindow2.Dict[0]
            self.image = QPixmap(Path)
            self.label_4.setPixmap(self.image)
            self.label_4.resize(401,311)
            self.label_4.setScaledContents(True)
            self.lineEdit_2.setText(Ui_MainWindow2.Dict1[0])
        except:
            self.label_4.setText("")

    countnext = 0
    def Next (self):
        try:
            Path = Ui_MainWindow2.Dict[Ui_MainWindow2.countnext]
            self.image = QPixmap(Path)
            self.label_4.setPixmap(self.image)
            self.label_4.resize(401,311)
            self.label_4.setScaledContents(True)
            self.lineEdit_2.setText(Ui_MainWindow2.Dict1[Ui_MainWindow2.countnext])
            Ui_MainWindow2.countnext = Ui_MainWindow2.countnext + 1


        except:
            self.label_4.setText("")
            Ui_MainWindow2.countnext = 0

        print(Ui_MainWindow2.countnext)


    countprev = 0
    def Prev(self):
        try:
            Path = Ui_MainWindow2.Dict[Ui_MainWindow2.countprev]
            self.image = QPixmap(Path)
            self.label_4.setPixmap(self.image)
            self.label_4.resize(401,311)
            self.label_4.setScaledContents(True)
            self.lineEdit_2.setText(Ui_MainWindow2.Dict1[Ui_MainWindow2.countprev])
            Ui_MainWindow2.countprev = Ui_MainWindow2.countprev +1



        except:
            self.label_4.setText("")
            Ui_MainWindow2.countprev = 0

        print(Ui_MainWindow2.countprev)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow2()
    window.show()
    sys.exit(app.exec_())

