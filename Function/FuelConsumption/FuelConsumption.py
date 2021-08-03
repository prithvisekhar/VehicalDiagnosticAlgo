import matplotlib.pyplot as plt

# create figure and axis objects with subplots()
def fuel_monitoring(EL, FM, speed, KMPL):
    fig, ax = plt.subplots()
    ax.plot(EL, color="red")
    ax.set_xlabel("Index", fontsize=14)
    ax.set_ylabel("Engine load", color="red", fontsize=14)

    # twin object for two different y-axis on the sample plot
    ax2 = ax.twinx()
    ax2.plot(FM, color="blue")
    ax2.set_ylabel("Fuel mass consumption", color="blue", fontsize=14)
    plt.show()
    # fig.savefig('Engine load_Fuel mass consumption_5')

    fig2, ax3 = plt.subplots()
    ax3.plot(speed, color="red")
    ax3.set_xlabel("Index", fontsize=14)
    ax3.set_ylabel("Vehicle_speed", color="red", fontsize=14)

    # twin object for two different y-axis on the sample plot
    ax4 = ax3.twinx()
    ax4.set_ylim(8, 16)
    ax4.plot(KMPL, color="blue")
    ax4.set_ylabel("KM per Liter", color="blue", fontsize=14)
    plt.yticks(KMPL)
    # ax4.set_ylim(8,16)
    plt.show()
    # fig2.savefig('Vehicle speed_KM per litre_5')
