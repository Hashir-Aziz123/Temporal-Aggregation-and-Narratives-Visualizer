# Time as a First-Class Citizen: The Illusion of Aggregation
**CS-366 Data Visualization Course Project**

##  Project Overview
This interactive application demonstrates that statistical "truth" is not fixed—it is a function of time resolution. By allowing users to dynamically resample electricity demand data (from Hourly to Monthly), the tool reveals how aggregation can reverse trends, hide volatility, and manufacture false correlations.

**Core Thesis:** Aggregation is a modeling decision, not a neutral operation.

##  Dataset
**Source:** Open Power System Data (European Power Demand)
**Attributes Used:**
* Global Timestamp
* Electrical Load (Germany & France)
* Solar & Wind Generation (MW)

## 🛠 Features & Visualizations
1.  **Multi-Scale Resampling:** Dynamic slider to shift between H/D/W/M resolutions.
2.  **Correlation Matrix:** Visualizes how the relationship between Solar Gen and Grid Load shifts from negative (hourly) to positive (seasonal).
3.  **Variance Analysis:** "Box Plot over Time" showing the hidden extremes masked by averages.
4.  **Narrative Guardrails:** Contextual warnings that appear when aggregation levels risk hiding critical data points.

## How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the Streamlit app:
    ```bash
    streamlit run src/app.py
    ```

##  Project Structure
* `notebooks/`: Contains the data cleaning documentation and outlier analysis.
* `src/`: Contains the application logic.
* `data/`: Contains the processed time-series datasets.