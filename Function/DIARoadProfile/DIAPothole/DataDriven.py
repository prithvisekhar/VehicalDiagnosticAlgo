from __future__ import division
import gmplot
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import peakutils 
import scipy



def highpassfilter(Accelerometer_values):
	fc = 0.2  
	b = 0.16  
	N = int(np.ceil((4 / b)))
	if not N % 2: N += 1  # Make sure that N is odd.
	n = np.arange(N)
 
	#Compute a low-pass filter.
	h = np.sinc(2 * fc * (n - (N - 1) / 2))
	w = np.blackman(N)
	h = h * w
	h = h / np.sum(h)
 
	#Create a high-pass filter from the low-pass filter through spectral inversion.
	h = -h
	h[(N - 1) // 2] += 1
	s = np.convolve(Accelerometer_values, h)
	np.set_printoptions(suppress=False)
	s1=s.astype(float) #amplifying the output by 10 times for further computation
	return s1

def threshold(list):
	values = np.array(list)
	confirmed_potholes = values[values<-0.2]
	indexvalues_confirmed = np.nonzero(list <-0.2)
	rest = np.array(list[list>-0.2])
	possible_potholes = rest[rest<-0.1]
	return confirmed_potholes,possible_potholes,indexvalues_confirmed


#df_File = pd.read_csv('trackLog-2020-Mar-27_18-08-37.csv')          #Target Variable
#time = df_File['Trip Time(Since journey start)(s)']
#Accx = df_File['Acceleration Sensor(X axis)(g)']
#Accy = df_File['Acceleration Sensor(Y axis)(g)']
#Accz = df_File['Acceleration Sensor(Z axis)(g)']
#Lat = df_File[' Latitude']
#Longi = df_File[' Longitude']

#accy = highpassfilter(Accy)
#accx = highpassfilter(Accx)



#print(max(accy))
#print(min(accy)) 


#print(max(accx))
#print(min(accx))

#print(threshold(accy))

