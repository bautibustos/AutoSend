import streamlit as st
def ErrorCarga(error_mensaje):
    st.error(icon="🚨",body=f"ERROR \n{error_mensaje}")
