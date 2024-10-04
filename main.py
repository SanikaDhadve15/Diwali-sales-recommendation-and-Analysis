import streamlit as st
from data_upload_analysis import data_analysis  # Ensure this matches your file name

def main():
    st.set_page_config(page_title="Diwali Sales Analysis")

    st.sidebar.title("Dashboard")
    page = st.sidebar.radio("Select Page", ["Data Upload & Analysis", "Visualizations", "Recommendations"])

    if page == "Data Upload & Analysis":
        data_analysis()
    # You can add additional pages here for Visualizations and Recommendations

if __name__ == "__main__":
    main()
