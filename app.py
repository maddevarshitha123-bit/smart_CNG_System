"""Home page. Run with: streamlit run app.py"""

import streamlit as st

from utils.ui import setup_page, header
from config import MODEL_PATH


# Page setup
setup_page("Home")

# Header
header(
    "⛽ Smart CNG Finder",
    "AI-powered CNG availability prediction and navigation"
)


# Main features
c1, c2, c3 = st.columns(3)

c1.markdown(
    "#### 📍 Find stations\n"
    "Search nearby CNG stations with distance and travel time."
)

c2.markdown(
    "#### 🤖 AI prediction\n"
    "Predicted availability and waiting time from historical patterns."
)

c3.markdown(
    "#### ⭐ Recommendations\n"
    "A transparent score, not just the nearest station."
)


# Important information
st.info(
    "**Note:** Availability shown here is "
    "**AI Predicted Availability** based on historical "
    "(sample) data and station updates. It is **not** "
    "confirmed real-time fuel availability."
)


# System status
st.subheader("System status")

s1, s2 = st.columns(2)


# CSV station data status
s1.success("Station data: available")

s1.caption(
    "Using CSV-based station and historical data."
)


# ML model status
if MODEL_PATH.exists():

    s2.success("ML model: loaded")

else:

    s2.warning(
        "ML model: missing. Run "
        "`python generate_dataset.py` then "
        "`python -m ml.train_model`."
    )


# Sidebar information
st.markdown(
    "Use the **sidebar** to open Account, Find Stations, "
    "AI Prediction, Recommendations and more."
) 