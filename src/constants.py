# src/constants.py

# --- ACCESSIBLE COLOR PALETTE (Okabe-Ito) ---
COLORS = {
    'DE': '#009E73',      # Teal (Safe Green)
    'FR': '#D55E00',      # Vermilion (Safe Red)
    'UK': '#0072B2',      # Blue
    'Ribbon': 'rgba(0, 158, 115, 0.2)', # Transparent Teal
    'Peak': '#D55E00',    # Risk/Warning Color
    'Avg': '#0072B2'      # Safe/Neutral Color
}

# --- RESOLUTION MAPPING ---
RESOLUTION_MAP = {
    "Hourly (Raw)": "H", 
    "Daily (24H)": "D", 
    "Weekly (7D)": "W", 
    "Monthly (30D)": "M"
}

# --- ANALYTICAL INSIGHTS ENGINE ---
INSIGHTS = {
    "Panel 1": { # Ribbon Chart (Trend & Risk)
        "H": "Operational Reality (High Volatility). The raw signal reveals the stochastic nature of the grid. Note the rapid oscillation driven by the diurnal cycle (human sleep/wake patterns). This noise is the primary operational challenge for grid stability.",
        "D": "Aliasing Effect. Aggregating to daily averages removes the intra-day volatility. The 'weekend dip' (industrial slowdown) becomes the dominant high-frequency pattern, masking the daily peak load stress.",
        "W": "Weather Dominance. Human daily cycles are smoothed out completely. The remaining variance is primarily driven by synoptic weather patterns (e.g., cold fronts passing through for a week).",
        "M": "The Stability Illusion. Monthly aggregation creates a smooth, U-shaped seasonal curve. However, the wide 'Risk Ribbon' (Min/Max area) proves that while the trend appears stable, the underlying operational risk remains critically high."
    },
    "Panel 2": { # Comparison Line (Infrastructure)
        "H": "Infrastructure Sensitivity. Compare France (Red) vs. Germany (Green). France's grid exhibits sharp, needle-like spikes in winter due to high elasticity with temperature (Electric Heating), whereas Germany's gas-reliant infrastructure is more stable.",
        "D": "Economic Synchronization. At this resolution, the economies move in lockstep, revealing deep regional integration. Workdays, holidays, and industrial shifts align perfectly across borders.",
        "W": "Baseload Separation. Weekly smoothing removes the noise of individual days, allowing for a clear structural comparison of national baseloads. The UK consistently isolates at the lower bound due to population scale and gas heating reliance.",
        "M": "Structural Divergence. The 'Summer Dip' reveals infrastructure strategy. France's demand collapses most dramatically in summer, confirming its structural dependency on heating load compared to the flatter profiles of the UK and Germany."
    },
    "Panel 3": { # Heatmap (Correlation)
        "H": "Positive Operational Correlation (+). In the short term, Solar generation and Demand are positively linked. Daylight drives human activity (and thus load), creating a coincidence of supply and demand.",
        "D": "Decoupling Zone (Noisy). The relationship weakens as the time-of-day signal is removed. A sunny day does not necessarily imply high demand (e.g., a sunny Sunday), breaking the operational link.",
        "W": "Inversion Onset (Transition). The correlation begins to trend negative. We are moving away from daily activity patterns and entering the domain of seasonal weather patterns.",
        "M": "Simpson's Paradox (Strong Negative -). The correlation completely reverses. Solar generation peaks in Summer, while Demand peaks in Winter. Long-term seasonal anti-phase dominates the short-term operational link."
    },
    "Panel 4": { # Distribution Histogram
        "H": "Platykurtic Distribution (High Variance). The wide spread indicates a system with 'fat tails'—frequent extreme low and high load events. This represents the true risk profile of the grid.",
        "D": "Variance Reduction. The distribution begins to narrow. Extreme hourly peaks are averaged into daily means, effectively deleting the 'tail risk' from the visual representation.",
        "W": "Central Tendency Reinforcement. The distribution tightens further. We are now only observing the variance of weekly weather patterns, losing all information about daily grid stress.",
        "M": "Leptokurtic Shift (False Normality). The distribution becomes narrow and peaked. Over 90% of the variance has been smoothed away, presenting a 'safe' bell curve that hides the reality of blackouts and surges."
    },
    "Panel 5": { # Radar Chart
        "H": "The 'Diurnal Clock'. The shape is driven by the 24-hour cycle, bulging at 12:00 (Noon) and retracting at 04:00 (Night). This captures human circadian rhythms.",
        "D": "The 'Weekly Star'. The geometry reveals the industrial week: 5 extended points (Weekdays) and 2 retracted points (Weekends).",
        "W": "The 'Stochastic Blob'. The geometric regularity vanishes. The shape is irregular and unpredictable, driven by random weather events rather than human schedules.",
        "M": "The 'Seasonal Diamond'. A clean, elongated shape pointing towards the winter months (Jan/Dec). The cycle is now purely climatic."
    },
    "Panel 6": { # Deception Bar
        "H": "Gap = 0. Reality is observed 1:1. No information is lost.",
        "D": "Minor Underestimation. Daily averages hide the specific hour of peak stress, slightly under-representing capacity requirements.",
        "W": "Significant Deviation. Weekly averages fail to capture the coldest day of the week, creating a safety gap in planning.",
        "M": "Critical Failure Mode. Monthly averaging systematically underestimates grid stress by >15GW. A grid planned on 'Average Monthly Load' would fail immediately during a winter peak."
    }
}
