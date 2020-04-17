import pandas as pd


def O2_Sensor(O2_value):
    O2_value = O2_value.replace(to_replace='-', value=0)
    df1 = pd.DataFrame(data=O2_value)
    mean_value = df1.mean()
    if ((mean_value > 0.315).any() & (mean_value < 0.585).any()):
        condition = 0
    elif ((mean_value > 0.225).any() & (mean_value < 0.675).any()):
        condition = 1
    else:
        condition = 2
    return mean_value, condition
