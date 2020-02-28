import unittest
import Speed_Voilation
import pandas as pd
import matplotlib.pyplot as plt
import os
class TestSpeed_Voilation(unittest.TestCase):
	def testspeed_violation(self):
		try:
			df_File = pd.read_excel("List_of_Data_Set.xlsx")
			os.system('mkdir Result')
			for i in df_File.index:
				df = pd.read_excel(str(df_File["Input_File_Name"][i]))
				Speed_violate=Speed_Voilation.speed_violation(df["Speed (GPS)(km/h)"],df["GPS Time"],df[' Latitude'],df[' Longitude'],20)
				t=df["Speed (GPS)(km/h)"]
				t2=t.replace(to_replace='-',value=0)
				plt.figure()
				plt.plot(t2,marker='o')
				plt.plot(Speed_violate['Index'],Speed_violate['Speed'], 'ro')
				t1=df_File["Input_File_Name"][i].split('/')
				t3=t1[-1].split('.')
				plt.savefig('Result/'+str(t3[0])+'.png')


			
		except AssertionError as e:
			f = open("Difference_Report_Speed_Voilation", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()


