import pandas as pd
import os

df_Pipeline = pd.read_csv("Running_Pipline.csv")

for j in df_Pipeline.index:
	
	t=df_Pipeline["File"][j].split('.')
	File_Name=str(t[0])
	Function_Name=str(df_Pipeline["Function"][j])
	Test_Case_File=str(df_Pipeline["Test_File"][j])
	if df_Pipeline['Type'][j]=='UT':
		f = open("Test_"+Function_Name+"_"+File_Name+".py", "w")
		f.write("import unittest\n")
		f.write("import "+File_Name+"\n")
		f.write("f = open(\"Difference_Report_"+File_Name+"\", \"a\")\n")
		f.write("class Test"+File_Name+"(unittest.TestCase):\n")
		f.write("\tdef test"+Function_Name+"(self):\n")
		df = pd.read_excel(Test_Case_File)
		for i in df.index:
			f.write("\t\ttry:\n")
			f.write("\t\t\tself.assertEqual("+File_Name+"."+Function_Name+"("+str(df["Input"][i])+"),"+str(df["Output"][i])+")\n")
			f.write("\t\texcept AssertionError as e:\n")
			f.write("\t\t\tf.write(\"TestCase_no_"+str(i)+":\\n\\t\"+str(e)+\" \\n\")\n")
		f.write("if __name__ == '__main__':\n")
		f.write("\tunittest.main()")
		f.close()
		os.system("mkdir "+File_Name+"_"+Function_Name)
		os.system("cp "+Test_Case_File+"  "+File_Name+"_"+Function_Name)
		os.system("mv "+"Test_"+Function_Name+"_"+File_Name+".py"+"  "+File_Name+"_"+Function_Name)
		os.system("cp "+str(df_Pipeline["File"][j])+"  "+File_Name+"_"+Function_Name)
	else:
		os.system("mkdir "+File_Name+"_"+Function_Name)
		os.system("cp "+Test_Case_File+"  "+File_Name+"_"+Function_Name)
		os.system("mv "+str(df_Pipeline["Testpy_File"][j])+"  "+File_Name+"_"+Function_Name)
		print("mv "+str(df_Pipeline["Testpy_File"][j])+"  "+File_Name+"_"+Function_Name)
		os.system("cp "+str(df_Pipeline["File"][j])+"  "+File_Name+"_"+Function_Name)

	
	
