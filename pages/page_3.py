import streamlit as st
import pandas as pd
import numpy as np


COLUMNS = ["price", "level", "levels", "rooms", "area", "kitchen_area"]


st.title("Визуализация распределний характеристик")

selected_col = st.selectbox("Выберите столбец:", COLUMNS)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)