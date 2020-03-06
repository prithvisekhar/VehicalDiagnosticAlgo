"""Function checks the load on the system and returns whether it is overloaded or not."""

import numpy as np
import pandas as pd
def LoadAnalysis(engine_load,engine_rpm,Vehicle_speed, tripTime):
	Gear_Ratio = 1.5
	AXLE_RATIO = 4
	TYRE_SIZE = 12
	EXPT_SPEED = []
	maxinload = 0
	maxinrpm = 0
	engine_loadLess = []
	engine_loadMore = []
	engine_rpmLess = []
	engine_rpmMore = []
	vehicleSpeedLess = []
	vehicleSpeedMore = []

	counter_overload = []
	temp_counter_overload=0
	Engine_loadLess = pd.DataFrame(data=engine_loadLess, columns=['engine_load','Index'])
	Engine_loadMore = pd.DataFrame(data=engine_loadMore, columns=['engine_load','Index'])
	Engine_rpmLess = pd.DataFrame(data=engine_rpmLess, columns=['engine_rpm','Index'])
	Engine_rpmMore = pd.DataFrame(data=engine_rpmMore, columns=['engine_rpm','Index'])
	VehicleSpeedLess = pd.DataFrame(data=vehicleSpeedLess, columns=['Vehicle_speed','Index'])
	VehicleSpeedMore = pd.DataFrame(data=vehicleSpeedMore, columns=['Vehicle_speed','Index'])

	for i in engine_load.index:
		if engine_load[i] == '-' :
			engine_load[i] = '0';
		if engine_rpm[i] == '-' :
			engine_rpm[i] = '0';
		engine_load[i] = float(engine_load[i])
		engine_rpm[i] = float(engine_rpm[i])

		if maxinload < engine_load[i]:
			maxinload = engine_load[i]

		if maxinrpm < engine_rpm[i]:
			maxinrpm = engine_rpm[i]

	load_threshold = 0.5 * maxinload
	rpm_threshold = 0.5 * maxinrpm

	for i in engine_rpm.index:
		if Vehicle_speed[i] == '-' :
			Vehicle_speed[i]= '0';
		if tripTime[i] == '-' :
			tripTime[i] = '0';

		if(engine_load[i]<load_threshold):  # Checking whether vehicle speed is less than expected speed
			engine_loadLess.append([engine_load[i], i])
			Engine_loadLess = pd.DataFrame(data=engine_loadLess, columns=['engine_load','Index'])
		else:
			engine_loadMore.append([engine_load[i], i])
			Engine_loadMore = pd.DataFrame(data=engine_loadMore, columns=['engine_load','Index'])

		if(engine_rpm[i]<rpm_threshold):  # Checking whether vehicle speed is less than expected speed
			engine_rpmLess.append([engine_rpm[i], i])
			Engine_rpmLess = pd.DataFrame(data=engine_rpmLess, columns=['engine_rpm','Index'])
		else:
			engine_rpmMore.append([engine_rpm[i], i])
			Engine_rpmMore = pd.DataFrame(data=engine_rpmMore, columns=['engine_rpm','Index'])

		if engine_load[i] > load_threshold and  engine_rpm[i] > rpm_threshold:
			temp_counter_overload = temp_counter_overload + 1 # Checking whether engine load and engine rpm are less than threshold
		counter_overload.append(temp_counter_overload)

		Vehicle_speed[i] = float(Vehicle_speed[i])

        #ACTUAL SPEED = (ENGINE RPM * PERIMETER OF TYRE)/(AXLE RATIO * GEAR RATIO)

		EXPT_SPEED.append(0.4*(engine_rpm[i] *60*3.14*2 *TYRE_SIZE*25.4*0.000001)/(Gear_Ratio*AXLE_RATIO))
		if(Vehicle_speed[i]<(EXPT_SPEED[i])):  # Checking whether vehicle speed is less than expected speed
			vehicleSpeedLess.append([Vehicle_speed[i], i])
			VehicleSpeedLess = pd.DataFrame(data=vehicleSpeedLess, columns=['Vehicle_speed','Index'])
		else:
			vehicleSpeedMore.append([Vehicle_speed[i], i])
			VehicleSpeedMore = pd.DataFrame(data=vehicleSpeedMore, columns=['Vehicle_speed','Index'])

	return Engine_loadLess, Engine_loadMore, Engine_rpmLess, Engine_rpmMore, VehicleSpeedLess, VehicleSpeedMore,EXPT_SPEED,load_threshold,rpm_threshold,counter_overload

def Coolant(CoolantTemperatureC,EngineLoad,TripTime):
	State0=[]
	State1=[]
	State2=[]
	State3=[]

	IndexTripTimeThreshold=0
	Safestate = 0
	LowestTemperatureC = 0.0
	NormalTemperatureC = 190.0 #Reference form internet safe state 190F to 220F
	HighestTemperatureC = 220.0

	CoolantTemperatureC_np=np.asarray(CoolantTemperatureC)
	CoolantTemperatureC_np=CoolantTemperatureC_np.astype(float)
	CoolantTemperatureF_np=(CoolantTemperatureC_np*(9/5))+32

	EngineLoad_np=np.asarray(EngineLoad)
	EngineLoad_np=EngineLoad_np.astype(float)

	TripTime_np=np.asarray(TripTime)
	TripTime_np=TripTime_np.astype(int)

	EngineLoadThreshold=0.50*max(EngineLoad_np)
	TripTimeThreshold = 0.50*max(TripTime_np)

	for i in CoolantTemperatureF_np.index:
		if CoolantTemperatureF_np[i] > NormalTemperatureC and CoolantTemperatureF_np[i] < HighestTemperatureC:
			if (TripTime_np[i] < TripTimeThreshold):
				IndexTripTimeThreshold=i
				if (EngineLoad_np[i] < EngineLoadThreshold):
					Safestate=Safestate+1
					State1.append([Safestate,i])
		elif CoolantTemperatureF_np[i] < NormalTemperatureC and CoolantTemperatureF_np[i] > LowestTemperatureC:
			Safestate=Safestate+1
			State2.append([Safestate,i])
		elif CoolantTemperatureF_np[i] > HighestTemperatureC:
			Safestate=Safestate-1
			State3.append([Safestate,i])
		State0.append(Safestate)


	SafeState1 = pd.DataFrame(data=State1, columns=['Safestate','Index'])
	SafeState2 = pd.DataFrame(data=State2, columns=['Safestate','Index'])
	SafeState3 = pd.DataFrame(data=State3, columns=['Safestate','Index'])

	return CoolantTemperatureF_np,HighestTemperatureC,NormalTemperatureC,LowestTemperatureC,SafeState1,SafeState2,SafeState3,State0,IndexTripTimeThreshold,EngineLoadThreshold
