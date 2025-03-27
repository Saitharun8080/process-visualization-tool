
import streamlit as st

# Set Page Configuration
st.set_page_config(
    page_title="Process Visualization Tool",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #eef2f5 100%);
    }
    
    /* Title styling */
    .title {
        text-align: center;
        color: #2E86C1;
        margin-bottom: 0.5rem;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(to right, #2E86C1, #4AA8FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
    }
    
    /* Card styling */
    .feature-card {
        border: none;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        background: white;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        color:black;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.12);
    }
    
    .card-title {
        color: #2E86C1;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .card-desc {
        color: #555;
        text-align: center;
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }
    
    .card-button {
        background: linear-gradient(to right, #2E86C1, #4AA8FF);
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 1rem;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(42, 134, 193, 0.3);
    }
    
    .card-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(42, 134, 193, 0.4);
    }
    
    /* Divider styling */
    .divider {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, transparent, #2E86C1, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 class='title'>Process Visualization Tool</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A modern tool to visualize CPU scheduling and system processes</p>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# Define pages with descriptions
pages = [
    {"title": "Real-time System Monitoring", "description": "View system processes and monitor resource usage in real-time with interactive dashboards.", "page": "Home"},
    {"title": "Process Scheduling", "description": "Simulate CPU scheduling algorithms like FCFS, SJF, RR, and Priority Scheduling with dynamic visualizations.", "page": "Scheduling"},
    {"title": "Analysis & Stats", "description": "View detailed Gantt charts, CPU utilization metrics, and comprehensive performance analysis.", "page": "Statistics"},
    {"title": "About Us", "description": "Browse and analyze past scheduling simulations with comparison tools.", "page": "About"},
]

# Display cards in a grid layout (2 columns, 2 rows)
cols = st.columns(2)  # 2 columns for better layout

# Loop through the pages and add each card in the grid layout
for i, page in enumerate(pages):
    with cols[i % 2]:  # Arrange in 2 columns
        st.markdown(
            f"""
            <div class="feature-card">
                <div>
                    <h2 class="card-title">{page['title']}</h2>
                    <p class="card-desc">{page['description']}</p>
                </div>
                <a href="{page['page']}" target="_self">
                    <button class="card-button">Go to {page['title']}</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
