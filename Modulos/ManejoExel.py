import pandas as pd
def LevantarNumeros(ruta):
    # Ruta del archivo (puede ser un CSV o un Excel)
    with pd.ExcelFile(ruta) as xls:
    # Leer el archivo (ajusta el método si es Excel)
        df = pd.read_excel(xls)  # Usa pd.read_excel() si es un archivo .xlsx
    try:
        return df["Telefono"]# agregar tolerancia mayusculas y minusculas
    except:
        return False


def LevantarNombres(ruta):
    # Ruta del archivo (puede ser un CSV o un Excel)
    ruta_archivo = ruta  

    # Leer el archivo (ajusta el método si es Excel)
    df = pd.read_excel(ruta_archivo)  # Usa pd.read_excel() si es un archivo .xlsx
    try:
        return df["Nombre"]
    except:
        return False

def LevantarMensaje(ruta):
    #ruta del archivo
    ruta_archivo = ruta
    # abrimos el execl
    df = pd.read_excel(ruta_archivo)
    
    #Buscamos la columna mensaje
    try:
        return df["Mensaje"]
    except:
        return False

if __name__ == "__main__":
    pass