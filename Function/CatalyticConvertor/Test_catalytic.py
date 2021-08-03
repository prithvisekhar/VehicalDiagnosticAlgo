import pandas as pd
from catalytic_performace import check_performance

df = pd.read_csv('02-Jan-2020.csv', header=0, skiprows=[1, 2, 3])

O1 = df['O2 Volts Bank 1 sensor 1(V)']
O2 = df['O2 Volts Bank 1 sensor 2(V)']
Trip_time = df['Trip time(whilst moving)(s)']
speed = df['GPS Speed (Meters/second)']

Upstream = O1
downstream = O2
Time = Trip_time
Speed = speed

y = check_performance(Upstream, downstream, Time, Speed)
