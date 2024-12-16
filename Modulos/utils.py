import streamlit as st
def ErrorCarga(error_mensaje):
    st.error(icon="🚨",body=f"ERROR \n{error_mensaje}")

def Warning(warning_mensaje):
    st.warning(icon="⚠️",body=f"ALERTA \n{warning_mensaje}")