import re
import matplotlib.pyplot as plt

def analyze_trace(trace_output):
    """Parse QEMU trace logs to count instructions and memory accesses."""
    instruction_count = len(re.findall(r"IN:", trace_output))
    mem_access_count = len(re.findall(r"MEM:", trace_output))
    return instruction_count, mem_access_count

def estimate_power_time(instr_count, mem_count, cycle_per_instr, energy_per_instr, cpu_freq):
    """Estimate execution time and energy consumption."""
    total_cycles = instr_count * cycle_per_instr
    execution_time = total_cycles / cpu_freq
    total_energy = instr_count * energy_per_instr
    return execution_time, total_energy

def plot_results(results):
    """Plot execution time and energy consumption for different architectures."""
    architectures = list(results.keys())
    exec_times = [results[arch]['time'] for arch in architectures]
    energy_usage = [results[arch]['energy'] for arch in architectures]
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('Architecture')
    ax1.set_ylabel('Execution Time (s)', color=color)
    ax1.bar(architectures, exec_times, color=color, alpha=0.6, label='Execution Time')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Energy Consumption (J)', color=color)
    ax2.bar(architectures, energy_usage, color=color, alpha=0.6, label='Energy Consumption')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('QEMU Profiling: Execution Time & Energy Consumption (Optimized with Vectorization)')
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    binaries = {
        "Cortex-M3 (Optimized)": {"cycle_per_instr": 1.1, "energy_per_instr": 0.4e-9, "cpu_freq": 120e6},
        "RISC-V (Optimized)": {"cycle_per_instr": 1.0, "energy_per_instr": 0.3e-9, "cpu_freq": 100e6},
        "RISC-V (Vectorized)": {"cycle_per_instr": 0.7, "energy_per_instr": 0.2e-9, "cpu_freq": 120e6}
    }
    
    
    results = {}
    for arch, params in binaries.items():
        # Simulated trace output (Replace with actual trace log parsing if available)
        trace_output = "IN:\n" * 1000000 + "MEM:\n" * 400000  # Simulated data
        instr_count, mem_count = analyze_trace(trace_output)
        exec_time, energy_used = estimate_power_time(instr_count, mem_count, params["cycle_per_instr"], params["energy_per_instr"], params["cpu_freq"])
        results[arch] = {"time": exec_time, "energy": energy_used}
        
        print(f"{arch} - Instructions executed: {instr_count}")
        print(f"{arch} - Memory accesses: {mem_count}")
        print(f"{arch} - Estimated Execution Time: {exec_time:.6f} sec")
        print(f"{arch} - Estimated Energy Consumption: {energy_used:.6e} J")
    
    plot_results(results)
