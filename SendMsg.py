import webbrowser,time, os, pyautogui, random
import Modulos.CopyImg as CopyImg
import Modulos.ManejoExel as LE
import win32gui, win32con, Modulos.utils as utils, threading
#from Interface import ErrorCarga
"""
Problemas a revisar:
    - Detectar que el numero de telefono puede dar error
    - Imagen suele salir rallada o una linea de mala carga
Pendientes:
    - revisar formato de los numeros
"""

#carpeta donde se guarda la imagen
path = os.getcwd()+"\\Files"

def AddImagen(nombre_imagen):
    try:#intenta ver si hay imagen, si la hay no hay error, si no hay error copia la imagen
        CopyImg.Copy(f"{path}\\{nombre_imagen}")
    except Exception as e:
        print("Error al copiar la imagen: ",e)

def Send(mensaje = None,
         imagen = None, imagen_texto = None,
         nombre_archivo = str):

    flag_nombre = bool
    #ubicacion del exel
    path_file =  f"{path}\\{nombre_archivo}"

    #Preguntamos si esta la columna
    if LE.LevantarNumeros(path_file) is False:
        utils.ErrorCarga(error_mensaje='Columna "Telefono" No encontrada')
    
    else:#si la columna esta
        # esta funcion retorna una lista y bool y selecciono el bool para saber si hay pintados
        flag_celda = LE.CeldaPintada(ruta=path_file, nombre_columna= "Telefono")
        if  flag_celda[0] is False:
            #guardo los numeros desde 0
            numeros_de_telefono = LE.LevantarNumeros(path_file)
        else:
            #si no guardo los numeros que no esten pintados
            numeros_de_telefono = LE.CeldaPintada(ruta=path, nombre_columna= "Telefono")[1]


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
        #abre Whatsapp desktop dentro del chat del numero y utilizando el texto enviado
        webbrowser.open(f'whatsapp://send?phone={numero}')#&text={text}

        #espera para darle tiempo a abrir el chat
        time.sleep(random.choice([1.5, 1.4, 1.6]))

        #Revisar si hay que enviar imagen
        if imagen != None:       
            # pega la imagen
            pyautogui.hotkey("ctrl","v")
            # tiempo de espera en lo que carga la imagen
            time.sleep(random.choice([1.5, 1.4, 1.6]))

            # Si el texto de la imagen no esta vacio lo escribe
            if imagen_texto != None:
                #si es True es xq hay nombre y lo remplaza por el valor de la lista
                try:
                    if flag_nombre:
                        imagen_edit = imagen_texto.replace("USUARIO", nombre[contador_nombre])
                except:
                    pyautogui.write(imagen_edit)
            
            #esper antes de enviar la imagen
            time.sleep(random.choice([1.4, 1.5, 1.6]))
            pyautogui.press("enter")
            #espera entre proximo chat y / o mensaje
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
            time.sleep(random.choice([1.3, 1.2, 1,4]) )
            #enviar mensaje
            pyautogui.press("enter")
        
        #contador para recorrer
        contador_nombre = contador_nombre + 1
        
        # pintar numero de telefono
        threading.Thread(target=LE.PintarUsados, args=(path_file, "Telefono", numero)).join
        #LE.PintarUsados(ruta=path_file, 
         #               nombre_columna="Telefono",
          #              numero_telefono=numero)
        
        #espera para abrir proximo chat
        time.sleep(random.choice([1.5, 1.4, 1.3]))
        

if __name__ == "__main__":
    Send(mensaje="USUARIO saludos",
         nombre_archivo="test.xlsx")