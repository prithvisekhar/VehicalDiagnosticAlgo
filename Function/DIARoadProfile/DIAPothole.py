import pandas as pd
import numpy as np
import peakutils


def mean_rolling(List_name):
    chunks = [List_name[i:i + 2] for i in range(0, len(List_name), 2)]
    d = []
    for i in chunks:
        s = 0
        for j in i:
            s += j / 2
        d.append(s)
    return d


def PotholeDetection(time, acc_y, lat, long):
    Lat_Long = []
    x = time  # np.array(data['Trip Time(Since journey start)(s)'])
    y = acc_y  # np.array(data['Acceleration Sensor(Y axis)(g)'])
    indexes = peakutils.indexes(-y, thres=0.9, min_dist=10)

    for i in indexes:
        Lat_Long.append([lat[i], long[i], i])
    PotholeDetection = pd.DataFrame(data=Lat_Long, columns=['Latitude', 'Longitude', 'Index'])
    return PotholeDetection
