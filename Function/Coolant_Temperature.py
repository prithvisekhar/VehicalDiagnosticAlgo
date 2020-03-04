"""!pip install shapely
!pip install geopandas
!pip install osmapi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from shapely.geometry import Point
#import geopandas as gpd
#import plotly.graph_objects as go
#import plotly.express as px
import os
# from Untitled1 import speed_violation
# To find the regions where the speed limit is exceeded

def coolant(coolant_temperature,engine_load,trip_time):
	coolant_temperature = coolant_temperature.astype(float)
	for i in range(0, len(coolant_temperature)):
		coolant_temperature[i] = (coolant_temperature[i]*9/5) +32
	for i in range(0, len(engine_load)):
		engine_load[i] = (float(engine_load[i]))
	for i in range(0, len(trip_time)):
		trip_time[i] = (int(trip_time[i]))
	engine_load_threshold = 0.50*max(engine_load)
	trip_time_threshold = 0.50*max(trip_time)
	Safestate=[]
	SafeState = pd.DataFrame(data=Safestate, columns=['Coolant_Temperature', 'Engine_Load','Trip_Time','Index'])				#"Engine is in safe state")
	UnSafestate=[]
	UnSafeState = pd.DataFrame(data=UnSafestate, columns=['Coolant_Temperature', 'Engine_Load','Trip_Time','Index'])				#"Engine is in safe state")
	safestate = 0
	lowesttemp = 0.0
	normaltemp = 190.0 			#Reference form internet safe state 190F to 220F
	highesttemp = 220.0
	for i in range(0, len(coolant_temperature)):
		if coolant_temperature[i] > normaltemp and coolant_temperature[i] < highesttemp:
			if trip_time[i] < trip_time_threshold:
				if engine_load[i] < engine_load_threshold:
					safestate += 1
			elif coolant_temperature[i] < normaltemp and coolant_temperature[i] > lowesttemp:
				safestate += 1
			elif coolant_temperature[i] > highesttemp:
				safestate -= 1
			if safestate > 400:
				Safestate.append([coolant_temperature[i], engine_load[i], trip_time[i], i])
				SafeState = pd.DataFrame(data=Safestate, columns=['Coolant_Temperature', 'Engine_Load','Trip_Time','Index'])				#"Engine is in safe state")
			else:
				UnSafestate.append([coolant_temperature[i], engine_load[i], trip_time[i], i])
				UnSafeState = pd.DataFrame(data=UnSafestate, columns=['Coolant_Temperature', 'Engine_Load','Trip_Time','Index'])			#"Engine is in danger state")

	return SafeState, UnSafeState, engine_load_threshold, trip_time_threshold