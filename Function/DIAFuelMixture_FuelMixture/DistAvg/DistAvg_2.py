
import pandas as pd
import numpy as np

def AverageDistance_modified(flowrate, Fuel, Kmpl,Speed):
    TotalCapacity = 35 #ltrs
    ExpectedDistance=[]
    temp=[]
    for i in Fuel.index:
        flowrate.iloc[i] = float(flowrate.iloc[i])

    for i in Fuel.index:
        Fuel.iloc[i] = float(Fuel.iloc[i])

    counter=0
    deltaT = 60
    a=[]
    for i in range(0,flowrate.size,deltaT):
        flow=(flowrate.loc[i:i+deltaT-1]) * (3.78541)  #gallons/min to ltrs/min
        # 3.78541 is a factor to convert gallons per minute to  ltrs/min
        # "flow" contains deltaT samples of fuel flow rate ("flowrate")

        flow_rate_mean = (flowrate.loc[i:i+deltaT-1]).mean() * (3.78541)
        # "flow_rate_mean" is the average fuel flow rate of deltaT samples of flowrate "flow"

        fuel_remaining=(Fuel.loc[i:i+deltaT-1])*TotalCapacity/100 #ltrs     #Fuel Dataset is present in percentage
        # "fuel_remaining" is the remaining fuel capacity of all deltaT sample instants in litres. (here size of fuel_remaining is deltaT)

        speed = (Speed.loc[i:i+deltaT-1])    #m/s
        # "speed" variable contains GPS speed in m/s of all deltaT sample instants (here size of fuel_remaining is deltaT)

        flow[flow<=0] = flow_rate_mean/2
        ### If flow rate at an instant is equal to zero then make that value equal to the first quartile value (mean/2)
        ### first quartile is selected so that all those (zero) values become closer to 0 then to mean

        time_remaining = fuel_remaining.divide(flow,fill_value = flow_rate_mean) #minutes
        #                          remaining_fuel(ltrs)
        # time_till_zero_fuel =  -----------------------
        #                          flow_rate(ltrs/min)

        
        fuel_remaining[fuel_remaining<=0] =((Fuel.loc[i:i+deltaT-1]).mean()*TotalCapacity/100 )/2
        ### If fuel remaining at an instant is equal to zero then make that value equal to the first quartile value (mean/2)
        ### so that all those values become closer to 0 than to mean
        ### Now the fuel_remaining will be used to calculate Mileage_Mean

        Speed_Mean = (Speed.loc[i:i+deltaT-1]).mean() * 3.6  #km/hr

        ### ExpectedDistance is the distance to zero which is calculated as
        ### ExpectedDistance = (Speed (m/s)/1000) * (time_remaining (min)*60    ----> in kms

        ### Mileage = ExpectedDistance (of every sample in deltaT)/Remaining_fuel(for every corresponding sample in deltaT)
        ### Mileage_Mean is the average of Mileage calculated calculated for deltaT samples taken together

        Mileage_Mean = ((speed * time_remaining * 60/1000).divide(fuel_remaining)).mean()    #km/ltr

        ExpectedDistance.append([((speed * time_remaining * 60).mean())/1000,Speed_Mean,Mileage_Mean])    #kms
        temp.append([((speed * time_remaining * 60).mean())/1000,flow_rate_mean,Speed_Mean])
        counter = counter+1
        
    DistanceToZero = pd.DataFrame(data=ExpectedDistance, columns=['DistanceToZero', 'Speed', 'Mileage'])
    tempo=pd.DataFrame(data=temp, columns=['DistanceToZero','flow rate','Average_Speed(km/hr)'])
    
    return DistanceToZero
