
import streamlit as st
import os
import sys

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import depuracion.depuracion as dp
#path raiz
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+"\\files"
duplicados = 0
erroneos = 0

st.set_page_config(page_title="Auto Send")

st.header(f'Depurar Números', anchor= False)

exel = st.file_uploader('Cargar hoja de calculo', type='xlsx')

if exel is not None:# si no esta vacio el archivo lo descargo y guardo
    with open(f"files\\{exel.name}","wb") as f:
        #se escribe y guarda el archivo
        f.write(exel.read())
        nombre_archivo = exel.name


def iniciar():
    global duplicados, erroneos
    dp.DepuracionCompleta(nombre_archivo)


if exel is not None:
    Bt_Empezar = st.button('Empezar',on_click=iniciar, disabled = False)
else:
    Bt_Empezar = st.button('Empezar', disabled = True)
st.subheader('Archivos filtrados')
with open(path+"\\Depurado - Erroneos.xlsx","rb") as file:
    st.download_button(label="Números erroneos",
                    data=file,
                    file_name="Depurado - Erroneos.xlsx",
                    mime="text/csv" )
    
with open(path+"\\Depurado - Validos.xlsx","rb") as file:
    st.download_button(label="Números validos",
                    data=file,
                    file_name="Depurado - Validos.xlsx",
                    mime="text/csv")
