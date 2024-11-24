import webbrowser,time, os, pyautogui
from urllib.parse import quote
import Modulos.CopyImg as CopyImg

"""
Problemas a revisar:
    - Detectar que el numero de telefono puede dar error
    - Imagen suele salir rallada o una linea de mala carga
Pendientes:
    - Levantar exel, leer de una columna presisa
    - revisar formato de los numeros
    - hacer que envie al listado de personas.
"""

def AddImagen():
    try:#intenta ver si hay imagen, si la hay no hay error, si no hay error copia la imagen

        #carpeta donde se guarda la imagen
        path = os.getcwd()+"\\imagen"
        
        #la imagen deberia estar sola para ser la unica seleccion
        img = os.listdir(path=path)[0]

        #print(os.listdir(path=path))
        
        CopyImg.Copy(path+'\\'+img)
    except Exception as e:
        print("Error al copiar la imagen: ",e)

def Send(mensaje = "mensaje default", numero = "+543385448553", imagen = False):
    # convierte en texto utilizable para url
    text = quote(mensaje) 
    

    #abre Whatsapp desktop dentro del chat del numero y utilizando el texto enviado
    webbrowser.open(f'whatsapp://send?phone={numero}&text={text}')

    #espera para darle tiempo a abrir el chat
    time.sleep(0.5)

    #Revisar si hay que enviar imagen
    if imagen:
        #llama a la funcion de la imagen
        AddImagen()
        
        # pega la imagen
        pyautogui.hotkey("ctrl","v")
        time.sleep(0.4)
    
    #enviar mensaje
    pyautogui.press("enter")

if __name__ == '__main __':
    for i in range(0,3):
        Send(numero="+5493704412273",imagen = True)