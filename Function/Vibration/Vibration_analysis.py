import pandas as pd
from FFT import convert_to_freq_domain
from plot import fft_grpah

data = pd.read_csv('02-Jan-2020.csv')
df_head = pd.DataFrame()
df_head['T'] = data[' Device Time'].head(30)
df_head['X'] = data['Acceleration Sensor(X axis)(g)'].head(40)
df_head['Y'] = data['Acceleration Sensor(Y axis)(g)'].head(40)
df_head['Z'] = data['Acceleration Sensor(Z axis)(g)'].head(40)

df_tail = pd.DataFrame()
df_tail['T'] = data[' Device Time'].tail(30)
df_tail['X'] = data['Acceleration Sensor(X axis)(g)'].tail(30)
df_tail['Y'] = data['Acceleration Sensor(Y axis)(g)'].tail(30)
df_tail['Z'] = data['Acceleration Sensor(Z axis)(g)'].tail(30)


def get_data(T, Accx, Accy, Accz):
    t = []
    x = []
    y = []
    z = []

    for i in range(Accx.shape[0]):
        t.append(T.iloc[i])
        x.append(Accx.iloc[i])
        y.append(Accy.iloc[i])
        z.append(Accz.iloc[i])

    return t, x, y, z


A, B, C, D = get_data(df_head['T'], df_head['X'], df_head['Y'], df_head['Z'])
W, X, Y, Z = get_data(df_tail['T'], df_tail['X'], df_tail['Y'], df_tail['Z'])

FX_s, AX_s, FY_s, AY_s, FZ_s, AZ_s = convert_to_freq_domain(B, C, D)
FX_e, AX_e, FY_e, AY_e, FZ_e, AZ_e = convert_to_freq_domain(X, Y, Z)

fft_grpah(FX_s, AX_s, FY_s, AY_s, FZ_s, AZ_s, FX_e, AX_e, FY_e, AY_e, FZ_e, AZ_e)
