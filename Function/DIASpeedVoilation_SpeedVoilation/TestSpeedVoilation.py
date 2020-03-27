import unittest
import DIASpeedVoilation
import pandas as pd
import matplotlib.pyplot as plt
import os


class TestSpeed_Voilation(unittest.TestCase):
    def testSpeedViolation(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not(os.path.isdir("Result")):
                os.mkdir("Result")
            for i in df_File.index:
                df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                SpeedViolate = DIASpeedVoilation.SpeedVoilation(df["Speed (GPS)(km/h)"], df[' Latitude'], df[' Longitude'], 20)
                TempSpeed = df["Speed (GPS)(km/h)"].replace(to_replace='-', value=0)
                plt.figure()
                plt.plot(TempSpeed, marker='o')
                plt.plot(SpeedViolate['Index'], SpeedViolate['Speed'], 'ro')
                TempFile1 = df_File["Input_File_Name"][i].split('/')
                TempFile3 = TempFile1[-1].split('.')
                plt.savefig('Result/'+str(TempFile3[0])+'.png')
        except AssertionError as e:
            f = open("Difference_Report_Speed_Voilation", "a")
            f.write("TestCase_no_0:\n\t"+str(e)+" \n")
if __name__ == '__main__':
    unittest.main()
