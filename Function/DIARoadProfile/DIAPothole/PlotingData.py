import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import DataDriven

path=os.getcwd()

ImageDetected= [f for f in os.listdir(path) if f.endswith('.bmp')]
		 
df_File = pd.read_csv('trackLog-2020-Mar-27_18-08-37.csv')
time = df_File['Trip Time(Since journey start)(s)']
Accx = df_File['Acceleration Sensor(X axis)(g)'] 
Accy = df_File['Acceleration Sensor(Y axis)(g)']
Accz = df_File['Acceleration Sensor(Z axis)(g)']
Lat = df_File[' Latitude']
time_np=np.array(time)

k='61_detected.bmp'
t=k.split('_')
idx=np.nonzero(time_np==int(t[0]))
accy = DataDriven.highpassfilter(Accy[idx[0][0]:idx[0][0]+30])
a,b,c=DataDriven.threshold(accy)

print(len(time_np[idx[0][0]:idx[0][0]+len(accy)]))
plt.figure(1)
plt.plot(time_np[idx[0][0]:idx[0][0]+len(accy)],accy,label='Vertical Acceleration')
plt.plot(time_np[idx[0][0]+c[0]],a,'r.',markersize=10,label='Pot Hole')
#plt.plot(np.repeat(-0.1,len(accy)),label='-0.1')
#plt.plot(np.repeat(-0.2,len(accy)),label='-0.2')

plt.axhline(y=-0.1, color='m', linestyle='-',label='-0.1 Possibility Threshold of Pothole ')
plt.axhline(y=-0.2, color='y', linestyle='-',label='-0.2 Confirmation Threshold of Pothole ')
plt.title("Pothole Detection with Filtered Acceleration Data.")
plt.ylabel('Acceleration After High Pass Filter')
plt.xlabel('Time in Seconds')

plt.legend(loc='upper right')
plt.savefig('1.png')
print(a)
print(c[0])
plt.show()
