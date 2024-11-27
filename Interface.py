import streamlit as st
import SendMsg

nombre_imagen = str
nombre_archivo = str
#titulo
st.header('Auto Enviar WhatsApps')

#Entry para el mensaje
TextoMensaje = st.text_input('Mensaje a enviar')

#guardar el estado de la imagen
estado_imagen = st.checkbox('Imagen')

#si esta checkeado entra a generar el boton para cargarla

imagen = st.file_uploader('Cargar imagen (opcional)', type=['png','jpg'])
if imagen is not None:# si no esta vacio el archivo lo descargo y guardo
    #                           con path (var.name).suffix rescata la extension
    with open(f"Files\\{imagen.name}","wb") as f:
        #se escribe y guarda el archivo
        f.write(imagen.read()) 
        nombre_imagen = imagen.name

# titulo
st.header('Exel de numeros de telefonos')

#guardo el exel y pido que solamente cargen los xlsx
exel = st.file_uploader('Cargar exel', type='xlsx')
if exel is not None:# si no esta vacio el archivo lo descargo y guardo
    #                              con path (var.name).suffix rescata la extension
    with open(f"Files\\{exel.name}","wb") as f:
        #se escribe y guarda el archivo
        f.write(exel.read())
        nombre_archivo = exel.name

# CallBack para evitar que la funcion se llame de forma incorrecta
def enviar():
    nombre_imagen = str
    #llamo a la funcion para que envie el mensaje
    SendMsg.Send(
                mensaje=TextoMensaje, 
                imagen=estado_imagen,
                nombre_imagen = nombre_imagen,
                nombre_archivo = nombre_archivo
                )

#boton para empezar a mandar el mensaje
st.button('Empezar',on_click=enviar)