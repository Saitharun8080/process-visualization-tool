import streamlit as st
from datetime import datetime
st.set_page_config(
    page_title="Process Visualization Tool",
    layout="wide",
    initial_sidebar_state="collapsed"
)
def main():
    st.title("About This Project")
    
    st.image("https://via.placeholder.com/800x200?text=Process+Scheduling+Visualizer", 
             use_container_width=True)
    
    st.header("🚀 Our Mission")
    st.markdown("""
    This tool was created to help students and professionals understand CPU scheduling algorithms 
    through interactive visualization and real-time system monitoring.
    """)
    
    with st.expander("📖 Background Information"):
        st.markdown("""
        ### What are CPU Scheduling Algorithms?
        CPU scheduling is a process that allows one process to use the CPU while 
        the execution of another process is on hold due to unavailability of any 
        resource like I/O etc.
        
        ### Why Visualization Matters
        Visualizing these algorithms helps in:
        - Understanding the theoretical concepts
        - Comparing algorithm performance
        - Seeing real-world system impacts
        """)
    
    st.header("👨‍💻 Development Team")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://via.placeholder.com/150?text=Team+Member", width=100)
        st.subheader("Your Name")
        st.markdown("""
        - Lead Developer
        - System Architecture
        - [GitHub](https://github.com/you)
        """)
    
    with col2:
        st.image("https://via.placeholder.com/150?text=Team+Member", width=100)
        st.subheader("Team Member")
        st.markdown("""
        - UI/UX Design
        - Documentation
        - [LinkedIn](#)
        """)
    
    with col3:
        st.image("https://via.placeholder.com/150?text=Team+Member", width=100)
        st.subheader("Advisor")
        st.markdown("""
        - Project Mentor
        - Algorithm Expert
        - [University](#)
        """)
    
    st.header("📚 Resources")
    st.markdown("""
    - **Source Code**: [GitHub Repository](https://github.com/your-repo)
    - **Documentation**: [ReadTheDocs](#)
    - **Report Issues**: [Issue Tracker](#)
    """)
    
    st.header("🛠️ Technologies Used")
    st.markdown("""
    - **Python** (Streamlit, Pandas, Matplotlib)
    - **System Monitoring** (psutil)
    - **Visualization** (Plotly, Altair)
    - **Deployment** (Docker, Heroku)
    """)
    
    st.markdown("---")
    st.markdown("""
    *Built with ❤️ for Operating Systems students and professionals*  
    *Version 1.0 | Last Updated: {date}*
    """.format(date=datetime.now().strftime("%B %Y")))

if __name__ == "__main__":
    main()
