import streamlit as st
import pandas as pd
# import numpy as np
st.sidebar.selectbox("")
from main import get_infectious_data
data, columns = get_infectious_data("infection_case")
# print(data, columns)
st.header("COVID Tracker")
st.subheader("Top 10 infectious case sources")
chart_data = pd.DataFrame(
data,
columns=columns)

st.table(chart_data)

# st.sidebar.selectbox("Select the state", ['isolated', 'deceased', 'released'])