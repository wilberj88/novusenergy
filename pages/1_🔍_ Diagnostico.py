import streamlit as st
import pandas as pd
import numpy as np

st.title('Diagnosticamos tu potencial ahorro energético')


st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000)

st.slider('En pesos cuánto es tu presupuesto energético anual?', 0, 1000000000)

st.selectbox('¿Cuál es tu fuente principal de energía?', ['agua', 'combustible', 'calor', 'carbón', 'termoeléctrica'])



# st.write('Indica la ubicación de la necesidad energética y el presupuesto anual disponible')
# map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [35.56, -74.04],
 #   columns=['lat', 'lon'])
# st.map(map_data)
