import unittest
import Traffic
import pandas as pd
import matplotlib.pyplot as plt
import os


class TestTraffic(unittest.TestCase):
    def testTraffic(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            os.system('mkdir Result')
            for i in df_File.index:
                df = pd.read_csv(df_File["Input_File_Name"][i])
                t1 = df_File["Input_File_Name"][i].split('/')
                t3 = t1[-1].split('.')
                t4 = str(t3[0])
                path = os.path.join("Result/", t4)
                os.mkdir(path)
                # os.chdir(path)
                df["Speed (GPS)(km/h)"] = \
                    df["Speed (GPS)(km/h)"].astype("float")
                HC, MC, LC = Traffic.traffic(
                    df["Speed (GPS)(km/h)"].replace('-', 0),
                    df[' Latitude'], df[' Longitude'])
                t = df["Speed (GPS)(km/h)"]
                t2 = t.replace(to_replace='-', value=0)
                plt.figure(1)
                plt.plot(HC.loc[:, 'Longitude'], HC.loc[:, 'Latitude'], 'r.')
                plt.plot(MC.loc[:, 'Longitude'], MC.loc[:, 'Latitude'], 'b.')
                plt.plot(LC.loc[:, 'Longitude'], LC.loc[:, 'Latitude'], 'g.')
                plt.title("Congestion Location")
                plt.savefig(path + "/Congestion Location" + '.png')

                plt.figure(2)
                plt.plot(HC.loc[:, 'Speed'], HC.loc[:, 'Index'], 'r.')
                plt.plot(MC.loc[:, 'Speed'], MC.loc[:, 'Index'], 'b.')
                plt.plot(LC.loc[:, 'Speed'], LC.loc[:, 'Index'], 'g.')
                plt.title("Speed vs Index")
                plt.savefig(path + "/Speed vs Index" + '.png')

                plt.figure(3)
                """plt.plot(HC.loc[:, 'Latitude'], HC.loc[:, 'Index'], 'r.')
                plt.plot(MC.loc[:, 'Latitude'], MC.loc[:, 'Index'], 'b.')
                plt.plot(LC.loc[:, 'Latitude'], LC.loc[:, 'Index'], 'g.')"""
                plot1('Latitude','Longitude','r.',HC)
                plot1('Latitude','Longitude','b.',MC)
                plot1('Latitude','Longitude','g.',LC)
                plt.title("Latitude vs Index")
                plt.savefig(path + "/Latitude vs Index" + '.png')

                plt.figure(4)
                plt.plot(HC.loc[:, 'Longitude'], HC.loc[:, 'Index'], 'r.')
                plt.plot(MC.loc[:, 'Longitude'], MC.loc[:, 'Index'], 'b.')
                plt.plot(LC.loc[:, 'Longitude'], LC.loc[:, 'Index'], 'g.')
                plt.title("Longitude vs Index")
                plt.savefig(path + "/Longitude vs Index" + '.png')

        # os.system('cd..')

        except AssertionError as e:
            f = open("Difference_Report_Speed_Voilation", "a")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")


if __name__ == '__main__':
    unittest.main()

def plot1(point1, point2, colour, dataset)
    plt.plot(dataset.loc[:, point1], dataset.loc[:, point2], colour'.')
