import matplotlib.pyplot as plt


def check_performance(Upstream_O2, downstream_O2, Time, Speed):
    plt.subplot(2, 1, 1)
    plt.plot(Time, Upstream_O2)
    plt.plot(Time, downstream_O2)
    plt.axhline(y=0.6, color='g', linestyle='--')
    plt.axhline(y=0.9, color='g', linestyle='--')
    plt.xlabel('time')
    plt.ylabel('O2 sensor value')
    plt.legend(['Upstream', 'downstrem'], loc='lower right')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(Time, Speed)
    plt.xlabel('time')
    plt.ylabel('speed (m/s)')
    # plt.legend()
    plt.grid()

    # plt.savefig('Catalyst performance_2')
    plt.show()
