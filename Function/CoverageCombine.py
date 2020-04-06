import os
import pandas as pd

df_Pipeline = pd.read_csv("Running_Pipline.csv")

f = open("Coverage_Function.sh", "w")

FilePaths=' '
for i in df_Pipeline.index:
	FilePaths= FilePaths+str(df_Pipeline["FileName"][i]) +"/.coverage  "
		
	
f.write("coverage combine  "+FilePaths+ "\n")
print("coverage combine  "+FilePaths+ "\n")
f.write("codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  \n")

f.close()
