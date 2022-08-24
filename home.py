import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Energy", page_icon=":battery:")

st.title('Novus Energy 🔋')
st.header("Salvemos juntos el planeta 🌎")

st.write("Bienvenidos al futuro energético 👋")

st.markdown(
  """
  En esta web encontrarás:
  - 🔎  Diagnóstico de tu necesidad energética y presupuestal
  - 🛒  Recomendación de Portafolio de Servicios Requeridos
  - ✍️  Propuesta Inteligente de Contrato
  
  Todo lo anterior basado en:
  - Tecnología para la optimización: Planes de Ahorro o Repotenciación
  - Tecnología para la neutralidad de carbono: Planes de Mitigación
  - Tecnología para salvar el planeta: Planes de Adaptación
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)
