import pandas as pd
from FuelConsumption import fuel_monitoring

df = pd.read_csv('02-Jan-2020.csv', header=0, skiprows=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

Engine_load = df['Engine Load(%)']
Fuel_mass = ((770 * 3.78541) / 360) * df['Fuel flow rate/hour(gal/hr)']
# Fuel_mass = (770 / 360) * df['Fuel flow rate/hour(l/hr)']
# Fuel_mass = ((770 * 3.78541 * 60) / 360) * df['Fuel flow rate/minute(gal/min)']
# Vehicle_speed = df['GPS Speed (Meters/second)'] * (18/5)
Vehicle_speed = df['Speed (OBD)(km/h)']
# Km_per_liter = df['Kilometers Per Litre(Long Term Average)(kpl)']
Km_per_liter = df['Trip average KPL(kpl)']

y = fuel_monitoring(Engine_load, Fuel_mass, Vehicle_speed, Km_per_liter)
