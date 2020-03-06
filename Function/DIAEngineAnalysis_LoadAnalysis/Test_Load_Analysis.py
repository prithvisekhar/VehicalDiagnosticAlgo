import unittest
import DIAEngineAnalysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
class TestTraffic(unittest.TestCase):
	def testTraffic(self):
		try:
			
			df_File = pd.read_csv("List_of_Data_Set.csv")
			if not os.path.isdir("Result"):
				os.mkdir("Result")
			for i in df_File.index:
				temp_counter_overload=[]
				df = pd.read_excel(str(df_File["Input_File_Name"][i]))
				TempFile1=df_File["Input_File_Name"][i].split('/')
				TempFile3=TempFile1[-1].split('.')
				TempFile4=str(TempFile3[0])
				path=os.path.join("Result/" , TempFile4)
				if not os.path.isdir(path):
					os.mkdir(path)


				Engine_loadLess, Engine_loadMore, Engine_rpmLess, Engine_rpmMore, VehicleSpeedLess, VehicleSpeedMore, EXPT_SPEED,load_threshold,rpm_threshold,counter_overload = DIAEngineAnalysis.LoadAnalysis(df["Engine Load(%)"], df["Engine RPM(rpm)"],df['Speed (GPS)(km/h)'],df['Trip Time(Since journey start)(s)'])
				temp_Engine_Load1=df["Engine Load(%)"].replace(to_replace='-',value=0)
				plt.figure(1)
				plt.plot(temp_Engine_Load1,marker='o',label='Engine Load')
				plt.plot(Engine_loadLess['Index'],Engine_loadLess['engine_load'],'g.')
				plt.plot(Engine_loadMore['Index'],Engine_loadMore['engine_load'],'r.')
				plt.plot(np.repeat(load_threshold,len(temp_Engine_Load1)),label='Threshold = '+str(round(load_threshold)))
				plt.plot(counter_overload,label='Counter Overload *10')
				plt.ylabel('Engine Load(%)')
				plt.title("Engine Load")
				plt.xlabel('Index')
				plt.legend(loc='lower right')
				plt.savefig(path+"/Engine_Load.png")
				plt.close()
			

				plt.figure(2)
				temp_Speed=df['Speed (GPS)(km/h)'].replace(to_replace='-',value=0)
				plt.plot(temp_Speed,marker='o',label='Speed')
				plt.plot(EXPT_SPEED,label='Expected Speed *0.4')
				plt.plot(VehicleSpeedLess['Index'],VehicleSpeedLess['Vehicle_speed'],'g.')
				plt.plot(VehicleSpeedMore['Index'],VehicleSpeedMore['Vehicle_speed'],'r.')
				plt.ylabel('Speed (GPS)(km/h)')
				plt.title("Speed")
				plt.xlabel('Index')
				plt.legend(loc='lower right')
				plt.savefig(path+"/Vehicle_Speed"+'.png')
				plt.close()
				
				temp_Engine_RPM1=df["Engine RPM(rpm)"].replace(to_replace='-',value=0)
				plt.figure(3)
				plt.plot(temp_Engine_RPM1,marker='o',label='Engine RPM')
				plt.plot(Engine_rpmLess['Index'],Engine_rpmLess['engine_rpm'],'g.')
				plt.plot(Engine_rpmMore['Index'],Engine_rpmMore['engine_rpm'],'r.')
				plt.plot(np.repeat(rpm_threshold,len(temp_Engine_RPM1)),label='Threshold = '+str(round(load_threshold)))
				for x in counter_overload:
					temp_counter_overload.append(x * 10)
				plt.plot(temp_counter_overload,label='Counter Overload')
				plt.ylabel('Engine RPM(rpm)')
				plt.title("Engine RPM")
				plt.xlabel('Index')
				plt.legend(loc='lower right')
				plt.savefig(path+"/Engine_RPM.png")
				plt.close()
	
		except AssertionError as e:
			f = open("Difference_Report_Speed_Voilation", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()
