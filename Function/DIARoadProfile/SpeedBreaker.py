# Pothole
# Insalation
# pip3 install peakutils 
# pip3 install gmplot

import pandas as pd
import peakutils 
from peakutils.plot import plot as pplot
import matplotlib.pyplot as plt
import numpy as np


#def pothole(Accx,Accy,Accz)
df_File = pd.read_csv("../../Datasets/Dataset-1.csv")
time = df_File['Trip Time(Since journey start)(s)']

Accx = df_File['Acceleration Sensor(X axis)(g)']
Accy = df_File['Acceleration Sensor(Y axis)(g)']
Accz = df_File['Acceleration Sensor(Z axis)(g)']
Lat = df_File[' Latitude']
Longi = df_File[' Longitude']


x = np.array(time)
y = np.array(Accy)

indexes = peakutils.indexes(y, thres=0.35, min_dist=5)
#print(indexes)
#print(x[indexes], y[indexes])
plt.figure(figsize=(10,6))
pplot(x, y, indexes)
plt.title('Number of speed breakers')
plt.xlabel('Time')
plt.ylabel('Acceleration in the y direction')
plt.show()
#lati = [13.027313,13.026308,13.025118,13.023361,13.028859,13.033193,13.036492 ]
#long = [77.577713,77.580344,77.581661,77.584423,77.586206,77.588136,77.589162 ]
#gmap = gmplot.GoogleMapPlotter(12.9716,77.5946, 13)
#gmap.scatter(lati, long,'yellow',size = 10, marker = False) 
#gmap.draw("Potholes.html")
