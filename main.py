import streamlit as st
from data_upload_analysis import data_analysis  # Ensure this matches your file name
from visualizations import show_visualizations  # Ensure this matches your file name
from recommendations import generate_recommendations  # Ensure this matches your file name

def main():
    st.set_page_config(page_title="Diwali Sales Analysis")

    st.sidebar.title("Dashboard")
    page = st.sidebar.radio("Select Page", ["Data Upload & Analysis", "Visualizations", "Recommendations"])

    if page == "Data Upload & Analysis":
        data_analysis()  # Function to handle data upload and analysis
    elif page == "Visualizations":
        show_visualizations()  # Function to display various visualizations
    elif page == "Recommendations":
        generate_recommendations()  # Function to generate product recommendations

if __name__ == "__main__":
    main()