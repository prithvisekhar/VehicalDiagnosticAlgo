
import os

df_Pipeline = pd.read_csv("Running_Pipline.csv")

f = open("Coverage_Function.sh", "w")

FilePaths=' '
for x in df_Pipeline.index:
	FilePaths= FilePaths+str(df_Pipeline["FileName"][i]) +"/.coverage  "
		
	
f.write("coverage combine .coverage "+FilePaths+ "\n")
print("coverage combine .coverage "+FilePaths+ "\n")
f.write("codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  \n")

f.close()
