from Modulos.ManejoExel import LevantarNumeros
import os
path = os.getcwd()+"\\Files\\test.xlsx"

Exel = LevantarNumeros(path)

# verifico que tengan el mas 54
for numero in Exel:
    item = str(numero)
    if not "+54" in item:
        if not "54" in item[:2]:
            item = "54"+item
        if not "+" in item:
            item = "+"+item
    print(item, not "+54" in item)