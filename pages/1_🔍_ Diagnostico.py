import streamlit as st


st.title('Diagnosticamos tu potencial ahorro energético')


st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000, key="consumo")

st.slider('En millones de pesos al año: ¿cuánto inviertes en energía?', 0, 1000000, key="presupuesto")

st.radio('Cuál es tu fuente principal de energia', ['agua', 'carbon', 'combustible', 'termoelectrica', 'solar', 'viento'], key="tipo")
