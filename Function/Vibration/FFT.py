import numpy as np
from scipy.fftpack import fft

def do_fftx(t, x, y, z):
    sampling_frequency = 20
    sampling_time = 1.0/sampling_frequency

        # following is to calculate the fft
        # and then to scale it across the calculated frequency domain
    fft_array_x = fft(x)
    n = len(x)
    axis_for_fft_x = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_x = (2.0/n*np.abs(fft_array_x[0:n//2]))[1:]

    fft_array_y = fft(y)
    n = len(y)
    axis_for_fft_y = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_y = (2.0/n*np.abs(fft_array_y[0:n//2]))[1:]

    fft_array_z = fft(z)
    n = len(z)
    axis_for_fft_z = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_z = (2.0/n*np.abs(fft_array_z[0:n//2]))[1:]

    return axis_for_fft_x, amplitude_x, axis_for_fft_y, amplitude_y, \
           axis_for_fft_z, amplitude_z
