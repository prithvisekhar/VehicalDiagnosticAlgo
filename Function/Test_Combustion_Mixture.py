import unittest
import Combustion_Mixture
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
				Lean, Rich, Nrml =Combustion_Mixture.combustion_mixture(df['O2 Volts Bank 1 sensor 2(V)'])
				#t=df["Speed (GPS)(km/h)"]
				#t2=t.replace(to_replace='-',value=0)
				plt.figure(1)
				plt.plot(Lean.loc[:, 'O2_Volts'], Lean.loc[:, 'Index'], 'r.')
				plt.plot(Rich.loc[:, 'O2_Volts'], Rich.loc[:, 'Index'], 'b.')
				plt.plot(Nrml.loc[:, 'O2_Volts'], Nrml.loc[:, 'Index'], 'g.')
				plt.title("Combustion Mixture")
				plt.savefig(path+"/Combustion_Mixture"+'.png')
	
		except AssertionError as e:
			f = open("Difference_Report_Speed_Voilation", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()
