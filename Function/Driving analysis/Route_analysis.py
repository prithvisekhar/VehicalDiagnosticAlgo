import pandas as pd
from Routine import avg_fuel
from TestOverspeed import over_speeding
from Test_cat_convertor import cat_convertor
data = pd.read_csv('Daily_data.csv')
df1 = data.to_dict()
print(df1)

A = data['Day'].tolist()
B = data['Average'].tolist()
C = data['efficiency_cat_con'].tolist()
D = data['No. of over_speeding_instances'].tolist()

df = pd.read_csv('data//14-Aug-2021-4.csv')

a = df['GPS Time'].iloc[1]
b = avg_fuel(df)
c = cat_convertor(df)
d = over_speeding(df)


def Append(w, x, y, z):
    A.append(w)
    B.append(x)
    C.append(y)
    D.append(z)
    add = {'Day': A, 'Average': B, 'efficiency_cat_con': C, 'No. of over_speeding_instances': D}
    return add


data1 = Append(a, b, c, d)
df1 = pd.DataFrame.from_dict(data1)
df1.to_csv('Daily_data.csv')
