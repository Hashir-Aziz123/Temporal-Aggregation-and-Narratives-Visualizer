# src/visuals.py
import plotly.express as px
import plotly.graph_objects as go
from constants import COLORS

# --- VIZ 1: RIBBON CHART ---
def plot_ribbon_chart(df, label, res_code):
    fig = go.Figure()
    if res_code == "H":
        fig.add_trace(go.Scatter(x=df.index, y=df['Load_DE'], line=dict(color=COLORS['DE']), name="Hourly"))
    else:
        fig.add_trace(go.Scatter(x=df.index, y=df['Load_DE_max'], line=dict(width=0), showlegend=False))
        fig.add_trace(go.Scatter(x=df.index, y=df['Load_DE_min'], line=dict(width=0), fill='tonexty', fillcolor=COLORS['Ribbon'], name="Risk Range"))
        fig.add_trace(go.Scatter(x=df.index, y=df['Load_DE_mean'], line=dict(color=COLORS['DE']), name="Average"))
    fig.update_layout(title=f"1. Trend & Risk ({label})", height=350, margin=dict(l=0, r=0, t=30, b=0))
    return fig

# --- VIZ 2: COMPARISON ---
def plot_comparison(df, label, res_code):
    cols = ['Load_DE', 'Load_FR', 'Load_UK'] if res_code == "H" else ['Load_DE_mean', 'Load_FR_mean', 'Load_UK_mean']
    df_melted = df[cols].reset_index().melt(id_vars='utc_timestamp', var_name='Country', value_name='Load')
    color_map = {cols[0]: COLORS['DE'], cols[1]: COLORS['FR'], cols[2]: COLORS['UK']}
    fig = px.line(df_melted, x='utc_timestamp', y='Load', color='Country', title=f"2. Cross-Border Comparison ({label})", color_discrete_map=color_map)
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0), xaxis_title=None)
    return fig

# --- VIZ 3: HEATMAP ---
def plot_heatmap(df, label, res_code):
    cols = ['Load_DE', 'Solar_DE', 'Wind_DE', 'Load_FR'] if res_code == "H" else ['Load_DE_mean', 'Solar_DE_mean', 'Wind_DE_mean', 'Load_FR_mean']
    fig = px.imshow(df[cols].corr(), text_auto=".2f", aspect="auto", color_continuous_scale="RdBu_r", zmin=-1, zmax=1, title=f"3. Correlation Matrix ({label})")
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
    return fig

# --- VIZ 4: HISTOGRAM ---
def plot_distribution(df, label, res_code):
    target = 'Load_DE' if res_code == "H" else 'Load_DE_mean'
    fig = px.histogram(df, x=target, nbins=50, title=f"4. Distribution Shape ({label})", color_discrete_sequence=[COLORS['DE']], marginal="box")
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0), showlegend=False)
    return fig

# --- VIZ 5: RADAR CHART (FIXED) ---
def plot_radar_chart(df, label, res_code):
    """
    Shows the 'Shape' of the cycle.
    NOTE: We always use 'Load_DE' (Raw Column) here because 'df' passed 
    from app.py is always df_raw for this specific chart.
    """
    if res_code == "H":
        # Shape of a Day: Average Load per Hour (0-23)
        data = df.groupby(df.index.hour)['Load_DE'].mean().reset_index()
        theta = data['utc_timestamp']
    elif res_code == "D":
        # Shape of a Week: Average Load per Day Name (Mon-Sun)
        # FIX: Changed 'Load_DE_mean' to 'Load_DE'
        data = df.groupby(df.index.day_name())['Load_DE'].mean().reindex(
            ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']).reset_index()
        theta = data['utc_timestamp']
    else:
        # Shape of a Year: Average Load per Month (Jan-Dec)
        # FIX: Changed 'Load_DE_mean' to 'Load_DE'
        data = df.groupby(df.index.month_name())['Load_DE'].mean().reindex(
            ['January','February','March','April','May','June','July','August','September','October','November','December']).reset_index()
        theta = data['utc_timestamp']
        
    fig = px.line_polar(data, r=data.iloc[:,1], theta=theta, line_close=True, title=f"5. Cyclic Shape ({label})")
    fig.update_traces(fill='toself', line_color=COLORS['DE'])
    fig.update_layout(height=350, margin=dict(l=30, r=30, t=30, b=30))
    return fig

# --- VIZ 6: DECEPTION BAR CHART ---
def plot_difference_bar(df, label, res_code):
    """Calculates Max - Mean to show what we are losing"""
    if res_code == "H":
        return go.Figure().add_annotation(text="Zoom out to see the Deception Gap!", showarrow=False)
    
    monthly = df.resample('M').agg(['mean', 'max'])
    monthly.columns = ['_'.join(col) for col in monthly.columns]
    monthly['Gap'] = monthly['Load_DE_max'] - monthly['Load_DE_mean']
    
    fig = px.bar(monthly, x=monthly.index, y='Gap', title="6. The Deception Gap (Max - Mean)", color_discrete_sequence=[COLORS['Peak']])
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0), yaxis_title="Hidden Load (MW)")
    return fig
