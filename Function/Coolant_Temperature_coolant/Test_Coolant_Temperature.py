import unittest
import Coolant_Temperature
import pandas as pd
import matplotlib.pyplot as plt
import os

class TestCoolant_Temperature(unittest.TestCase):
	def testCoolantTemperature(self):
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
				SS, US, ELT, TTT=Coolant_Temperature.coolant(df['Engine Coolant Temperature(Â°C)'].replace(to_replace="-", value="0"),df['Engine Load(%)'].replace(to_replace="-", value="0"),df['Trip Time(Since journey start)(s)'].replace(to_replace="-", value="0"))
				#t=df["Engine Coolant Temperature(Â°C)"]
				#t2=t.replace(to_replace='-',value=0)
				plt.figure(1)
				#plt.plot(t2,marker='o')
				#fig, Cool=plt.subplots(2)
				plt.plot(SS['Coolant_Temperature'],SS['Index'], 'b')
				plt.plot(US['Coolant_Temperature'],US['Index'], 'r')
				plt.title("Coolant_Temperature vs Index")
				plt.savefig(path+"/Coolant_Temperature vs Index"+'.png')
				
				plt.figure(2)
				#plt.plot(t2,marker='o')
				plt.plot(SS['Coolant_Temperature'],SS['Engine_Load'], 'b')
				plt.plot(US['Coolant_Temperature'],US['Engine_Load'], 'r')
				plt.title("Coolant_Temperature vs Engine_Load")
				plt.savefig(path+"/Coolant_Temperature vs Engine_Load"+'.png')
				
				plt.figure(3)
				#plt.plot(t2,marker='o')
				plt.plot(SS['Coolant_Temperature'],SS['Trip_Time'], 'b')
				plt.plot(US['Coolant_Temperature'],US['Trip_Time'], 'r')
				plt.title("Coolant_Temperature vs Index")
				plt.savefig(path+"/Coolant_Temperature vs Trip_Time"+'.png')


			
		except AssertionError as e:
			f = open("Difference_Report_Speed_Voilation", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()

