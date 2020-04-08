import os
import pandas as pd

df_Pipeline = pd.read_csv("Running_Pipline.csv")

f = open("Coverage_Function.sh", "w")
flage=0
FilePaths=' '
for i in df_Pipeline.index:
	if os.path.exists(str(df_Pipeline["FileName"][i]) +"/.coverage"):
		FilePaths= FilePaths+str(df_Pipeline["FileName"][i]) +"/.coverage  "
		print('dsfdsfssfsf')
		flage=1
		
		
if flage==1:	
	f.write("coverage combine .coverage  "+FilePaths+ "\n")
	f.write("codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  \n")

f.close()
