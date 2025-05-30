import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Streamlit interface for file upload
st.title('CSV File Uploader')
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write('Data Preview:', df.head())

    # Send the file to FastAPI backend
    response = requests.post('http://localhost:8000/process', files={'file': uploaded_file})
    processed_data = response.json()

    # Display processed data
    st.write('Processed Data:', processed_data)

    # Plotly visualization
    fig = px.scatter(processed_data, x='column_x', y='column_y')
    st.plotly_chart(fig)