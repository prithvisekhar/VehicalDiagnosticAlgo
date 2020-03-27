import pandas as pd


def SpeedVoilation(Speed, Latitude, Longitude, ThresholdSpeed):
    TempSpeedVoilation = []
    for i in Speed.index:
        if Speed[i] == '-':
            Speed[i] = 0
        if(float(Speed[i]) > ThresholdSpeed):
            TempSpeedVoilation.append([Latitude[i], Longitude[i], Speed[i], i])
    SpeedVoilation = pd.DataFrame(data=TempSpeedVoilation, columns=['Latitude', 'Longitude', 'Speed', 'Index'])
    return SpeedVoilation
