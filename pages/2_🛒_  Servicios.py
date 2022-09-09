import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Gracias a tu Diagnóstico🔎 sabemos que podemos ahorrarte💰:')
st.write('1 año: XXX')
st.write('5 años: YYYY')
st.write('El portafolio de servicios personalizado 🛒 a tu necesidad🎯 es:')

st.write('BLA BLA BLA')

st.write('Empecemos ahora 🕰')

st.write('¿Cómo materializaremos el ahorro?')
st.write('Transformaremos tu matriz energética hacia fuentes no solo más económicas sino también más sostenibles:')
st.write('Matriz Energética Actual Vs Proyectada')

theta = np.linspace(0,2*np.pi)
r = 5 + 50*theta

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r)

plt.show()
