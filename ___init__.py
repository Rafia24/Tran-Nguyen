import streamlit as st
import pandas as pd
from _display import display_data


st.title('CSV Explorer')

expander = st.expander("ℹ️ - Streamlit application for performing data exploration on a CSV")

uploaded_file = expander.file_uploader('Choose a CSV file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    display_data(df)