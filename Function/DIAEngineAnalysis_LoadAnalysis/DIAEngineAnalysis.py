"""Function checks the load on the engine and returns it as overloaded or not."""

import numpy as np
import pandas as pd
def LoadAnalysis(EngineLoad,EngineRPM,VehicleSpeed, TripTime):
	GearRatio = 1.5
	AxleRatio = 4
	TyreSize = 12
	ExpectedSpeed = []
	MaxLoad = 0
	MaxRPM = 0
	TempEngineLoadLess = []
	TempEngineLoadMore = []
	TempEngineRPMLess = []
	TempEngineRPMMore = []
	TempVehicleSpeedLess = []
	TempVehicleSpeedMore = []

	CounterOverload = []
	TempCounterOverload=0

	for i in EngineLoad.index:
		if EngineLoad[i] == '-' :
			EngineLoad[i] = '0';
		if EngineRPM[i] == '-' :
			EngineRPM[i] = '0';
		EngineLoad[i] = float(EngineLoad[i])
		EngineRPM[i] = float(EngineRPM[i])

		if MaxLoad < EngineLoad[i]:
			MaxLoad = EngineLoad[i]

		if MaxRPM < EngineRPM[i]:
			MaxRPM = EngineRPM[i]

	LoadThreshold = 0.5 * MaxLoad
	RPMThreshold = 0.5 * MaxRPM

	for i in EngineRPM.index:
		if VehicleSpeed[i] == '-' :
			VehicleSpeed[i]= '0';
		if TripTime[i] == '-' :
			TripTime[i] = '0';

		if(EngineLoad[i]<LoadThreshold):  # Checking whether vehicle speed is less than expected speed
			TempEngineLoadLess.append([EngineLoad[i], i])
		else:
			TempEngineLoadMore.append([EngineLoad[i], i])

		if(EngineRPM[i]<RPMThreshold):  # Checking whether vehicle speed is less than expected speed
			TempEngineRPMLess.append([EngineRPM[i], i])
		else:
			TempEngineRPMMore.append([EngineRPM[i], i])

		if EngineLoad[i] > LoadThreshold and  EngineRPM[i] > RPMThreshold:
			TempCounterOverload = TempCounterOverload + 1 # Checking whether engine load and engine rpm are less than threshold
		CounterOverload.append(TempCounterOverload)

		VehicleSpeed[i] = float(VehicleSpeed[i])

        #ACTUAL SPEED = (ENGINE RPM * PERIMETER OF TYRE)/(AXLE RATIO * GEAR RATIO)
		ExpectedSpeed.append(0.4*(EngineRPM[i] *60*3.14*2 *TyreSize*25.4*0.000001)/(GearRatio*AxleRatio))

		if(VehicleSpeed[i]<(ExpectedSpeed[i])):  # Checking whether vehicle speed is less than expected speed
			TempVehicleSpeedLess.append([VehicleSpeed[i], i])
		else:
			TempVehicleSpeedMore.append([VehicleSpeed[i], i])

	EngineLoadLess = pd.DataFrame(data=TempEngineLoadLess, columns=['EngineLoad','Index'])
	EngineLoadMore = pd.DataFrame(data=TempEngineLoadMore, columns=['EngineLoad','Index'])
	EngineRPMLess = pd.DataFrame(data=TempEngineRPMLess, columns=['EngineRPM','Index'])
	EngineRPMMore = pd.DataFrame(data=TempEngineRPMMore, columns=['EngineRPM','Index'])
	VehicleSpeedLess = pd.DataFrame(data=TempVehicleSpeedLess, columns=['VehicleSpeed','Index'])
	VehicleSpeedMore = pd.DataFrame(data=TempVehicleSpeedMore, columns=['VehicleSpeed','Index'])

	return EngineLoadLess, EngineLoadMore, EngineRPMLess, EngineRPMMore, VehicleSpeedLess, VehicleSpeedMore,ExpectedSpeed,LoadThreshold,RPMThreshold,CounterOverload

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
