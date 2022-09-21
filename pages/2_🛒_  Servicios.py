import streamlit as st
import numpy as np

st.title('Tu Diagnóstico🔎 nos indica que podemos ahorrarte💰:')

tab1, tab2, tab3, tab4 = st.tabs(["En 1 año", "En 5 años", "En 10 años", "En 20 años"])
tab1.write("Entre un 15-27%")
tab2.write("Entre un 18-32%")
tab3.write("Entre un 45-82%")
tab4.write("Entre un 95-100%")

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

