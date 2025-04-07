import streamlit as st
import pandas as pd
import time
import psutil  # Import psutil for system metrics
from utils.helpers import get_process_info  # Import process fetching function
# st.set_page_config(
#     page_title="Process Visualization Tool",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )
# Set Page Config
st.set_page_config(page_title="Process Visualization Tool", layout="wide", initial_sidebar_state="collapsed")


# Title and Description
st.title("🏠 Home - Process Visualization Tool")
st.write("Welcome to the Process Visualization Tool! 🚀")
st.write("This page displays the currently running processes on your system.")

st.subheader("🔍 Running Processes")

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = get_process_info()  # Store DataFrame in session state

if "refresh_rate" not in st.session_state:
    st.session_state.refresh_rate = 1  # Default refresh rate (1 second)

# New Feature: System Overview (Process Count, CPU, Memory & Disk Usage)
st.markdown("### ⚡ System Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="📌 Total Processes", value=len(st.session_state.df))

with col2:
    cpu_usage = psutil.cpu_percent(interval=1)
    st.metric(label="💻 CPU Usage (%)", value=f"{cpu_usage}%")

with col3:
    memory_usage = psutil.virtual_memory().percent
    st.metric(label="🧠 Memory Usage (%)", value=f"{memory_usage}%")

with col4:
    disk_usage = psutil.disk_usage("/").percent
    st.metric(label="💾 Disk Usage (%)", value=f"{disk_usage}%")

# New Feature: Top 5 CPU-Consuming Processes
st.markdown("### 🔥 Top 5 CPU-Consuming Processes")
processes = []
for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent"]):
    processes.append(proc.info)

df_top_cpu = pd.DataFrame(processes).sort_values(by="cpu_percent", ascending=False).head(5)
st.dataframe(df_top_cpu, use_container_width=True)



# Display all running processes
st.subheader("📋 All Running Processes")
st.dataframe(st.session_state.df, use_container_width=True)

# Auto-refresh logic (without user controls)
time.sleep(st.session_state.refresh_rate)
st.session_state.df = get_process_info()  # Update only data
st.rerun()  # Refresh without blinking