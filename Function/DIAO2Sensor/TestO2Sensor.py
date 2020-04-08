import os
import unittest
import pandas as pd
import DIAO2Sensor
import matplotlib.pyplot as plt


class Test_O2Sensor(unittest.TestCase):
    def testO2Sensor(self):
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
                mean_value = DIAO2Sensor.O2_Sensor\(df['02 Volts Bank 1 sensor 1(V)'])
                plt.figure()
                plt.plot(df['Trip Time(Since journey start)(s)'][0:100], df['O2 Volts Bank 1 sensor 1(V)'][0:100], marker='o', markerfacecolor='red')
                plt.show()
                plt.title("Trip Time vs O2 Sensor")
                plt.xlabel("Time")
                plt.ylabel("O2 in volts")
                plt.close()
        
        except AssertionError as e:
            print("In Test Failed")
            f = open("Error_O2Sensor", "w")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")


if __name__ == '__main__':
    unittest.main()
