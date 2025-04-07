import matplotlib.pyplot as plt
from pydss import PyDSS

def plot_voltages():
    pydss = PyDSS("project.json", "default")
    results = pydss.get_full_results()
    voltages = results["Buses"]["MG2"]["VoltageMagPu"]
    
    plt.plot(voltages, label="Voltage (pu)")
    plt.title("Microgrid Voltage Stability")
    plt.legend()
    plt.savefig("results/voltage_plot.png")  # Save to repo
    plt.show()

if __name__ == "__main__":
    plot_voltages()