#!/usr/bin/env python
# coding: utf-8

# In[57]:


from __future__ import division
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import peakutils 
#import scipy

def Pothole(Accelerometer_values):
    Cutoff_freq = 0.2  
    bandwidth = 0.16  
    N = int(np.ceil((4 / bandwidth)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)
 
    #Compute a low-pass filter.
    h = np.sinc(2 * Cutoff_freq * (n - (N - 1) / 2))
    w = np.blackman(N)
    h = h * w
    h = h / np.sum(h)
 
    #Create a high-pass filter from the low-pass filter through spectral inversion.
    h = -h
    h[(N - 1) // 2] += 1
    signal = np.convolve(Accelerometer_values, h,'same')
    np.set_printoptions(suppress=False)
    signal1=signal.astype(float) #amplifying the output by 10 times for further computation
    
    values = np.array(signal1)
    confirmed_potholes = values[values<-0.19]
    indexvalues_confirmed = np.nonzero(signal1 <-0.19)
    rest = np.array(signal1[signal1>-0.2])
    possible_potholes = rest[rest<-0.1]
    index_acc =  np.nonzero(signal1)
    return confirmed_potholes,possible_potholes,indexvalues_confirmed,signal1, index_acc

