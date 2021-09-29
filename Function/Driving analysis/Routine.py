import pandas as pd
import numpy as np

def avg_fuel(df):
    R = pd.DataFrame()
    R['KPL'] = df['Trip average KPL(kpl)']
    R['KPL'] = R['KPL'].replace('-', 0)
    R['KPL'] = R['KPL'].astype(float)
    R = R[R['KPL'] > 0]
    avg_KPL = np.mean(R['KPL'])
    return round(avg_KPL, 3)


def cat_conv(df):
    R = pd.DataFrame()
    R['O2_down'] = df['O2 Volts Bank 1 sensor 2(V)']
    efficiency = np.mean(R['KPL'])
    return efficiency
