import streamlit as st
import pandas as pd
import numpy as np
#from yahoofinance import HistoricalPrices

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Energy", page_icon="🔋")

st.title('Novus Energy 🔋')
st.header("Monitor de Acciones de Empresas Energéticas ⚡")
st.write("Información desde Yahoo Finance - ajustando compatibilidad con Streamlit")

#req = HistoricalPrices('AAPL')
