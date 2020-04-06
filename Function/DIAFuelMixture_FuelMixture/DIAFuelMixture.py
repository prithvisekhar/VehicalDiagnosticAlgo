import pandas as pd


def Fuel_Mixture(O2_Volts):
    TempLean = []
    TempRich = []
    TempNrml = []

    for i in O2_Volts.index:
        O2_Volts[i] = float(O2_Volts[i])
        if O2_Volts[i] <= 0.1:
            TempLean.append([O2_Volts[i], i])
        elif O2_Volts[i] >= 0.9:
            TempRich.append([O2_Volts[i], i])
        else:
            TempNrml.append([O2_Volts[i], i])
    Lean = pd.DataFrame(data=TempLean, columns=['O2_Volts', 'Index'])
    Rich = pd.DataFrame(data=TempRich, columns=['O2_Volts', 'Index'])
    Nrml = pd.DataFrame(data=TempNrml, columns=['O2_Volts', 'Index'])
    return Lean, Rich, Nrml


def AverageDistance(Distance, Fuel, Kmpl):
    ExpectedDistance = []
    TotalDistance = Distance.iloc[-1]
    TotalDistance = float(TotalDistance)
    print("The total Distance covered:", TotalDistance)
    for i in Fuel.index:
        Fuel.iloc[i] = float(Fuel.iloc[i])
    RemainingFuel = Fuel.iloc[-1]
    UsedFuel = Fuel.iloc[-1] - Fuel.iloc[1]
    print ("UsedFuel:", UsedFuel)
    Mileage = TotalDistance/UsedFuel
    TimeIndex = 28 #int(input('Enter the Time : '))
    for i in Distance.index:
        ExpectedDistance.append([Fuel[i] * Mileage, i])
    if TimeIndex < Kmpl.index[-1]:
        TempExpectedDistance = Fuel[TimeIndex]*Mileage
    else:
        TempExpectedDistance = RemainingFuel*Mileage
    print('Expected Distance', TempExpectedDistance)
    DistanceToZero = pd.DataFrame(data=ExpectedDistance, columns=['DistanceToZero', 'Index'])
    return DistanceToZero