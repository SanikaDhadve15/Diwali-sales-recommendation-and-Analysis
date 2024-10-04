import streamlit as st
import pandas as pd
import chardet

def app():
    # File uploader
    uploaded_file = st.file_uploader("Upload your Diwali sales data (CSV)", type=["csv"])

    if uploaded_file is not None:
        # Detect encoding
        rawdata = uploaded_file.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
        
        # Move the cursor back to the beginning of the file
        uploaded_file.seek(0)

        # Read the data with the detected encoding
        try:
            data = pd.read_csv(uploaded_file, encoding=encoding)
            st.success("File loaded successfully!")

            # Store the DataFrame in session state
            st.session_state.data = data

            # Display the first few rows of the dataframe
            st.write("Preview of the data:")
            st.dataframe(data.head())
            st.write("Columns in the dataset:", data.columns.tolist())

            # Basic Analysis
            st.subheader("Basic Analysis")
            st.write("Total Number of Entries:", len(data))
            if 'Amount' in data.columns:
                st.write("Total Amount Spent:", data['Amount'].sum())
            if 'Orders' in data.columns:
                st.write("Total Number of Orders:", data['Orders'].sum())
                
            # Additional features can be added here

        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")
