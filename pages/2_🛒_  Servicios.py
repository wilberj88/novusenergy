import streamlit as st
import numpy as np

consumo = st.session_state.consumo
presupuesto = st.session_state.presupuesto
tipo = st.session_state.tipo

ahorro_uno = presupuesto*0,2

st.title('Tu Diagnóstico🔎 nos indica cuánto podemos ahorrarte💰:')
st.write('En 1 año:')

st.write(ahorro_uno)

st.write('En 5 años:')

st.write('El portafolio de servicios personalizado 🛒 a tu necesidad🎯 es:')

st.write('BLA BLA BLA')

st.write('Empecemos ahora 🕰')

st.write('¿Cómo materializaremos el ahorro?')
st.write('Transformaremos tu matriz energética hacia fuentes no solo más económicas sino también más sostenibles:')
st.write('Matriz Energética Actual Vs Proyectada')

