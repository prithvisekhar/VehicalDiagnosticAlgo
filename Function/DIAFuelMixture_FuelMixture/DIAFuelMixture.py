import pandas as pd


def FuelMixture(O2_Volts):
    TempLean = []
    TempRich = []
    TempNrml = []

    for i in O2_Volts.index:
        if O2_Volts[i] == '-':
            O2_Volts[i] = '0'
        O2_Volts[i] = float(O2_Volts[i])
        O2_Volts[i] = float(O2_Volts[i])
        if O2_Volts[i] >= 0.0 and O2_Volts[i] <= 0.1:
            TempLean.append([O2_Volts[i], i])
        elif O2_Volts[i] >= 0.9 and O2_Volts[i] <= 1.0:
            TempRich.append([O2_Volts[i], i])
        else:
            TempNrml.append([O2_Volts[i], i])
    Lean = pd.DataFrame(data=TempLean,columns = ['O2_Volts', 'Index'])
    Rich = pd.DataFrame(data=TempRich,columns = ['O2_Volts', 'Index'])
    Nrml = pd.DataFrame(data=TempNrml,columns = ['O2_Volts', 'Index'])
    return Lean, Rich, Nrml
