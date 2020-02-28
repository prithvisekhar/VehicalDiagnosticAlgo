!pip install shapely
!pip install geopandas
!pip install osmapi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px

def traffic(SPEED,latitude longitude):
  SPEED_ARR = np.array(SPEED)
  #GPS_ARR = np.array(GPS)
  A = len(SPEED)
  for i in range(0, A):
      SPEED_ARR[i] = float(SPEED_ARR[i])
  LOW_CONGESTION_COUNT = 0
  MODERATE_CONGESTION_COUNT = 0
  HIGH_CONGESTION_COUNT = 0

  LOW_CONGESTION_LOC = []
  MODERATE_CONGESTION_LOC = []
  HIGH_CONGESTION_LOC = []

  for i in range(0, A):
      if SPEED_ARR[i] < 10.00:
          HIGH_CONGESTION_COUNT += 1
          HIGH_CONGESTION_LOC.append(latitude[i], longitude[i])
		  HighCongestion = pd.DataFrame(data=HIGH_CONGESTION_LOC, columns=['Latitude', 'Longitude')
      elif SPEED_ARR[i] > 10.00 and SPEED_ARR[i] < 20.00:
          MODERATE_CONGESTION_COUNT += 1
          MODERATE_CONGESTION_LOC.append(latitude[i], longitude[i])
		  ModerateCongestion = pd.DataFrame(data=MODERATE_CONGESTION_COUNT, columns=['Latitude', 'Longitude')
      elif SPEED_ARR[i] > 20.00:
          LOW_CONGESTION_COUNT += 1
          LOW_CONGESTION_LOC.append(latitude[i], longitude[i])
		  LowCongestion = pd.DataFrame(data=LOW_CONGESTION_COUNT, columns=['Latitude', 'Longitude')


  print("No. Of High Congestion Areas:%.2f"%HIGH_CONGESTION_COUNT)
  print("No. Of Moderate Congestion Areas:%.2f"%MODERATE_CONGESTION_COUNT)
  print("No. Of Low Congestion Areas:%.2f"%LOW_CONGESTION_COUNT)
  print()
	return HighCongestion, ModerateCongestion, LowCongestion 