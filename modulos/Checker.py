import ctypes, os

def check(st):
    try:
        open("C:\\zact\\new.txt")
    except:
        ctypes.windll.user32.MessageBoxW(0," Faltan archivos, contactarse con soporte", "Alerta de uso",0x30, 0)
        st.stop()
        os.exit(0)