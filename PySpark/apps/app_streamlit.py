"""Ejecutar con python -m streamlit run apps/app_streamlit.py desde PySpark."""

import streamlit as st

from panel_siniestros import cargar_datos, distritos, figura_panel

st.set_page_config(page_title='Panel de siniestros', layout='wide')
st.title('Siniestros de tráfico en Barcelona')
try:
    datos = cargar_datos()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

distrito = st.sidebar.selectbox('Distrito', distritos(datos))
periodo = st.sidebar.slider('Mes inicial y final', 1, 12, (1, 12))
st.plotly_chart(figura_panel(datos, distrito, periodo))
st.caption('Los recuentos describen expedientes registrados. Para comparar riesgo hace falta medir la exposición al tráfico.')
