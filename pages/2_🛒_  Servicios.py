import streamlit as st
import numpy as np

st.title('Tu Diagnóstico🔎 nos indica que podemos ahorrarte💰:')

tab1, tab2 = st.tabs(["Ahorro en año 1", "Ahorro en año 2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

st.header('Ahorro en el año 1 (%)')
st.write([5, 9, 14, 17]) # see *

st.header('Ahorro en el año 5 (%)')
st.write([20, 36, 56, 68]) # see *

st.write(st.session_state.presupuesto)

st.write(st.session_state.consumo)


st.write(st.session_state.fuente)


st.write('Empecemos ahora 🕰')

st.write('¿Cómo materializaremos el ahorro?')
st.write('Transformaremos tu matriz energética hacia fuentes no solo más económicas sino también más sostenibles:')
st.write('Matriz Energética Actual Vs Proyectada')

