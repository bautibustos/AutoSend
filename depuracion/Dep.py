import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import webbrowser, time, win32gui, win32con
import modulos.utils as utils
import modulos.ManejoExel as LE  # Ahora debe encontrarlo correctamente

Fila = 0
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+"\\files"


def Depuracion(nombre_archivo, tiempo, cantidad_de_numeros=100):
    global Fila
    path_file = os.path.join(path, nombre_archivo)

    # Preguntamos si está la columna
    print(LE.LevantarNumeros(path_file))
    if LE.LevantarNumeros(path_file) is False:
        utils.ErrorCarga(error_mensaje='Columna "Telefono" No encontrada')    
    else:
        # Obtener los números de teléfono
        numeros_de_telefono = LE.LevantarNumeros(path_file)

    # Buscar la existencia del proceso de WhatsApp
    hwnd = win32gui.FindWindow(None, "WhatsApp")
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restaurar si está minimizada

    for numero in numeros_de_telefono:
        if Fila >= cantidad_de_numeros:
            break
        Fila += 1
        webbrowser.open(f'whatsapp://send?phone={int(numero)}')
        time.sleep(tiempo)

if __name__ == "__main__":
    Depuracion("P_uni.xlsx", 8, 50)
