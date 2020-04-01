import os


f = open("Coverage_Function.sh", "w")

FileNames=[name for name in os.listdir(".") if os.path.isdir(name)]
FilePaths=' '
for x in FileNames:
	if os.path.isfile(x+"/.coverage"):
		FilePaths= FilePaths+ x +"/.coverage  "
		

if len(FileNames)>1:
	f.write("coverage combine "+FilePaths+ "\n")
	#print("coverage combine "+FilePaths+ "\n")
else:
	f.write("cp  "+FilePaths+ " .coverage \n")
	
f.write("codeclimate-test-reporter  --token $CC_TEST_REPORTER_ID --file ./.coverage  \n")
f.close()
