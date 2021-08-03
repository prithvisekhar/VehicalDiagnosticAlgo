import pandas as pd
df = pd.read_csv('01-Aug-21.csv')

data = pd.DataFrame()
data['Time'] = df['Trip Time(Since journey start)(s)']
data['Engine RPM'] = df['Engine RPM(rpm)']
data['Speed'] = df['Speed (OBD)(km/h)']
data['Power(W)'] = df['Engine kW (At the wheels)(kW)']
data['Torque'] = df['Torque(Nm)']

data = data.replace('-', 0)
data_2 = data[(data[['Power(W)', 'Torque']] != 0).all(axis=1)]

data_2['Power(W)'] = data_2['Power(W)'].astype(float)
data_2['Torque'] = data_2['Torque'].astype(float)
data_2['Power/Torque'] = (data_2['Power(W)'] * 1000) / data_2['Torque']
data_2['Omega'] = (2 * (22/7) * data_2['Engine RPM']) / 60
data_2['Speed_ratio'] = data_2['Power/Torque'] / data_2['Omega']
Speed_ratio = data_2['Speed_ratio']

data_2 = data_2[data_2['Speed_ratio'] >= 1.2]
data_2 = data_2[data_2['Speed'] > 10]
print(data_2.shape)
print(data_2.head())

count = []
for i in range(data_2.shape[0]):
    count.append(data_2['Time'].iloc[i])

print(count)
Sum = 0
for i in range(len(count)-1):
    if (count[i+1] - count[i]) == 1:
        i += 4
        Sum += 1
    else:
        i += 1
        Sum += 0

print("Over_speeding occurs : ", Sum, "times")
