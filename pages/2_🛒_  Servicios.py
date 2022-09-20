import streamlit as st
import numpy as np

st.title('Tu Diagnóstico🔎 nos indica que podemos ahorrarte💰:')


st.header('Ahorro en el año 1')

st.header('Ahorro en el año 5')


st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')

st.subheader('My sub')

st.write('En 1 año:')

st.write(st.session_state.presupuesto)


st.write('En 5 años:')

st.write('El portafolio de servicios personalizado 🛒 a tu necesidad🎯 es:')

st.write('BLA BLA BLA')

st.write('Empecemos ahora 🕰')

st.write('¿Cómo materializaremos el ahorro?')
st.write('Transformaremos tu matriz energética hacia fuentes no solo más económicas sino también más sostenibles:')
st.write('Matriz Energética Actual Vs Proyectada')

st.write(st.session_state.consumo)


st.write(st.session_state.fuente)
