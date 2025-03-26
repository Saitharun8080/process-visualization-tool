import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from algorithms.fcfs import fcfs_scheduling
from algorithms.fcfs import generate_gantt_chart  # Import functions

# Streamlit UI
st.title("Process Scheduling Visualization")

# Dropdown for selecting scheduling algorithm
algorithm = st.selectbox("Select Scheduling Algorithm", ["FCFS", "SJF", "Round Robin", "Priority Scheduling"])

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

# Dynamically show additional inputs based on selected algorithm
if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1, value=2)
elif algorithm == "Priority Scheduling":
    priorities = []
    for i in range(num_processes):
        priority = st.number_input(f"Priority of {pid}", min_value=1, value=1)
        priorities.append(priority)

# Compute Scheduling on Button Click
if st.button("Compute Scheduling"):
    if not process_data:
        st.error("No processes entered! Please add at least one process.")
    else:
        try:
            if algorithm == "FCFS":
                result = fcfs_scheduling(process_data)
            elif algorithm == "SJF":
                result = sjf_scheduling(process_data)
            elif algorithm == "Round Robin":
                result = round_robin_scheduling(process_data, time_quantum)
            elif algorithm == "Priority Scheduling":
                result = priority_scheduling(process_data, priorities)

            # ✅ Ensure the function returns exactly 4 lists
            if isinstance(result, tuple) and len(result) == 4:
                start, completion, turnaround, waiting = result
            else:
                raise ValueError("Unexpected return format from scheduling algorithm")

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

            # Display DataFrame in Streamlit
            st.write("### Scheduling Table")
            st.dataframe(df)

            # Generate and Show Gantt Chart with adjusted bar width
            fig = generate_gantt_chart(df, bar_width=0.4)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error computing scheduling: {e}")