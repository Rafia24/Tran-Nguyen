import pandas as pd


def data_analysis(data):
    num_rows = data.shape[0]
    num_cols = data.shape[1]
    num_duplicate = data.duplicated().sum()
    num_missing = data.isnull().any(axis=1).sum()

    data = {
        "Description": ["Number of Rows", "Number of Columns", "Number of Duplicate Rows",
                        "Number of Rows with Missing Values"],
        "Value": [num_rows, num_cols, num_duplicate, num_missing]
    }

    return data


def list_of_columns(df):

    #Creating dictionary to store column-wise memory usage
    column_memory_usage = {}

    for col in df.columns:

        #Calculating memory usage for each column and converting to KB
        memory_usage = int(df[col].memory_usage(deep=True) / (1024))
        column_memory_usage[col] = memory_usage


    data = {
        "column": list(column_memory_usage.keys()),
        "data_type": list(df.dtypes),
        "memory": list(column_memory_usage.values())
    }

    return data
