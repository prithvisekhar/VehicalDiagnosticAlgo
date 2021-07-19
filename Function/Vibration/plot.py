import matplotlib.pyplot as plt

def fft_plot(FX_s, AX_s, FY_s, AY_s, FZ_s, AZ_s,
             FX_e, AX_e, FY_e, AY_e, FZ_e, AZ_e):

    plt.figure(figsize=(650, 650))

    plt.subplot(2, 3, 1)
    plt.plot(FX_s, AX_s, 'r', label='x fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in X direction at start')
    plt.legend()
    plt.grid()

    plt.subplot(2, 3, 2)
    plt.plot(FY_s, AY_s, 'b', label='y fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in Y direction at start')
    plt.legend()
    plt.grid()

    plt.subplot(2, 3, 3)
    plt.plot(FZ_s, AZ_s, 'g', label='z fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in Z direction at start')
    plt.legend()
    plt.grid()

    plt.subplot(2, 3, 4)
    plt.plot(FX_e, AX_e, 'r', label='x fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in X direction at end')
    plt.legend()
    plt.grid()

    plt.subplot(2, 3, 5)
    plt.plot(FY_e, AY_e, 'b', label='y fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in Y direction at end')
    plt.legend()
    plt.grid()

    plt.subplot(2, 3, 6)
    plt.plot(FZ_e, AZ_e, 'g', label='z fft')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude in Z direction at end')
    plt.legend()
    plt.grid()
    # plt.savefig('Overall.png')
    plt.show()
