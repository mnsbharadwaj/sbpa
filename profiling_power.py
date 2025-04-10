import numpy as np
import matplotlib.pyplot as plt

# Sample instruction count and energy values (Modify based on profiling)
instructions = ["Forward NTT", "Backward NTT", "Pointwise Multiplication"]
cortex_power = [85_000, 82_000, 78_000]  # Example nJ values for Cortex-M4
riscv_power = [72_000, 70_000, 68_000]   # Example nJ values for RISC-V

# Plot the comparison
plt.figure(figsize=(8,5))
x = np.arange(len(instructions))
plt.bar(x - 0.2, cortex_power, width=0.4, label="Cortex-M4", color="blue")
plt.bar(x + 0.2, riscv_power, width=0.4, label="RISC-V", color="red")

plt.xticks(x, instructions)
plt.xlabel("Kyber Operations")
plt.ylabel("Power Consumption (nJ)")
plt.title("Power Comparison: Cortex-M vs RISC-V")
plt.legend()
plt.grid()

# Save the figure instead of displaying it
plt.savefig("kyber_power_comparison.png")

print("Graph saved as 'kyber_power_comparison.png'")
