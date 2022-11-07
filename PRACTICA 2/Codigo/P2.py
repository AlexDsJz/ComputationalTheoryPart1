import numpy as np
from functions import *
import sys

def getPrimos(n):
    primos = []
    unos = []
    largo =[]
    cont = -1

    f_primo1 = open("../PARCIAL 1/PROGRAMAS/Programa2/outputs/primosbin.txt", "w", encoding="utf-8")
    f_primo2 = open("../PARCIAL 1/PROGRAMAS/Programa2/outputs/primosint.txt", "w", encoding="utf-8")

    f_primo1.write("{ε")
    f_primo2.write("{ε")
    for i in range (2,n+1):
        if Primo(i):
            primos.append(i)
            binario = bin(i)[2:]
            f_primo1.write(','+binario)
            cont+=1
            f_primo2.write(','+str(i))    
            unos.append(binario.count('1'))
            largo.append(cont) 
    
    f_primo1.write("}")
    f_primo2.write("}")
    f_primo1.close()
    f_primo2.close()
    graficar(largo, unos, "Cadenas", "Cantidad de 1's")
    graficar(largo, np.log10(unos), "Cadenas", "Cantidad de 1's (Log10)")
    graficar(largo, np.log2(unos), "Cadenas", "Cantidad de 1's (Log2)")

#Generamos nuestro menú de opciones
opc = "1"
print("MENU DE OPCIONES")
while opc == "1":
    
    opc = input("Seleccione una opción: \n1.- Ingresar n \n2.- Finalizar\n")
    
    if opc == "1":
        n = int(input("Ingrese el valor de n: "))
        getPrimos(n)
    else:
        if opc == "2":
            print(f"FIN DE LA EJECUCION")
            sys.exit(0)
        else:
            if opc != "1":
                print("Seleccione una opcion valida")