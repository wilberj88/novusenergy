import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Energy", page_icon="🔋")

st.title('Novus Energy 🔋')
st.header("Ahorra 💰 mientras salvamos juntos el planeta 🌎")

st.write("Bienvenidos al futuro energético 👋")

st.markdown(
  """
  En esta web encontrarás:
  - 🔎 _    Diagnóstico de tu necesidad energética y presupuestal
  - 🛒 _    Recomendación de Portafolio de Servicios Requeridos
  - ✍️ _     Propuesta Inteligente de Contrato
  
  Todo lo anterior basado en:
  - Tecnología para la optimización: Planes de Ahorro o Repotenciación
  - Tecnología para la neutralidad de carbono: Planes de Mitigación
  - Tecnología para salvar el planeta: Innovación en toda la cadena energética y Planes de Adaptación
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)


#st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000, key="consumo")

#st.slider('En millones de pesos al año: ¿cuánto inviertes en energía?', 0, 1000000, key="presupuesto")

#st.radio('¿Cuál es tu fuente principal de energia?', ['Agua', 'Carbon', 'Combustible', 'Termoelectrica', 'Solar', 'Viento'], key="fuente")

