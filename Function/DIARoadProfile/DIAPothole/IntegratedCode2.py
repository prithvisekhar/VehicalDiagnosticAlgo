import os
import sys
import Colour
import DataDriven
import pandas as pd 
import numpy as np
import MapPloting
import datetime

VideoInput=sys.argv

df_File = pd.read_csv('trackLog-2020-Mar-27_18-08-37.csv')
time = df_File['Trip Time(Since journey start)(s)']
Accx = df_File['Acceleration Sensor(X axis)(g)'] 
Accy = df_File['Acceleration Sensor(Y axis)(g)']
Accz = df_File['Acceleration Sensor(Z axis)(g)']
Lat = df_File[' Latitude']
time_np=np.array(time)


#accy = highpassfilter(Accy)
#accx = highpassfilter(Accx)
accy = DataDriven.highpassfilter(Accy)
a,b,c=DataDriven.threshold(accy)

print(a)
print(b)
print(c[0])
#print(type(c[0][0]))

#print(c[0][0]-20)
k=1
path=os.getcwd()
for i1 in c[0]:
	t=str(datetime.timedelta(seconds =int(time_np[i1])-20)) 
	g="ffmpeg -ss "+str(t)+" -i "+str(VideoInput[1])+" -t "+"00:00:20"+" -c copy "+str(k)+".mp4"
	
	os.system(g)
	os.system('ffmpeg -i '+str(k)+".mp4"+' -r 1/1 $filename%d.bmp')
	os.remove(str(k)+".mp4")
	ImageFiles = [f for f in os.listdir(path) if f.endswith('.bmp')]
	k=k+1
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
			else:
				FileName=os.path.splitext(o)
				os.system('mkdir Result')
				os.replace(FileName[0]+'_detected.bmp', "Result/"+str(k-1)+"_"+FileName[0]+'_detected.bmp')


