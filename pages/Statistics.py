import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
st.set_page_config(
    page_title="Process Visualization Tool",
    layout="wide",
    initial_sidebar_state="collapsed"
)
def main():
    st.title("📊 Performance Analysis")
    
    # Check for simulation history
    if 'simulation_history' not in st.session_state or not st.session_state.simulation_history:
        st.warning("No simulation data available. Run some scheduling simulations first.")
        return
    
    # Convert history to DataFrame
    history_data = []
    for entry in st.session_state.simulation_history:
        history_data.append({
            'timestamp': entry['timestamp'],
            'algorithm': entry['algorithm'],
            'avg_waiting': entry['results']['avg_waiting'],
            'avg_turnaround': entry['results']['avg_turnaround'],
            'throughput': entry['results'].get('throughput', 0),  # Handle cases where throughput might not exist
            'num_processes': entry['num_processes']
        })
    
    df = pd.DataFrame(history_data)
    
    # Metrics overview
    st.subheader("Performance Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Best Avg Waiting Time", f"{df['avg_waiting'].min():.2f}")
    col2.metric("Best Avg Turnaround", f"{df['avg_turnaround'].min():.2f}")
    col3.metric("Highest Throughput", f"{df['throughput'].max():.2f}")
    
    # Visualization
    st.subheader("Trend Analysis")
    
    tab1, tab2, tab3 = st.tabs(["Waiting Time", "Turnaround Time", "Throughput"])
    
    with tab1:
        fig, ax = plt.subplots()
        ax.bar(df['algorithm'], df['avg_waiting'])
        ax.set_title("Average Waiting Time Comparison")
        ax.set_ylabel("Time Units")
        st.pyplot(fig)
    
    with tab2:
        fig, ax = plt.subplots()
        ax.plot(df['algorithm'], df['avg_turnaround'], marker='o')
        ax.set_title("Turnaround Time Trend")
        ax.set_ylabel("Time Units")
        st.pyplot(fig)
    
    with tab3:
        fig, ax = plt.subplots()
        ax.barh(df['algorithm'], df['throughput'])
        ax.set_title("Throughput Comparison")
        ax.set_xlabel("Processes per Time Unit")
        st.pyplot(fig)
    
    # Raw data
    st.subheader("Simulation History Data")
    st.dataframe(df)

if __name__ == "__main__":
    main()
