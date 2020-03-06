"""Function checks for speed voilation at the certain location."""

import pandas as pd

def speed_violation(speed, Latitude,Longitude,Threshold_Speed):
	SPEED_VIOLATION = []
	for i in speed.index:
		if speed[i]== '-' :
			speed[i]=0
		if (float(speed[i])>Threshold_Speed):
			SPEED_VIOLATION.append([Latitude[i],Longitude[i],speed[i],i])
	VIOLATION = pd.DataFrame(data=SPEED_VIOLATION, columns=['Latitude', 'Longitude','Speed','Index'])
	return VIOLATION
