import unittest
import DistAvg
import pandas as pd
import matplotlib.pyplot as plt
import os


class TestDistAvg(unittest.TestCase):
    def testDistAvg(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not(os.path.isdir("Result")):
                os.mkdir("Result")
                for i in df_File.index:
                    df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                    TempFile1 = df_File["Input_File_Name"][i].split('/')
                    TempFile3 = TempFile1[-1].split('.')
                    TempFile4 = str(TempFile3[0])
                    path = os.path.join("Result/", TempFile4)
                    DistanceToZero = DistAvg.AverageDistance(df['Trip Distance(km)'].replace(to_replace="-", value="0"), df['Fuel Remaining (Calculated from vehicle profile)(%)'].replace(to_replace="-", value="0"), df['Kilometers Per Litre(Instant)(kpl)'].replace(to_replace="-", value="0"))
                    plt.plot(DistanceToZero.loc[:, 'DistanceToZero'], DistanceToZero.loc[:, 'Index'], 'r.')
                    plt.title("Distance To Zero")
                    plt.savefig(path+"Distance To Zero"+'.png')
                    fig.savefig(path+'.png')
        except AssertionError as e:
            f = open("ErrorMessage", "a")
            f.write(str(e)+" \n")

if __name__ == '__main__':
    unittest.main()
