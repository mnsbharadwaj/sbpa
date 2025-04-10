import numpy as np
import matplotlib.pyplot as plt

# Kyber operations
kyber_operations = ["Forward NTT", "Backward NTT", "Pointwise Multiplication"]

# Power consumption (nJ)
power_consumption = {
    "Cortex-M4": [85000, 82000, 78000],
    "RISC-V RV64GC": [72000, 70000, 68000]
}

# Execution time (arbitrary units)
execution_time = {
    "Cortex-M4": [300, 280, 260],
    "RISC-V RV64GC": [250, 230, 220]
}

# X-axis positions
x = np.arange(len(kyber_operations))
bar_width = 0.35

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar chart for power consumption
bars1 = ax1.bar(x - bar_width/2, power_consumption["Cortex-M4"], bar_width, label="Cortex-M4 Power (nJ)", color='royalblue', alpha=0.7)
bars2 = ax1.bar(x + bar_width/2, power_consumption["RISC-V RV64GC"], bar_width, label="RISC-V Power (nJ)", color='darkorange', alpha=0.7)

# Secondary y-axis for execution time
ax2 = ax1.twinx()
lines1 = ax2.plot(x, execution_time["Cortex-M4"], marker='o', linestyle='-', color='blue', label="Cortex-M4 Time (units)")
lines2 = ax2.plot(x, execution_time["RISC-V RV64GC"], marker='s', linestyle='-', color='red', label="RISC-V Time (units)")

# Labels and title
ax1.set_xlabel("Kyber Operation")
ax1.set_ylabel("Power Consumption (nJ)", color='black')
ax2.set_ylabel("Execution Time (Arbitrary Units)", color='black')
ax1.set_title("Power & Execution Time for Kyber Operations on Cortex-M4 vs RISC-V RV64GC")
ax1.set_xticks(x)
ax1.set_xticklabels(kyber_operations)

# Legends
bars = bars1 + bars2
lines = lines1 + lines2
all_labels = [bar.get_label() for bar in bars] + [line.get_label() for line in lines]
ax1.legend(tuple(bars) + tuple(lines) , all_labels, loc="upper left")

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
