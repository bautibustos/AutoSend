from PIL import Image
import win32clipboard as clipboard # type: ignore
import io

def Copy(ruta_imagen):
    # Abrir la imagen con Pillow
    imagen = Image.open(ruta_imagen).convert('RGB')

    # Convertir la imagen a formato BMP
    salida = io.BytesIO()
    # Genera el formato para guardar en el porta papeles
    imagen.save(salida, format="BMP")
    # Omitir los primeros 14 bytes (cabecera de archivo BMP)
    datos_bmp = salida.getvalue()[14:]  
    salida.close()

    # Copiar al portapapeles
    clipboard.OpenClipboard()
    #limpia el portapapeles
    clipboard.EmptyClipboard()
    #copia el contenido
    clipboard.SetClipboardData(clipboard.CF_DIB, datos_bmp)
    clipboard.CloseClipboard()
