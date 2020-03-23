import pandas as pd
from importlib.machinery import SourceFileLoader

DIAEngineAnalysis = SourceFileLoader("LoadAnalysis", "../Function/DIAEngineAnalysis_Coolant/DIAEngineAnalysis.py").load_module()
DIAFuelMixture = SourceFileLoader("FuelMixture", "../Function/DIAFuelMixture_FuelMixture/DIAFuelMixture.py").load_module()
DIASpeedVoilation = SourceFileLoader("SpeedVoilation", "../Function/DIASpeedVoilation_SpeedVoilation/DIASpeedVoilation.py").load_module()

df = pd.read_csv("../Datasets/Dataset-1.csv")

EngineLoadLess, EngineLoadMore, EngineRPMLess, EngineRPMMore, VehicleSpeedLess, VehicleSpeedMore, ExpectedSpeed,LoadThreshold,RPMThreshold,CounterOverload = DIAEngineAnalysis.LoadAnalysis(df["Engine Load(%)"], df["Engine RPM(rpm)"],df['Speed (GPS)(km/h)'],df['Trip Time(Since journey start)(s)'])

CoolantTemperatureF_np,HighestTemperatureC,NormalTemperatureC,LowestTemperatureC,SafeState1,SafeState2,SafeState3,State0,IndexTripTimeThreshold,EngineLoadThreshold \
 =DIAEngineAnalysis.Coolant(df['Engine Coolant Temperature(°C)'].replace(to_replace="-", value="0"),df['Engine Load(%)'].replace(to_replace="-", value="0"),df['Trip Time(Since journey start)(s)'].replace(to_replace="-", value="0"))

Lean, Rich, Nrml =DIAFuelMixture.FuelMixture(df['O2 Volts Bank 1 sensor 2(V)'])

SpeedViolate=DIASpeedVoilation.SpeedVoilation(df["Speed (GPS)(km/h)"],df[' Latitude'],df[' Longitude'],20)


