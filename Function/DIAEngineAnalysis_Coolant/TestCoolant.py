import unittest
import DIAEngineAnalysis
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

class TestCoolant_Temperature(unittest.TestCase):
	def testCoolantTemperature(self):
		try:
			df_File = pd.read_csv("List_of_Data_Set.csv")
			if not(os.path.isdir("Result")):
				os.mkdir("Result")
			for i in df_File.index:
				temp_coolant_temperature_F=[]

				df = pd.read_excel(str(df_File["Input_File_Name"][i]))
				TempFile1=df_File["Input_File_Name"][i].split('/')
				TempFile3=TempFile1[-1].split('.')
				TempFile4=str(TempFile3[0])
				path=os.path.join("Result/",TempFile4)


				CoolantTemperatureF_np,HighestTemperatureC,NormalTemperatureC,LowestTemperatureC,SafeState1,SafeState2,SafeState3,State0,IndexTripTimeThreshold,EngineLoadThreshold=DIAEngineAnalysis.Coolant(df['Engine Coolant Temperature(Â°C)'].replace(to_replace="-", value="0"),df['Engine Load(%)'].replace(to_replace="-", value="0"),df['Trip Time(Since journey start)(s)'].replace(to_replace="-", value="0"))




				TempEngineLoad=df['Engine Load(%)'].replace(to_replace="-", value="0")
				TempEngineLoad_np=np.asarray(TempEngineLoad)
				TempEngineLoad_np=TempEngineLoad_np.astype(float)

				fig, axs = plt.subplots(3)
				axs[0].plot(CoolantTemperatureF_np,'y')
				axs[0].plot(SafeState1['Index'],CoolantTemperatureF_np[SafeState1['Index']],'g.')
				axs[0].plot(SafeState2['Index'],CoolantTemperatureF_np[SafeState2['Index']],'r.')
				axs[0].plot(SafeState3['Index'],CoolantTemperatureF_np[SafeState3['Index']],'k.')
				


				axs[1].plot(State0,'y')
				axs[1].plot(SafeState1['Index'],SafeState1['Safestate'],'g.')
				axs[1].plot(SafeState2['Index'],SafeState2['Safestate'],'r.')
				axs[1].plot(SafeState3['Index'],SafeState3['Safestate'],'k.')
				#axs[1].title.set_text("Coolant Temperature in F")

				axs[2].plot(TempEngineLoad_np,'y')
				axs[2].plot(np.repeat(EngineLoadThreshold,len(TempEngineLoad_np)))
				axs[2].plot(SafeState1['Index'],TempEngineLoad_np[SafeState1['Index']],'g.')



				axs[1].axvline(x=IndexTripTimeThreshold)
				axs[0].axvline(x=IndexTripTimeThreshold)
				axs[2].axvline(x=IndexTripTimeThreshold)

				
				fig.savefig(path+'.png')	





			
		except AssertionError as e:
			f = open("Error Message", "a")
			f.write(str(e)+" \n")

if __name__ == '__main__':
	unittest.main()

