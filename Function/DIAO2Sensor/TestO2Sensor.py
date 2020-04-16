import os
import unittest
import DIAO2Sensor
import pandas as pd
import matplotlib.pyplot as plt
import sys

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
                mean_value = DIAO2Sensor.O2_Sensor(df['O2 Volts Bank 1 sensor 1(V)'])
                plt.figure(figsize=(10, 6))
                plt.plot(df['Trip Time(Since journey start)(s)'][:100], df['O2 Volts Bank 1 sensor 1(V)'][:100],
                         marker='o', markerfacecolor='red')
                plt.axhline(y=0.45, color='r', linestyle='-', label='Ideal Condition')
                plt.axhline(y=0.8, color='g', linestyle='--', label='Rich Condition')
                plt.axhline(y=0.2, color='brown', linestyle='--', label='Lean Condition')
                plt.legend(loc='best')
                plt.xlabel("Trip Time in secs")
                plt.ylabel("O2 Sensor in volts")
                plt.savefig(path + '.png')
                plt.close()

        except:
            e = sys.exc_info()
            print("In Test Failed")
            f = open("Error_O2Sensor", "w")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")

if __name__ == '__main__':
    unittest.main()

