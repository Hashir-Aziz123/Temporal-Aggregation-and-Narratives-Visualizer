# src/data_loader.py
import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset(filepath):
    try:
        df = pd.read_csv(filepath, parse_dates=['utc_timestamp'], index_col='utc_timestamp')
        return df
    except FileNotFoundError:
        return None

def resample_data(df, res_code):
    """
    Resamples data and calculates Mean, Min, and Max for the Ribbon Chart.
    """
    if res_code == "H":
        return df.copy()
    else:
        # Calculate Mean, Min, and Max simultaneously
        agg = df.resample(res_code).agg(['mean', 'min', 'max'])
        # Flatten the MultiIndex columns (e.g., Load_DE -> Load_DE_mean)
        agg.columns = ['_'.join(col) for col in agg.columns]
        return agg
