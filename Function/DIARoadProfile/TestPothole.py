import unittest
import DIAPothole
import pandas as pd
import matplotlib.pyplot as plt
import os


class Test_Pothole(unittest.TestCase):
    def testPothole(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not (os.path.isdir("Result")):
                os.mkdir("Result")
            for i in df_File.index:
                df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                TempFile1 = df_File["Input_File_Name"][i].split('/')
                TempFile3 = TempFile1[-1].split('.')
                TempFile4 = str(TempFile3[0])
                path = os.path.join("Result/", TempFile4)
                Location = DIAPothole.PotholeDetection(
                    df['Trip Time(Since journey start)(s)'].replace('-', 0),
                    df['Acceleration Sensor(Y axis)(g)'].replace('-', 0),
                    df[' Latitude'],
                    df[' Longitude'])
                plt.figure()
                plt.plot(Location['Latitude'], Location['Longitude'], 'r.',
                         label='Lean')

                plt.title("Pot Holes")
                plt.ylabel('Longitude')
                plt.xlabel('Latitude')
                plt.legend(loc='lower right')
                plt.savefig(path + '.png')
                plt.close()

        except AssertionError as e:
            f = open("Error_Pothole", "a")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")
