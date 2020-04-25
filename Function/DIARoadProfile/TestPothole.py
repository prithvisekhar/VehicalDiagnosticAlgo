#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import DIAPothole
import unittest


class Test_Pothole(unittest.TestCase):
    def testPothole(self):
        try:
            df_File = pd.read_csv("List_of_Data_Set.csv")
            if not (os.path.isdir("Result1")):
                os.mkdir("Result1")
            #if not (os.path.isdir("Result2")):
                #os.mkdir("Result2")
            for i in df_File.index:
                df = pd.read_csv(str(df_File["Input_File_Name"][i]))
                TempFile1 = df_File["Input_File_Name"][i].split('/')
                TempFile3 = TempFile1[-1].split('.')
                TempFile4 = str(TempFile3[0])
                path = os.path.join("Result1/", TempFile4)
                #path1 = os.path.join("Result2/", TempFile4)
                time = df['Trip Time(Since journey start)(s)']
                Accx = df['Acceleration Sensor(X axis)(g)'] 
                Accy = df['Acceleration Sensor(Y axis)(g)']
                Accz = df['Acceleration Sensor(Z axis)(g)']
                Speed = df['Speed (OBD)(km/h)']
                RPM = df['Engine RPM(rpm)']
                Acc_pedal = df['Accelerator PedalPosition E(%)']
                time_np=np.array(time)
                confirmed_potholes,possible_potholes,indexvalues_confirmed,Acc_signal,Acc_index=DIAPothole.Pothole(Accx)
                confirmed = np.array(indexvalues_confirmed)
                idx=  np.nonzero(confirmed)
                plt.figure(1)
                plt.plot(time_np,Acc_signal,label='Vertical Acceleration')
                plt.plot(time_np[idx[0][0]+confirmed[0]],confirmed_potholes,'r.',markersize=10,label='Detected Potholes')
                #plt.plot(np.repeat(-0.1,len(d)),label='-0.1')
                #plt.plot(np.repeat(-0.2,len(d)),label='-0.2')

                plt.axhline(y=-0.1, color='m', linestyle='-',label='-0.1 Possibility Threshold of Pothole ')
                plt.axhline(y=-0.2, color='y', linestyle='-',label='-0.2 Confirmation Threshold of Pothole ')
                plt.title("Pothole Detection with Filtered Acceleration Data.")
                plt.ylabel('Acceleration After High Pass Filter')
                plt.xlabel('Time in Seconds')
                plt.legend(loc='upper right')
                plt.savefig(path+'.png')
                #figure(2)
                #plt.plot(time,Speed, label='Speed')
                #plt.plot(time,Acc_pedal, label='Accelerator pedal position')
                #plt.plot(time,RPM, label='RPM')
                #plt.ylabel('Parameters')
                #plt.xlabel('Time in Seconds')
                #plt.legend(loc='upper right')

                
                #plt.savefig(path1+'.png')
                
                
                
                print(confirmed_potholes)
                print(indexvalues_confirmed[0])
                plt.close()
                
        except AssertionError as e:
            f = open("Error_Pothole", "a")
            f.write("TestCase_no_0:\n\t" + str(e) + " \n")

if __name__ == '__main__':
    unittest.main()
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




