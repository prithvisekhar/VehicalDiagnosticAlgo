import os
import sys
import Colour
import DataDriven
import pandas as pd 
import numpy as np
import MapPloting


VideoInput=sys.argv
os.system('ffmpeg -i '+str(VideoInput[1])+' -r 1/1 $filename%d.bmp')
path=os.getcwd()
ImageFiles = [f for f in os.listdir(path) if f.endswith('.bmp')]

for o in ImageFiles:
	g="python3 predict.py -c config.json -w trained_wts.h5 -i "+o
	os.system(g)
	os.remove(o)
	files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and 'Part_' in i]
	for j in files:
		Result = Colour.ColorThreshold(j)
		os.remove(j)
		if Result:
			FileName=os.path.splitext(o)
			os.remove(FileName[0]+'_detected.bmp')

ImageDetected= [f for f in os.listdir(path) if f.endswith('.bmp')]
		 
df_File = pd.read_csv('trackLog-2020-Mar-27_18-08-37.csv')
time = df_File['Trip Time(Since journey start)(s)']
Accx = df_File['Acceleration Sensor(X axis)(g)'] 
Accy = df_File['Acceleration Sensor(Y axis)(g)']
Accz = df_File['Acceleration Sensor(Z axis)(g)']
Lat = df_File[' Latitude']
time_np=np.array(time)

f = open("LogFile.csv", "w")
f.write("Trip Time in Seconds,ImageFile,PotholeValue,DataDriven, Longitude, Latitude\n")
for k in ImageDetected:
	t=k.split('_')
	idx=np.nonzero(time_np==int(t[0]))
	accy = DataDriven.highpassfilter(Accy[idx[0][0]:idx[0][0]+30])
	a,b,c=DataDriven.threshold(accy)
	if len(a)>0:
		c_array=np.array(c)
		f.write(str(df_File.iloc[int(np.average(c_array)+int(t[0])), 73])+','+str(k)+','+str(a)+','+'Confirmend With Data,'+str(df_File.iloc[int(np.average(c_array)+int(t[0])), 2])+','+ str(df_File.iloc[int(np.average(c_array)+int(t[0])), 3])+'\n')

		MapPloting.PlotingMap(float(df_File.iloc[int(np.average(c_array)+int(t[0])), 2]),float(df_File.iloc[int(np.average(c_array)+int(t[0])), 3]),str(t[0]))
		
#		print(c)
#		print(c_array)
#		print(np.average(c_array))
#		print(int(np.average(c_array)+int(t[0])))
#		print(df_File.iloc[int(np.average(c_array)+int(t[0])), 2])
		
	else:
		f.write(','+str(k)+', ,'+'Not Confirmend With Data ,, \n')
		
	
f.close()
