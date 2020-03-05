import unittest
import DIA_Fuel_Mixture
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
class TestFuel_Mixture(unittest.TestCase):
	def testFuelMixture(self):
		try:
			df_File = pd.read_csv("List_of_Data_Set.csv")
			if not(os.path.isdir("Result")):
				os.mkdir("Result")
			
			for i in df_File.index:
				df = pd.read_excel(str(df_File["Input_File_Name"][i]))
				t1=df_File["Input_File_Name"][i].split('/')
				t3=t1[-1].split('.')
				t4=str(t3[0])
				path=os.path.join("Result/" , t4)
				Lean, Rich, Nrml =DIA_Fuel_Mixture.Fuel_Mixture(df['O2 Volts Bank 1 sensor 2(V)'])
				t=df['O2 Volts Bank 1 sensor 2(V)']
				t2=t.replace(to_replace='-',value=0)
				plt.figure()

				plt.plot(np.repeat(0.1,len(t2)))
				plt.plot(t2,marker='o',label='O2 Bank1')
				plt.plot(Lean['Index'],Lean['O2_Volts'],'r.',label='Lean')
				plt.plot(Rich['Index'],Rich['O2_Volts'],'y.',label='Rich')
				plt.plot(Nrml['Index'],Nrml['O2_Volts'],'g.',label='Normal')
				plt.title("Fuel Mixture")
				plt.ylabel('O2 in Volts')
				plt.xlabel('Index')
				plt.legend(loc='lower right')
				plt.savefig(path+'.png')
				plt.close()
	
		except AssertionError as e:
			f = open("Error_Fuel_Mixture", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()
