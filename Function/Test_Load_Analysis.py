import unittest
import Load_Analysis
import pandas as pd
import matplotlib.pyplot as plt
import os
class TestTraffic(unittest.TestCase):
	def testTraffic(self):
		try:
			df_File = pd.read_csv("List_of_Data_Set.csv")
			os.system('mkdir Result')
			for i in df_File.index:
				df = pd.read_excel(str(df_File["Input_File_Name"][i]))
				t1=df_File["Input_File_Name"][i].split('/')
				t3=t1[-1].split('.')
				t4=str(t3[0])
				path=os.path.join("Result/" , t4)
				os.mkdir(path)
				#os.chdir(path)
				Engine_loadLess, Engine_loadMore, Engine_rpmLess, Engine_rpmMore, VehicleSpeedLess, VehicleSpeedMore, NotOverloaded, Overloaded = Load_Analysis.loadanalysis(df["Engine Load(%)"], df["Engine RPM(rpm)"],df['Speed (GPS)(km/h)'],df['Trip Time(Since journey start)(s)'])
				t=df["Speed (GPS)(km/h)"]
				t2=t.replace(to_replace='-',value=0)
				plt.figure(1)
				#plt.plot(Engine_loadLess.loc[:, 'engine_load'], Engine_loadLess.loc[:, 'Index'], 'r.')
				plt.plot(Engine_loadLess['engine_load'], Engine_loadLess['Index'], 'r.')
				plt.plot(Engine_loadMore['engine_load'], Engine_loadMore['Index'], 'b.')
				plt.title("Engine Load")
				plt.savefig(path+"/Engine Load"+'.png')
				
				plt.figure(2)
				plt.plot(Engine_rpmLess.loc[:, 'engine_rpm'], Engine_rpmLess.loc[:, 'Index'], 'r.')
				plt.plot(Engine_rpmMore.loc[:, 'engine_rpm'], Engine_rpmMore.loc[:, 'Index'], 'b.')
				plt.title("engine_rpm")
				plt.savefig(path+"/engine_rpm"+'.png')
	
				plt.figure(3)
				plt.plot(VehicleSpeedLess.loc[:, 'Vehicle_speed'], VehicleSpeedLess.loc[:, 'Index'], 'r.')
				plt.plot(VehicleSpeedMore.loc[:, 'Vehicle_speed'], VehicleSpeedMore.loc[:, 'Index'], 'b.')
				plt.title("Vehicle_speed")
				plt.savefig(path+"/Vehicle_speed"+'.png')
				
				plt.figure(4)
				plt.plot(NotOverloaded.loc[:, 'Trip_Time'], NotOverloaded.loc[:, 'Index'], 'r.')
				plt.plot(Overloaded.loc[:, 'Trip_Time'], Overloaded.loc[:, 'Index'], 'b.')
				plt.title("Overload")
				plt.savefig(path+"/Overload"+'.png')
				
				#os.system('cd..')
				
		except AssertionError as e:
			f = open("Difference_Report_Speed_Voilation", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()
