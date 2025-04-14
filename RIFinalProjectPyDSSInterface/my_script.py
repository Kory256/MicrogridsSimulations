import py_dss_interface
import os
import pathlib
import matplotlib.pyplot as plt

# find current path
script_path = os.path.dirname(os.path.abspath(__file__))

# import dss file
dss_file = os.path.join(script_path, 'feeders/NoWorkuy.dss')

dss = py_dss_interface.DSS()

dss.text(f"compile [{dss_file}]")

dss.text("solve")

# dss.text("show voltages")

# Extract data for plotting
voltages = dss.circuit_all_bus_voltages()
# Plot the voltages
plt.figure()
plt.plot(voltages)
plt.title('Bus Voltages')
plt.xlabel('Buses')
plt.ylabel('Voltage (pu)')
plt.show()