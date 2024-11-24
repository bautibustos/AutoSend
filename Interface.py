import streamlit as st
from pathlib import Path
import SendMsg

#titulo
st.header('Auto Enviar WhatsApps')

#Entry para el mensaje
TextoMensaje = st.text_input('Mensaje a enviar')

#guardar el estado de la imagen
EstadoImagen = st.checkbox('Imagen')

#si esta checkeado entra a generar el boton para cargarla
if EstadoImagen:
    imagen = st.file_uploader('Cargar imagen (opcional)', type=['png','jpg'])
    if imagen is not None:# si no esta vacio el archivo lo descargo y guardo
        #                           con path (var.name).suffix rescata la extension
        with open(f"Files\\ImgLoaded{Path(imagen.name).suffix}","wb") as f:
            #se escribe y guarda el archivo
            f.write(imagen.read()) 

# titulo
st.header('Exel de numeros de telefonos')

#guardo el exel y pido que solamente cargen los xlsx
exel = st.file_uploader('Cargar exel', type='xlsx')
if exel is not None:# si no esta vacio el archivo lo descargo y guardo
    #                              con path (var.name).suffix rescata la extension
    with open(f"Files\\FileLoaded{Path(exel.name).suffix}","wb") as f:
        #se escribe y guarda el archivo
        f.write(exel.read())

# CallBack para evitar que la funcion se llame de forma incorrecta
def enviar():
    #llamo a la funcion para que envie el mensaje
    SendMsg.Send(mensaje=TextoMensaje, imagen=EstadoImagen)

#boton para empezar a mandar el mensaje
st.button('Empezar',on_click=enviar)