# -*- coding: utf-8 -*-
import webbrowser,time, os, pyautogui, random
import Modulos.CopyImg as CopyImg
import Modulos.ManejoExel as LE
import win32gui, win32con, Modulos.utils as utils 
import json   
#from Interface import ErrorCarga
"""
Problemas a revisar:
    - Detectar que el numero de telefono puede dar error

Pendientes:
    - revisar formato de los numeros
"""


#carpeta donde se guarda la imagen
path = os.getcwd()+"\\Files"

def CargarJson():
    with open(f"{os.getcwd()}\\config.json", 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
    
def AddImagen(nombre_imagen):
    try:#intenta ver si hay imagen, si la hay no hay error, si no hay error copia la imagen
        CopyImg.Copy(f"{path}\\{nombre_imagen}")
    except Exception as e:
        utils.ErrorCarga(error_mensaje= "Problemas con la imagen")
        #print("Error al copiar la imagen: ",e)

def Send(mensaje = None,
        imagen = None, imagen_texto = None,
        nombre_archivo = str):

    flag_nombre = bool
    #ubicacion del exel
    path_file =  f"{path}\\{nombre_archivo}"
    
    tiempos = CargarJson()["tiempo"]
    cant_msg = CargarJson()["cantidad_mensajes"]

    #Preguntamos si esta la columna
    if LE.LevantarNumeros(path_file) is False:
        utils.ErrorCarga(error_mensaje='Columna "Telefono" No encontrada')
    
    else:#si la columna esta
        # esta funcion retorna una lista y bool y selecciono el bool para saber si hay pintados
        numeros_de_telefono = LE.LevantarNumeros(path_file)

    #para que se ejecute el levantar personas, se deben cumplir las condiciones que se encuentren essos textos y que no sean nulos
    if (mensaje is not None and "USUARIO" in mensaje) or (imagen_texto is not None and "USUARIO" in imagen_texto):
        # Nombre de las personas    
        nombre = LE.LevantarNombres(path_file)
        if nombre is not False:
            flag_nombre = True
        else:
            utils.ErrorCarga(error_mensaje='Columna "Nombre" no encontrada')
             
    else:
        flag_nombre = False

    # busca la existencia del proceso
    hwnd = win32gui.FindWindow(None, "WhatsApp")
    # Restaurar si está minimizada
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE) 

    # la forza a ponerse en primer plano
    # win32gui.SetForegroundWindow(hwnd) #esta linea por algun motivo da error con la interfaz

    #si hay que cargar imagen se copia para despues ser pegada
    if imagen != None:
        #llama a la funcion de la imagen
        AddImagen(imagen)

    contador_nombre = 0 #contador para el nombre
    mensaje_edit = mensaje # si no no permite editarlo
    imagen_edit = imagen_texto
    # agregar el check si es es falso
    for numero in numeros_de_telefono:
        
        try:
            numero = int(numero)#intenta volverlo entero pasa sacar decimales
        except:
            pass
        
        """
        agregar para que la cantidad de mensajes la defina en el archivo de config
        """
        # si supera a los 200 mensajes
        if contador_nombre == 195:#aviso de alerta qque se llegaron a los 200 msg
            utils.Warning(warning_mensaje=f" Estas por llegar al limite de 200 mensajes.")
            break
        else:
            if cant_msg == contador_nombre:
                break
            else:
                if str(numero) != "nan":# convierte el numero en str para encontrar el nan
                    item = str(numero)#lo convierto enstr
                    if not "+54" in item:#me fijo tiene el mas +54
                        #comparo si los primeros dos items son 54
                        if not "54" in item[:2]:
                            item = "54"+item#agro el 54 si no lo tiene
                        if not "+" in item:# pregunto si tengo el +
                            item = "+"+item# agrego el + si no esta
                    #elimino guiones de por medio
                    if "-" in item:
                        item.replace('-','')
                    #elimino espacios si hay
                    if " " in item:
                        item.replace(' ','')
                    # limpiar parentesis
                    if "(" in item:
                        item.replace('(', '')
                    # limpiar parentesis
                    if ')' in item:
                        item.replace(')', '')

                    numero = item # reemplazo el valor nuevo
                    
                    #abre Whatsapp desktop dentro del chat del numero y utilizando el texto enviado
                    webbrowser.open(f'whatsapp://send?phone={numero}')#&text={text}

                    #espera para darle tiempo a abrir el chat
                    time.sleep(random.choice([2.7, 2.8, 2.9]))

                    #Revisar si hay que enviar imagen
                    if imagen != None:

                        # pega la imagen
                        pyautogui.hotkey("ctrl","v")

                        # tiempo de espera en lo que carga la imagen
                        time.sleep(random.choice([2.7, 2.8, 2.9]))

                        # Si el texto de la imagen no esta vacio lo escribe
                        if imagen_texto != None:
                            #si es True es xq hay nombre y lo remplaza por el valor de la lista
                            try:
                                if flag_nombre:
                                    imagen_edit = imagen_texto.replace("USUARIO", nombre[contador_nombre])
                                    pyautogui.write(imagen_edit)
                            except:
                                pyautogui.write(imagen_edit)
                        
                        #esper antes de enviar la imagen
                        time.sleep(random.choice([tiempos+0.7, tiempos+0.8, tiempos+0.9]))

                        # enviar mensaje
                        pyautogui.press("enter")

                        #espera entre proximo mensaje
                        time.sleep(random.choice([0.6, 0.7, 0.8]))
                        

                    #detecta que encuentre un mensaje
                    if mensaje != None:
                    # Escribir mensaje
                        try:
                            if flag_nombre:#si es que hay usuario, reemplaza por el valor de la lista
                                mensaje_edit =  mensaje.replace("USUARIO", nombre[contador_nombre])
                        except:
                            mensaje_edit
                        #escribo el mensaje manualmente
                        pyautogui.write(mensaje_edit)
                        #tiempo de espera antes de enviar el mensaje
                        time.sleep(random.choice([0.3+tiempos, tiempos+0.2, tiempos+0.4]) )
                        #enviar mensaje
                        pyautogui.press("enter")
                    
                    #contador para recorrer
                    contador_nombre +=1
                    
                    #espera para abrir proximo chat
                    time.sleep(random.choice([tiempos+0.5, tiempos+0.4, tiempos+0.3]))
                else:
                    contador_nombre +=1
        

if __name__ == "__main__":
    Send(mensaje="USUARIO saludos",
         nombre_archivo="test.xlsx")