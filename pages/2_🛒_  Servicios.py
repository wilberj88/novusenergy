import streamlit as st
import numpy as np

st.title('Tu Diagnóstico🔎 nos indica que podemos ahorrarte💰:')

tab1, tab2, tab3, tab4 = st.tabs(["En 1 año", "En 5 años", "En 10 años", "En 20 años"])
tab1.write("Entre un 15-27%")
tab2.write("Entre un 18-32%")
tab3.write("Entre un 45-82%")
tab4.write("Entre un 95-100%")

st.header('Lo anterior dado que tu presupuesto anual es:')
st.write(st.session_state.presupuesto)

st.header('Lo anterior dado que tu consumo promedio es:')
st.write(st.session_state.consumo)

st.header('Lo anterior dado que tu fuente principal de energía es:')
st.write(st.session_state.fuente)


st.write('¿Te parece que podemos ser tu solución energética ?Empecemos ahora 🕰')


