import pandas as pd
#from shapely.geometry import Point
#import geopandas as gpd
#import plotly.graph_objects as go
#import plotly.express as px

def traffic(SPEED,latitude,longitude):
    #SPEED_ARR = np.array(SPEED)
    #GPS_ARR = np.array(GPS)
    A = len(SPEED)
    for i in range(0, A):
        #t2=SPEED_ARR.replace(to_replace='-',value=0)
        #SPEED_ARR[SPEED_ARR = '-' ] = 0
        if SPEED[i]== '-' :
            SPEED[i] = '0'
        SPEED[i] = float(SPEED[i])
        LOW_CONGESTION_COUNT = 0
        MODERATE_CONGESTION_COUNT = 0
        HIGH_CONGESTION_COUNT = 0
    LOW_CONGESTION_LOC = []
    MODERATE_CONGESTION_LOC = []
    HIGH_CONGESTION_LOC = []

    for i in range(0, A):
        if SPEED[i] < 10.00:
            HIGH_CONGESTION_COUNT += 1
            HIGH_CONGESTION_LOC.append([latitude[i], longitude[i], SPEED[i], i])
            HighCongestion = pd.DataFrame(data=HIGH_CONGESTION_LOC, columns=['Latitude', 'Longitude','Speed','Index'])
        elif SPEED[i] > 10.00 and SPEED[i] < 20.00:
            MODERATE_CONGESTION_COUNT += 1
            MODERATE_CONGESTION_LOC.append([latitude[i], longitude[i], SPEED[i], i])
            ModerateCongestion = pd.DataFrame(data=MODERATE_CONGESTION_LOC, columns=['Latitude', 'Longitude','Speed','Index'])
        elif SPEED[i] > 20.00:
            LOW_CONGESTION_COUNT += 1
            LOW_CONGESTION_LOC.append([latitude[i], longitude[i], SPEED[i], i])
            LowCongestion = pd.DataFrame(data=LOW_CONGESTION_LOC, columns=['Latitude', 'Longitude','Speed','Index'])
    print("No. Of High Congestion Areas:%.2f"%HIGH_CONGESTION_COUNT)
    print("No. Of Moderate Congestion Areas:%.2f"%MODERATE_CONGESTION_COUNT)
    print("No. Of Low Congestion Areas:%.2f"%LOW_CONGESTION_COUNT)
    print()
    return HighCongestion, ModerateCongestion, LowCongestion 
