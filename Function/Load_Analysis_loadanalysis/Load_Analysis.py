import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from shapely.geometry import Point

def loadanalysis(engine_load,engine_rpm,Vehicle_speed, tripTime):
	Gear_Ratio = 1.5
	AXLE_RATIO = 4
	TYRE_SIZE = 12
	EXPT_SPEED = []
	OVERLOAD_COUNTER = 0
	maxinload = 0
	maxinrpm = 0
	engine_loadLess = []
	engine_loadMore = []
	engine_rpmLess = []
	engine_rpmMore = []
	vehicleSpeedLess = []
	vehicleSpeedMore = []
	notOverloaded = []
	overloaded = []
	counter_overload = 0
	Engine_loadLess = pd.DataFrame(data=engine_loadLess, columns=['engine_load','Index'])
	Engine_loadMore = pd.DataFrame(data=engine_loadMore, columns=['engine_load','Index'])
	Engine_rpmLess = pd.DataFrame(data=engine_rpmLess, columns=['engine_rpm','Index'])
	Engine_rpmMore = pd.DataFrame(data=engine_rpmMore, columns=['engine_rpm','Index'])
	VehicleSpeedLess = pd.DataFrame(data=vehicleSpeedLess, columns=['Vehicle_speed','Index'])
	VehicleSpeedMore = pd.DataFrame(data=vehicleSpeedMore, columns=['Vehicle_speed','Index'])
	NotOverloaded = pd.DataFrame(data=notOverloaded, columns=['Trip_Time','Index'])
	Overloaded = pd.DataFrame(data=overloaded, columns=['Trip_Time','Index'])

	for i in range(len(engine_load)):
		if engine_load[i]== '-' :
			engine_load[i]= '0';
		if engine_rpm[i]== '-' :
			engine_rpm[i]= '0';
		engine_load[i] = float(engine_load[i])
		engine_rpm[i] = float(engine_rpm[i])
		
		if maxinload < engine_load[i]:
			maxinload = engine_load[i]

		if maxinrpm < engine_rpm[i]:
			maxinrpm = engine_rpm[i]
			
	load_threshold = 0.5 * maxinload
	rpm_threshold = 0.5 * maxinrpm
	
	for i in range(len(engine_rpm)):
		if Vehicle_speed[i]== '-' :
			Vehicle_speed[i]= '0';
		if tripTime[i]== '-' :
			tripTime[i]= '0';

		if(engine_load[i]<load_threshold):  # Checking whether vehicle speed is less than expected speed
			engine_loadLess.append([engine_load[i], i])
			Engine_loadLess = pd.DataFrame(data=engine_loadLess, columns=['engine_load','Index'])
		else:
			engine_loadMore.append([engine_load[i], i])
			Engine_loadMore = pd.DataFrame(data=engine_loadMore, columns=['engine_load','Index'])
		
		if(engine_rpm[i]<load_threshold):  # Checking whether vehicle speed is less than expected speed
			engine_rpmLess.append([engine_rpm[i], i])
			Engine_rpmLess = pd.DataFrame(data=engine_rpmLess, columns=['engine_rpm','Index'])
		else:
			engine_rpmMore.append([engine_rpm[i], i])
			Engine_rpmMore = pd.DataFrame(data=engine_rpmMore, columns=['engine_rpm','Index'])
			
		if engine_load[i] > load_threshold and  engine_rpm[i] > rpm_threshold:
			counter_overload = counter_overload + 1 # Checking whether engine load and engine rpm are less than threshold
		
		Vehicle_speed[i] = float(Vehicle_speed[i])
		
        #ACTUAL SPEED = (ENGINE RPM * PERIMETER OF TYRE)/(AXLE RATIO * GEAR RATIO)
		
		EXPT_SPEED = (engine_rpm[i] *60*3.14*2 *TYRE_SIZE*25.4*0.000001)/(Gear_Ratio*AXLE_RATIO)
		
		if(Vehicle_speed[i]<(0.4*EXPT_SPEED)):  # Checking whether vehicle speed is less than expected speed
			vehicleSpeedLess.append([Vehicle_speed[i], i])
			VehicleSpeedLess = pd.DataFrame(data=vehicleSpeedLess, columns=['Vehicle_speed','Index'])
			OVERLOAD_COUNTER = OVERLOAD_COUNTER + 1
		else:
			vehicleSpeedMore.append([Vehicle_speed[i], i])
			VehicleSpeedMore = pd.DataFrame(data=vehicleSpeedMore, columns=['Vehicle_speed','Index'])

		if counter_overload < 150 or OVERLOAD_COUNTER < 150:
			notOverloaded.append([float(tripTime[i]), i])
			NotOverloaded = pd.DataFrame(data=notOverloaded, columns=['Trip_Time','Index'])
		else:
			overloaded.append([float(tripTime[i]), i])
			Overloaded = pd.DataFrame(data=overloaded, columns=['Trip_Time','Index'])
			
	return Engine_loadLess, Engine_loadMore, Engine_rpmLess, Engine_rpmMore, VehicleSpeedLess, VehicleSpeedMore, NotOverloaded, Overloaded

