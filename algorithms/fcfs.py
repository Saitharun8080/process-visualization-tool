import matplotlib.pyplot as plt

def fcfs_scheduling(processes):
    """
    Implements First-Come, First-Served (FCFS) Scheduling Algorithm.
    Returns: Start Time, Completion Time, Turnaround Time, Waiting Time as lists.
    """
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    start_time, completion_time, turnaround_time, waiting_time = [], [], [], []

    current_time = 0
    for pid, arrival, burst in processes:
        if current_time < arrival:
            current_time = arrival
        start_time.append(current_time)
        completion = current_time + burst
        completion_time.append(completion)
        turnaround_time.append(completion - arrival)
        waiting_time.append(current_time - arrival)
        current_time = completion

    return start_time, completion_time, turnaround_time, waiting_time  # ✅ Return only 4 lists

def generate_gantt_chart(df, bar_width=0.5):  # ✅ Add bar_width parameter
    fig, ax = plt.subplots(figsize=(10, 4))
    for i, (pid, st_time, bt) in enumerate(zip(df["Process"], df["Start Time"], df["Burst Time"])):
        ax.barh(y=pid, width=bt, left=st_time, height=bar_width, align="center")  # ✅ Use bar_width
        ax.text(st_time + bt / 2, i, f"{pid}", ha="center", va="center", color="white", fontsize=12)

    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title("Gantt Chart for FCFS Scheduling")
    ax.grid(axis="x", linestyle="--")

    return fig