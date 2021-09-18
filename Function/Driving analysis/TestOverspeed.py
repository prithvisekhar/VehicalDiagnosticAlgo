import pandas as pd
data1 = pd.read_csv('data//14-Aug-2021-4.csv')


def over_speeding(data):
    df = pd.DataFrame()
    df['Time'] = data['Trip Time(Since journey start)(s)']
    df['Engine RPM'] = data['Engine RPM(rpm)']
    df['Speed'] = data['Speed (OBD)(km/h)']
    df['Power(W)'] = data['Engine kW (At the wheels)(kW)']
    df['Torque'] = data['Torque(Nm)']
    df = df.replace('-', 0)
    df = df[(df[['Power(W)', 'Torque']] != 0).all(axis=1)]
    df['Power(W)'] = df['Power(W)'].astype(float)
    df['Torque'] = df['Torque'].astype(float)
    df['Power/Torque'] = (df['Power(W)'] * 1000) / df['Torque']
    df['Omega'] = (2 * (22/7) * df['Engine RPM']) / 60
    df['Speed_ratio'] = df['Power/Torque'] / df['Omega']
    df = df[df['Speed_ratio'] >= 1.2]
    df = df[df['Speed'] > 10]
    # print(df.shape)
    # print(df.head())

    count = []
    for i in range(df.shape[0]):
        count.append(df['Time'].iloc[i])
    # print(count)
    Sum = 0
    for i in range(len(count)-1):
        if (count[i+1] - count[i]) == 1:
            i += 4
            Sum += 1
        else:
            i += 1
            Sum += 0
    return Sum
