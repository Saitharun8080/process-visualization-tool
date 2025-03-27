import matplotlib.pyplot as plt
from collections import deque

def round_robin_scheduling(processes, time_quantum):
    """
    Implements Round Robin Scheduling Algorithm.
    Args:
        processes: List of tuples (pid, arrival_time, burst_time)
        time_quantum: Time quantum for RR scheduling
    Returns: Start Time, Completion Time, Turnaround Time, Waiting Time, Gantt data
    """
    processes = sorted(processes, key=lambda x: x[0])  # Sort by PID for consistent order
    n = len(processes)
    burst_remaining = [p[2] for p in processes]
    start_time = [-1] * n
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0
    gantt = []
    
    # Create a queue for ready processes
    queue = deque()
    completed = 0
    arrived = [False] * n
    
    while completed != n:
        # Add newly arrived processes to queue
        for i in range(n):
            if not arrived[i] and processes[i][1] <= current_time and burst_remaining[i] > 0:
                arrived[i] = True
                queue.append(i)
        
        if not queue:
            current_time += 1
            continue
        
        # Get next process from queue
        idx = queue.popleft()
        
        if start_time[idx] == -1:
            start_time[idx] = current_time
        
        # Execute for time quantum or until completion
        exec_time = min(time_quantum, burst_remaining[idx])
        burst_remaining[idx] -= exec_time
        gantt.append((processes[idx][0], current_time, current_time + exec_time))
        current_time += exec_time
        
        # Check if process completed
        if burst_remaining[idx] == 0:
            completed += 1
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - processes[idx][1]
            waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
        else:
            # Re-add to queue if not completed
            queue.append(idx)
    
    return start_time, completion_time, turnaround_time, waiting_time, gantt

def generate_gantt_chart(gantt_data, bar_width=0.5):
    """Generate Gantt chart from scheduling data"""
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Create a mapping from process to y-position
    processes = sorted({p[0] for p in gantt_data})
    y_pos = {p: i for i, p in enumerate(processes)}
    
    for pid, start, end in gantt_data:
        duration = end - start
        ax.barh(y=y_pos[pid], width=duration, left=start, height=bar_width, align='center')
        ax.text(start + duration/2, y_pos[pid], f"{pid}", ha='center', va='center', color='white', fontsize=10)
    
    ax.set_yticks(range(len(processes)))
    ax.set_yticklabels(processes)
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title("Gantt Chart for Round Robin Scheduling")
    ax.grid(axis='x', linestyle='--')
    
    return fig
