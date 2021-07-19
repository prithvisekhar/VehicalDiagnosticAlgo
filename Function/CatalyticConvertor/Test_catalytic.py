import pandas as pd
import matplotlib.pyplot as plt
from catalytic_performace import check_performance
df = pd.read_csv('D://G Drive backup//LTTS Internship//Reimplementing_codes//'
                 'Datasets//Dataset-2.csv')
O1 = df['O2 Volts Bank 1 sensor 1(V)']
O2 = df['O2 Volts Bank 1 sensor 2(V)']
Trip_time = df['Trip time(whilst moving)(s)']
speed = df['GPS Speed (Meters/second)']
"""data = pd.DataFrame()
data['Upstream O2'] = O1[3:]
data['downstream O2'] = O2
data['time'] = Trip_time[3:]
data['speed'] = speed """

Upstream = O1
downstream = O2
Time = Trip_time
Speed = speed

y = check_performance(Upstream, downstream, Time, Speed)
