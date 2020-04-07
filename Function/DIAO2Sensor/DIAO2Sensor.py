import pandas as pd


def O2_Sensor(O2_value):
    O2_value = O2_value.replace(to_replace='-', value=0)
    df1 = pd.DataFrame(data=O2_value)
    mean_value = df1.mean()
    return mean_value
    if ((mean_value > 0.315).any() & (mean_value < 0.585).any()):
        print("Good Condition")
    elif ((mean_value > 0.225).any() & (mean_value < 0.675).any()):
        print("O2 Sensor Warning")
    else:
        print("Bad Condition")
