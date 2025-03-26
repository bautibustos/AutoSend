import streamlit as st, depuracion.Dep as Dep

st.header(f'Depurar Numeros')

slider = st.slider("Tiempo entre chat y chat", min_value=1, max_value=10, value=3)

