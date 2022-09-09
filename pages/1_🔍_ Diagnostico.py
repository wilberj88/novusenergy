import streamlit as st


st.title('Diagnosticamos tu potencial ahorro energético')


st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000)

st.slider('En millones de pesos al año: ¿cuánto inviertes en energía?', 0, 100000000)

st.radio('Pick one', ['cats', 'dogs'])

# st.select_slider('¿Cuál es tu fuente principal de energía?', ['Agua', 'Combustible', 'Calor'])


# st.write('Indica la ubicación de la necesidad energética y el presupuesto anual disponible')
# map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [35.56, -74.04],
 #   columns=['lat', 'lon'])
# st.map(map_data)
