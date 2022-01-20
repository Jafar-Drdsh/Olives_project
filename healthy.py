import cv2
import pandas as pd
import numpy as np


image_Path = 'healthy_images\\0.jpg'
xlsx_Path = 'healthy_dataset\d_0.xlsx'

Y_percentage_array = []
G_percentage_array = []
B_percentage_array = []
count = 0

while (count <=96) :

    Y_percentage_List = []
    G_percentage_List = []
    B_percentage_List = []

    Y_sum = 0.0
    G_sum = 0.0
    B_sum = 0.0

    Leave_data = 0
    Y_percentage = 0
    G_percentage = 0
    B_percentage = 0
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
        # cv2.imshow('original image', frame)
        #
        # cv2.imshow('y', y_mask)
        # cv2.imshow('g', g_mask)
        # cv2.imshow('b', b_mask)
        #
        # cv2.waitKey(0)
        # cv2.destroyWindow('MyWindow')

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

        Y_percentage_array.insert(count, Y_percentage)
        G_percentage_array.insert(count, G_percentage)
        B_percentage_array.insert(count, B_percentage)

        for i in range(len(b)):

            if (i == 0):
                Y_percentage_List.insert(i, Y_percentage)
                G_percentage_List.insert(i, G_percentage)
                B_percentage_List.insert(i, B_percentage)

            else:
                Y_percentage_List.insert(i, '---')
                G_percentage_List.insert(i, '---')
                B_percentage_List.insert(i, '---')

        try:
            df = pd.DataFrame(
                {'Y': y, 'G': g, 'B': b, 'Y_%': Y_percentage_List, 'G_%': G_percentage_List, 'B_%': B_percentage_List})
            df.to_excel(xlsx_Path)
        except:
            print("large")

    except:
        print("MOM")

    count = count + 1
    count_cast = str(count)

    jpg = ".jpg"
    diseased_images_file = 'healthy_images\\'
    datasetFile = "healthy_dataset"
    datasetFile1 = "\d_"
    xlsx = ".xlsx"

    image_Path = "".join([diseased_images_file,count_cast, jpg])
    xlsx_Path = "".join([datasetFile, datasetFile1,count_cast,xlsx])
    print(count)


df = pd.DataFrame({'Y_%': Y_percentage_array, 'G_%': G_percentage_array, 'B_%': B_percentage_array})
df.to_excel(xlsx_Path)

print(Y_percentage)
print(G_percentage)
print(B_percentage)
