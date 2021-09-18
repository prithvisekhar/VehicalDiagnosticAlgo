import pandas as pd
import numpy as np
import gmplot
from Turning import check_turn, quality_turn

data = pd.read_csv('data//14-Aug-2021-4.csv')
# print(data[' Bearing'])
df = pd.DataFrame()
df['time'] = data['Trip Time(Since journey start)(s)']
df['Latitude'] = data[' Latitude']
df['Longitude'] = data[' Longitude']
df['Compass angle'] = data[' Bearing'].astype('float')
df['Speed'] = data['Speed (OBD)(km/h)'].astype('float')

df['Compass angle'] = df['Compass angle'].replace(0, np.nan)
df['Compass angle'] = df['Compass angle'].replace(method='ffill')
df = df.dropna(axis=0)
df.set_index('time', inplace=True)

Speed = df['Speed']
Angle = df['Compass angle']


spot1 = []
spot2 = []
i = 0
while i < (df.shape[0] - 10):
    if abs(Angle.iloc[i] - Angle.iloc[i + 9]) >= 60:
        spot1.append(i)
        spot2.append(i + 9)
        # ans.append(check_turn(i, i + 10))
        i = i + 10
    else:
        i += 1

print(spot1)
print(spot2)
# print(ans)

Latitude = []
Longitude = []
for i in range(len(spot1)):
    T = check_turn(Angle, spot1[i], spot2[i])
    print(T)
    y = quality_turn(Speed, spot1[i], spot2[i])
    if y >= 60:
        print('Good Turn, score is', y, '%')
    else:
        print('Bad Turn, score is', y, '%')
        for j in range(spot2[i] - spot1[i]):
            Latitude.append(df['Latitude'].iloc[spot1[i] + j])
            Longitude.append(df['Longitude'].iloc[spot1[i] + j])


def PlotMap(Lati, Longi):
    plot = gmplot.GoogleMapPlotter(df['Latitude'].iloc[1], df['Longitude'].iloc[1], 17)
    plot.scatter(Lati, Longi, 'red', size=2, marker=False)
    plot.draw("Bad_turns_1.html")


PlotMap(Latitude, Longitude)
