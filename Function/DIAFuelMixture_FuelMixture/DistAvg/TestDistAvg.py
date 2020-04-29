import unittest
#import DistAvg
import DistAvg_2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class TestDistAvg(unittest.TestCase):
    def testDistAvg(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not(os.path.isdir("Result")):
                os.mkdir("Result")
            
            for i in df_File.index:
                df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                TempFile1 = df_File["Input_File_Name"][i].split('/')
                TempFile3 = TempFile1[-1].split('.')
                TempFile4 = str(TempFile3[0])
                path = os.path.join("Result/", TempFile4)
               # DistanceToZero = DistAvg.AverageDistance(df['Trip Distance(km)'].replace(to_replace="-", value="0"), df['Fuel Remaining (Calculated from vehicle profile)(%)'].replace(to_replace="-", value="0"), df['Kilometers Per Litre(Instant)(kpl)'].replace(to_replace="-", value="0"))
              
                #### Modification #######
                DistanceToZero_Modified = DistAvg_2.AverageDistance_modified(df['Fuel flow rate/minute(gal/min)'].replace(to_replace="-", value="0"), df['Fuel Remaining (Calculated from vehicle profile)(%)'].replace(to_replace="-", value="0"), df['Kilometers Per Litre(Instant)(kpl)'].replace(to_replace="-", value="0"),df['GPS Speed (Meters/second)'].replace(to_replace="_",value="0"))
                #### Modification #######

                DistanceToZero = (DistanceToZero_Modified['DistanceToZero']).to_numpy()
                Mileage_Mean = (DistanceToZero_Modified['Mileage']).to_numpy()
                Speed = (DistanceToZero_Modified['Speed']).to_numpy()
                x = np.linspace(1,np.size(Mileage_Mean),np.size(Mileage_Mean))
                                

                plt.figure(1,figsize=(30,20))
                plt.subplot(3,1,1)
                plt.plot(x,DistanceToZero,label='Distance to zero Prediction every minute',marker='o',linewidth=6.0)
                markerline, stemlines, baseline,=plt.stem(x,DistanceToZero,use_line_collection=True,linefmt='--')
                plt.setp(stemlines,color='r', linewidth=3.0)
                plt.setp(markerline,color='r', markersize=4.0)
                plt.ylabel('Distance in km', fontsize = 24)
               # plt.xlabel('Time (min)')
                plt.xticks(x,fontsize=24)
                plt.yticks(fontsize=24)
                plt.title("Distance to Zero Prediction every minute", fontsize = 26)

                plt.subplot(3,1,2)
                plt.plot(x,Speed,label='Speed (km/hr)',marker='o',linewidth=6.0)
                markerline, stemlines, baseline,=plt.stem(x,Speed,use_line_collection=True,linefmt='--')
                plt.setp(stemlines,color='r', linewidth=3.0)
                plt.setp(markerline,color='r', markersize=4.0)
                plt.ylabel('Speed in km/hr', fontsize = 24)
                plt.xlabel('Time (min)', fontsize = 26)
                plt.xticks(x,fontsize=24)
                plt.yticks(fontsize=24)


                plt.subplot(3,1,3)
                plt.plot(x,Mileage_Mean,label='Mileage (km/ltr)',marker='o',linewidth=6.0)
                markerline, stemlines, baseline,=plt.stem(x,Mileage_Mean,use_line_collection=True,linefmt='--')
                plt.setp(stemlines,color='r', linewidth=3.0)
                plt.setp(markerline,color='r', markersize=4.0)
                plt.ylabel('Mileage in km/ltr', fontsize = 24)
                plt.xlabel('Time (min)', fontsize = 26)
                plt.xticks(x,fontsize=24)
                plt.yticks(fontsize=24)

                plt.savefig(path+"f,Distance To Zero"+'.png')
                plt.close()

                #plt.figure(2)
                
                #plt.plot(DistanceToZero.loc[:, 'Index'], DistanceToZero.loc[:, 'DistanceToZero'], 'r.')
                #plt.title("Distance To Zero")
                #plt.savefig(path+"Distance To Zero"+'.png')
               #plt.savefig(path+'.png')
            #plt.savefig(path+"Distance To Zero"+'.png')        
        except AssertionError as e:
            f = open("ErrorMessage", "a")
            f.write(str(e)+" \n")

if __name__ == '__main__':
  #  pwd=''
   # for i,path in enumerate(os.getcwd().split('\\')):
    #    if(i<len(os.getcwd().split('\\'))):
     #       pwd = pwd+path+'/'
   # os.chdir(f'{pwd}')
    #os.chdir(r'C:\Users\Subodh\Desktop\Python\VehicalDiagnosticAlgo-master\VehicalDiagnosticAlgo-master\Function\DIAFuelMixture_FuelMixture\DistAvg')
    #print(pwd)
    unittest.main()
