import streamlit as st

st.title('Tenemos un contrato 📜  personalizado 🎯 a tu diagnóstico 🔎 ')
st.write('Porque tu necesidad es única, también tu contrato, pero primero regístrate:')

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')

st.button('Descargar Contrato Inteligente')

st.text_input("Incorpore su firma si está de acuerdo con las condiciones")

st.text_input("Incorpore su correo electrónico para envío de factura")
st.write('Gracias por confiar en los servicios de Novus Energy 🔋')
