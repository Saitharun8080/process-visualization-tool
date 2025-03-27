import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from algorithms.fcfs import fcfs_scheduling, generate_gantt_chart as generate_fcfs_gantt
from algorithms.sjf import sjf_scheduling, generate_gantt_chart as generate_sjf_gantt
from algorithms.priority import priority_scheduling, generate_gantt_chart as generate_priority_gantt
from algorithms.round_robin import round_robin_scheduling, generate_gantt_chart as generate_rr_gantt

# Streamlit UI
st.title("Process Scheduling Visualization")

# Dropdown for selecting scheduling algorithm
algorithm = st.selectbox("Select Scheduling Algorithm", 
                        ["FCFS", "SJF", "Round Robin", "Priority Scheduling"])

# Algorithm-specific options
if algorithm == "SJF":
    sjf_mode = st.radio("SJF Mode", ["Non-Preemptive", "Preemptive"])
elif algorithm == "Priority Scheduling":
    priority_mode = st.radio("Priority Mode", ["Non-Preemptive", "Preemptive"])

num_processes = st.number_input("Number of processes", min_value=1, value=3, step=1)

# Collect Process Data
process_data = []
for i in range(num_processes):
    pid = f"P{i+1}"
    col1, col2 = st.columns(2)
    with col1:
        arrival = st.number_input(f"Arrival Time of {pid}", min_value=0, value=i)
    with col2:
        burst = st.number_input(f"Burst Time of {pid}", min_value=1, value=i+2)
    process_data.append((pid, arrival, burst))

# Additional inputs based on selected algorithm
if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1, value=2)
elif algorithm == "Priority Scheduling":
    priorities = []
    for i in range(num_processes):
        priority = st.number_input(f"Priority of P{i+1} (lower=higher priority)", 
                                 min_value=1, value=i+1)
        priorities.append(priority)

# Compute Scheduling on Button Click
if st.button("Compute Scheduling"):
    if not process_data:
        st.error("No processes entered! Please add at least one process.")
    else:
        try:
            if algorithm == "FCFS":
                start, completion, turnaround, waiting = fcfs_scheduling(process_data)
                fig = generate_fcfs_gantt(pd.DataFrame({
                    "Process": [p[0] for p in process_data],
                    "Start Time": start,
                    "Burst Time": [p[2] for p in process_data]
                }))
            elif algorithm == "SJF":
                preemptive = sjf_mode == "Preemptive"
                start, completion, turnaround, waiting, gantt = sjf_scheduling(process_data, preemptive)
                fig = generate_sjf_gantt(gantt)
            elif algorithm == "Round Robin":
                start, completion, turnaround, waiting, gantt = round_robin_scheduling(process_data, time_quantum)
                fig = generate_rr_gantt(gantt)
            elif algorithm == "Priority Scheduling":
                preemptive = priority_mode == "Preemptive"
                start, completion, turnaround, waiting, gantt = priority_scheduling(process_data, priorities, preemptive)
                fig = generate_priority_gantt(gantt)

            # Create DataFrame for Display
            df = pd.DataFrame({
                "Process": [p[0] for p in process_data],
                "Arrival Time": [p[1] for p in process_data],
                "Burst Time": [p[2] for p in process_data],
                "Start Time": start,
                "Completion Time": completion,
                "Turnaround Time": turnaround,
                "Waiting Time": waiting
            })

            # Add priority column if applicable
            if algorithm == "Priority Scheduling":
                df["Priority"] = priorities

            # Display DataFrame in Streamlit
            st.write("### Scheduling Table")
            st.dataframe(df)

            # Generate and Show Gantt Chart
            st.write("### Gantt Chart")
            st.pyplot(fig)

            # Calculate and display averages
            avg_turnaround = sum(turnaround) / len(turnaround)
            avg_waiting = sum(waiting) / len(waiting)
            
            st.write("### Performance Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Average Turnaround Time", f"{avg_turnaround:.2f}")
            col2.metric("Average Waiting Time", f"{avg_waiting:.2f}")

        except Exception as e:
            st.error(f"Error computing scheduling: {e}")
