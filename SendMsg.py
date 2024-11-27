import webbrowser,time, os, pyautogui, random
import Modulos.CopyImg as CopyImg
import Modulos.LeerExel as LE
import win32gui, win32con
"""
Problemas a revisar:
    - Detectar que el numero de telefono puede dar error
    - Imagen suele salir rallada o una linea de mala carga
Pendientes:
    - Levantar exel, leer de una columna presisa
    - revisar formato de los numeros
    - Usar nombre de personas, levantar desde una columna con algun nombre caracteristico
    - hacer que envie al listado de personas.
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
    #ubicacion del exel
    path_file =  f"{path}\\{nombre_archivo}"
    #guardamos numeros de telefono
    numeros_de_telefono = LE.LevantarNumeros(path_file)

    #para que se ejecute el levantar personas, se deben cumplir las condiciones que se encuentren essos textos y que no sean nulos
    if (mensaje is not None and "USUARIO" in mensaje) or (imagen_texto is not None and "USUARIO" in imagen_texto):
        # Nombre de las personas    
        nombre = LE.LevantarNombres(path_file)

    # busca la existencia del proceso
    hwnd = win32gui.FindWindow(None, "WhatsApp")
    # Restaurar si está minimizada
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE) 

    # la forza a ponerse en primer plano
    # win32gui.SetForegroundWindow(hwnd) #esta linea por algun motivo no fuerza a whatsapp y da error.

    #si hay que cargar imagen se copia para despues ser pegada
    if imagen != None:
        #llama a la funcion de la imagen
        AddImagen(imagen)

    contador_nombre = 0
    mensaje_edit = mensaje
    imagen_edit = imagen_texto
    for numero in numeros_de_telefono:
        #abre Whatsapp desktop dentro del chat del numero y utilizando el texto enviado
        webbrowser.open(f'whatsapp://send?phone=+{numero}')#&text={text}

        #espera para darle tiempo a abrir el chat
        time.sleep(random.choice([1.5, 1.4, 1.6]))

        #Revisar si hay que enviar imagen
        if imagen != None:       
            # pega la imagen
            pyautogui.hotkey("ctrl","v")
            time.sleep(random.choice([1.5, 1.4, 1.6]))
            if imagen_texto != None:
                imagen_edit = imagen_texto.replace("USUARIO", nombre[contador_nombre])
                pyautogui.write(imagen_edit)

        if mensaje != None:
        # Escribir mensaje
            mensaje_edit =  mensaje.replace("USUARIO", nombre[contador_nombre])
            
            #escribo el mensaje manualmente
            pyautogui.write(mensaje_edit)
        
        #contador para recorrer
        contador_nombre = contador_nombre + 1

        time.sleep(random.choice([0.3, 0.2, 0,4]))
        #enviar mensaje
        pyautogui.press("enter")
        time.sleep(random.choice([1.5, 1.4, 1.3]))
        

if __name__ == "__main__":
    Send(mensaje="USUARIO saludos",
         imagen=True, 
         nombre_imagen="test.jpg",
         nombre_archivo="test.xlsx")