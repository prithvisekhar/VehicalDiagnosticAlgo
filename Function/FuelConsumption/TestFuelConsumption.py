import pandas as pd
import matplotlib.pyplot as plt
from FuelConsumption import fuel_monitoring

df = pd.read_csv('D://G Drive backup//LTTS Internship//Reimplementing_codes//'
                 'Datasets//Dataset-5.csv')

Engine_load = df['Engine Load(%)']
# Fuel_mass = ((770 * 3.78541) / 360) * df['Fuel flow rate/hour(gal/hr)']
Fuel_mass = (770 / 360) * df['Fuel flow rate/hour(l/hr)']
Vehicle_speed = df['GPS Speed (Meters/second)'] * (18/5)
# Km_per_liter = df['Kilometers Per Litre(Long Term Average)(kpl)']
Km_per_liter = df['Trip average KPL(kpl)']

y = fuel_monitoring(Engine_load, Fuel_mass, Vehicle_speed, Km_per_liter)
