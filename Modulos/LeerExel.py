import pandas as pd

def LevantarNumeros(ruta):
    # Ruta del archivo (puede ser un CSV o un Excel)
    ruta_archivo = ruta  # Cambia esto por el nombre de tu archivo

    # Leer el archivo (ajusta el método si es Excel)
    try:
        df = pd.read_excel(ruta_archivo)  # Usa pd.read_excel() si es un archivo .xlsx
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit()

    return df["telefono"]

def LevantarNombres(ruta):
    # Ruta del archivo (puede ser un CSV o un Excel)
    ruta_archivo = ruta  # Cambia esto por el nombre de tu archivo

    # Leer el archivo (ajusta el método si es Excel)
    try:
        df = pd.read_excel(ruta_archivo)  # Usa pd.read_excel() si es un archivo .xlsx
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit()

    return df["Nombre"]

if __name__ == "__main__":
    print(LevantarNumeros(Ruta="C:\\Users\\Sistemas\\Desktop\\AutoSend\\Files\\test.xlsx")[0])