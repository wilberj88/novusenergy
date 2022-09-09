import streamlit as st
import pandas as pd
import numpy as np

st.title('Diagnosticamos tu potencial ahorro energético')


st.slider('En Megavatios: ¿cuál es tu consumo energético mensual?', 0, 100)

st.text_input("¿Cuál es tu presupuesto anual para consumo energético?")

st.text_input("¿Cuál es tu fuente principal de energía?")




# st.write('Indica la ubicación de la necesidad energética y el presupuesto anual disponible')
# map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [35.56, -74.04],
 #   columns=['lat', 'lon'])
# st.map(map_data)
