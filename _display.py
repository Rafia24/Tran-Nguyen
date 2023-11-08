import pandas as pd
import streamlit as st
from _logics import data_analysis
from _logics import list_of_columns


def display_data(df):
    tab1, tab2, tab3, tab4 = st.tabs(["DataFrame", "Numeric Series", "Time Series", "Datetime Series"])
    with (tab1):
        expander = st.expander('DataFrame')
        analyzed_data = data_analysis(df)
        expander.table(pd.DataFrame(analyzed_data))
        column_details = list_of_columns(df)
        st.subheader('Columns')
        st.table(column_details)

        expander = st.expander('Explore Dataframe')
        num_of_rows = expander.slider('Select the number of rows to be displayed',5,50)
        chosen_logics = expander.radio(
               'Exploration Method',
               ['Head','Tail','Sample']
        )
        expander.subheader("Top Rows of Selected Table")

        if chosen_logics == 'Head':
            expander.dataframe(df.head(num_of_rows))
        elif chosen_logics == 'Tail':
            expander.dataframe(df.tail(num_of_rows))
        else:
            expander.dataframe(df.sample(num_of_rows))