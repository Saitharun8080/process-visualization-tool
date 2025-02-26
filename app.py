import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="Process Visualization Tool", layout="wide", initial_sidebar_state="collapsed")

# Page Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🚀 Process Visualization Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>A simple tool to visualize CPU scheduling and system processes.</p>", unsafe_allow_html=True)
st.markdown("---")

# Define pages with descriptions
pages = [
    {"title": "🏠 Home", "description": "View system processes and monitor resource usage in real-time.", "page": "Home"},
    {"title": "📅 Process Scheduling", "description": "Simulate CPU scheduling algorithms like FCFS, SJF, RR, and Priority Scheduling.", "page": "Scheduling"},
    {"title": "📊 Analysis & Stats", "description": "View Gantt charts, CPU utilization, and other performance metrics.", "page": "Statistics"},
    {"title": "📜 Previous Simulations", "description": "Browse and analyze past scheduling simulations (Optional).", "page": "History"},
]

# Display cards in a grid layout (2 columns, 2 rows)
cols = st.columns(2)  # 2 columns for better layout

# Loop through the pages and add each card in the grid layout
for i, page in enumerate(pages):
    with cols[i % 2]:  # Arrange in 2 columns
        st.markdown(
            f"""
            <div style="
                border: 2px solid #ddd; 
                padding: 20px; 
                border-radius: 15px; 
                margin-bottom: 20px; 
                background: linear-gradient(135deg, #F8F9FA, #D6EAF8); 
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.2s ease-in-out;
                height: 250px; /* Fixed height for all cards */
            " 
            onmouseover="this.style.transform='scale(1.03)'" 
            onmouseout="this.style.transform='scale(1)'">
                <h2 style="color: #2E86C1; text-align: center; font-size: 18px;">{page['title']}</h2>
                <p style="color: #555; text-align: center; font-size: 14px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{page['description']}</p>
                <div style="text-align: center; margin-top: 10px;">
                    <a href="{page['page']}" target="_self">
                        <button style="
                            background-color: #2E86C1; 
                            color: white; 
                            border: none; 
                            padding: 12px 24px; 
                            font-size: 16px; 
                            border-radius: 8px; 
                            cursor: pointer;
                            box-shadow: 2px 4px 6px rgba(0, 0, 0, 0.2);
                        ">Go to {page['title']}
                        </button>
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
