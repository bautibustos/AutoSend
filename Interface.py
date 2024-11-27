import streamlit as st
import SendMsg

st.set_page_config(page_title="Auto Send")

#titulo
st.header(f'Auto Enviar WhatsApps')


#entry para el mensaje
mensaje = st.text_area('Mensaje a enviar',height = 80, value = None)

#si esta checkeado entra a generar el boton para cargarla

imagen = st.file_uploader('Cargar imagen', type=['png','jpg'])
if imagen is not None:# si no esta vacio el archivo lo descargo y guardo
    #                           con path (var.name).suffix rescata la extension
    with open(f"Files\\{imagen.name}","wb") as f:
        #se escribe y guarda el archivo
        f.write(imagen.read())

imagen_texto =  st.text_area("Pie de la imagen", height = 69, value = None)

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
    if imagen is not None:
        nombre_imagen = imagen.name
    else:
        nombre_imagen =  None
    #llamo a la funcion para que envie el mensaje
    SendMsg.Send(
                mensaje = mensaje, 
                imagen = nombre_imagen,
                imagen_texto = imagen_texto,
                nombre_archivo = nombre_archivo
                )

#boton para empezar a mandar el mensaje
if exel is not None and (imagen is not None or mensaje is not None):
    Bt_Empezar = st.button('Empezar',on_click=enviar, disabled = False)
else:
    Bt_Empezar = st.button('Empezar',on_click=enviar, disabled = True)