from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

df_Pipeline = pd.read_csv("RequiredDataset.csv")
dfCSV=df_Pipeline['CSV']
dfVideos=df_Pipeline['Videos']


gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()

for file1 in file_list:
	if file1['title']=='OBD Datasets':
		OBDID=file1['id']

file_listOBD = drive.ListFile({'q': "'"+str(OBDID)+"' in parents and trashed=false"}).GetList()

for file1 in file_listOBD:
	if file1['title']=='CSV':
		CSVID=file1['id']
	elif file1['title']=='Videos':
		VideosID=file1['id']

file_listCSV = drive.ListFile({'q': "'"+str(CSVID)+"' in parents and trashed=false"}).GetList()
file_listVideos = drive.ListFile({'q': "'"+str(VideosID)+"' in parents and trashed=false"}).GetList()
CSV=[]
Videos=[]
CSV.append('CSV')
Videos.append('Videos')
for file1 in file_listCSV:
	CSV.append(file1['title'])
	for i in dfCSV.index:
		if dfCSV[i]==file1['title']:
			test_downloaded = drive.CreateFile({'id': file1['id']})
			test_downloaded.GetContentFile(file1['title'])
		
		
for file1 in file_listVideos:
	Videos.append(file1['title'])
	for i in dfVideos.index:
		if dfVideos[i]==file1['title']:
			test_downloaded = drive.CreateFile({'id': file1['id']})
			test_downloaded.GetContentFile(file1['title'])
		

	
	
CSVMax=max(len(CSV),len(Videos))

f = open("DataSetFiles.csv", "w")
for i in range(0,CSVMax):
	if i<len(CSV):
		f.write(CSV[i])
	if i<len(Videos):
		f.write(','+Videos[i]+'\n')
f.close()


	

