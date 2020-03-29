import unittest
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from importlib.machinery import SourceFileLoader

DIAEngineAnalysis = SourceFileLoader("LoadAnalysis",
                                     "../DIAEngineAnalysis.py").load_module()


class TestLoad_Analysis(unittest.TestCase):
    def testLoadAnalysis(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not os.path.isdir("Result"):
                os.mkdir("Result")
            for i in df_File.index:
                TempCounterOverload = []
                df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                TempFile1 = df_File["Input_File_Name"][i].split('/')
                TempFile3 = TempFile1[-1].split('.')
                TempFile4 = str(TempFile3[0])
                path = os.path.join("Result/", TempFile4)
                if not os.path.isdir(path):
                    os.mkdir(path)
                (EngineLoadLess, EngineLoadMore, EngineRPMLess, EngineRPMMore,
                 VehicleSpeedLess, VehicleSpeedMore, ExpectedSpeed, LoadThreshold,
                 RPMThreshold, CounterOverload) = DIAEngineAnalysis.LoadAnalysis(
                    df["Engine Load(%)"].replace(to_replace="-", value="0"),
                    df["Engine RPM(rpm)"].replace(to_replace="-", value="0"),
                    df['Speed (GPS)(km/h)'].replace(to_replace="-", value="0"),
                    df['Trip Time(Since journey start)(s)'])
                TempEngineLoad1 = df["Engine Load(%)"].replace(to_replace='-',
                                                               value=0)
                plt.figure(1)
                plt.plot(TempEngineLoad1, marker='o', label='Engine Load')
                plt.plot(EngineLoadLess['Index'],
                         EngineLoadLess['EngineLoad'], 'g.')
                plt.plot(EngineLoadMore['Index'],
                         EngineLoadMore['EngineLoad'], 'r.')
                plt.plot(np.repeat(LoadThreshold, len(TempEngineLoad1)),
                         label='Threshold = ' + str(round(LoadThreshold)))
                plt.plot(CounterOverload, label='Counter Overload *10')
                plt.ylabel('Engine Load(%)')
                plt.title("Engine Load")
                plt.xlabel('Index')
                plt.legend(loc='lower right')
                plt.savefig(path + "/Engine_Load.png")
                plt.close()
                plt.figure(2)
                TempSpeed = df['Speed (GPS)(km/h)'].replace(to_replace='-',
                                                            value=0)
                plt.plot(TempSpeed, marker='o', label='Speed')
                plt.plot(ExpectedSpeed, label='Expected Speed *0.4')
                plt.plot(VehicleSpeedLess['Index'],
                         VehicleSpeedLess['VehicleSpeed'], 'g.')
                plt.plot(VehicleSpeedMore['Index'],
                         VehicleSpeedMore['VehicleSpeed'], 'r.')
                plt.ylabel('Speed (GPS)(km/h)')
                plt.title("Speed")
                plt.xlabel('Index')
                plt.legend(loc='lower right')
                plt.savefig(path + "/Vehicle_Speed" + '.png')
                plt.close()

                TempEngineRPM1 = df["Engine RPM(rpm)"].replace(to_replace='-', value=0)
                plt.figure(3)
                plt.plot(TempEngineRPM1, marker='o', label='Engine RPM')
                plt.plot(EngineRPMLess['Index'],
                         EngineRPMLess['EngineRPM'], 'g.')
                plt.plot(EngineRPMMore['Index'],
                         EngineRPMMore['EngineRPM'], 'r.')
                plt.plot((np.repeat(RPMThreshold, len(TempEngineRPM1)),
                          label='Threshold = ' + str(round(LoadThreshold)))
                for x in CounterOverload:
                    TempCounterOverload.append(x * 10)
                plt.plot(TempCounterOverload, label='Counter Overload')
                plt.ylabel('Engine RPM(rpm)')
                plt.title("Engine RPM")
                plt.xlabel('Index')
                plt.legend(loc='lower right')
                plt.savefig(path + "/Engine_RPM.png")
                plt.close()

        except AssertionError as e:
            f = open("Difference_Report_Speed_Voilation", "a")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")


if __name__ == '__main__':
    unittest.main()
