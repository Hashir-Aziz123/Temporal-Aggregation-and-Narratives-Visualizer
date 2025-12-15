# src/app.py
import streamlit as st
import data_loader as dl
import visuals as viz
from constants import INSIGHTS, RESOLUTION_MAP

st.set_page_config(page_title="Temporal Illusions", layout="wide", page_icon="⏳")

# --- LOAD DATA ---
df_raw = dl.load_dataset('data/processed/electricity_cleaned.csv')
if df_raw is None: st.stop()

# --- SIDEBAR ---
st.sidebar.title("Controls")
selected_res_label = st.sidebar.select_slider("Resolution", options=list(RESOLUTION_MAP.keys()), value="Hourly (Raw)")
res_code = RESOLUTION_MAP[selected_res_label]
df_agg = dl.resample_data(df_raw, res_code)

# --- HEADER ---
st.title("Time as a First-Class Citizen")
st.markdown("**Thesis:** Aggregation is a lie. See how 6 different truths emerge from 1 dataset.")
st.markdown("---")

# --- ROW 1: THE BASICS (Trend + Comparison) ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(viz.plot_ribbon_chart(df_agg, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 1'][res_code]}")

with col2:
    st.plotly_chart(viz.plot_comparison(df_agg, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 2'][res_code]}")

st.markdown("---")

# --- ROW 2: STATISTICAL SHIFTS (Heatmap + Histogram) ---
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(viz.plot_heatmap(df_agg, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 3'][res_code]}")

with col4:
    st.plotly_chart(viz.plot_distribution(df_agg, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 4'][res_code]}")

st.markdown("---")

# --- ROW 3: ADVANCED SHAPES (Radar + Deception Bar) ---
col5, col6 = st.columns(2)
with col5:
    st.plotly_chart(viz.plot_radar_chart(df_raw, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 5'][res_code]}")

with col6:
    st.plotly_chart(viz.plot_difference_bar(df_raw, selected_res_label, res_code), use_container_width=True)
    st.info(f"**Insight:** {INSIGHTS['Panel 6'][res_code]}")
