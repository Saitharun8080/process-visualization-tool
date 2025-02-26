import psutil
import pandas as pd

def get_process_info():
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            processes.append({
                "PID": info["pid"],
                "Name": info["name"],
                "CPU %": info["cpu_percent"] if info["cpu_percent"] is not None else 0.0,  # Replace None with 0
                "Memory %": info["memory_percent"] if info["memory_percent"] is not None else 0.0,  # Replace None with 0
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip inaccessible or zombie processes

    # Sort: First by CPU% (Descending), then by Memory% (Descending)
    df = pd.DataFrame(processes)
    df = df.sort_values(by=["CPU %", "Memory %"], ascending=[False, False])

    return df