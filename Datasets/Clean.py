import pandas as pd
import os

df_Pipeline = pd.read_csv("RequiredDataset.csv")
dfCSV=df_Pipeline['CSV']
dfVideos=df_Pipeline['Videos']

for i in dfCSV.index:
	os.remove(dfCSV[i])

for i in dfVideos.index:
	os.remove(dfVideos[i])
