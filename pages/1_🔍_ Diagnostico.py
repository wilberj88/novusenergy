import streamlit as st
import pandas as pd
import numpy as np

st.title('Diagnosticamos tu potencial ahorro energético')
st.write('Indica las ubicaciones que requieres y el presupuesto anual disponible')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
